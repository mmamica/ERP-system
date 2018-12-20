from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfileInfo
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate
import requests
from admin_app.models import Magazine


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'city'}))
    street = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'street'}))
    house_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'id': 'house_number', 'onchange': 'geocode(platform)'}))

    def clean(self):
        city = self.cleaned_data.get('city')
        street = self.cleaned_data.get('street')
        house_number = self.cleaned_data.get('house_number')
        search_text = city + ' ' + street + ' ' + ' ' + str(house_number)

        message = requests.get('https://geocoder.api.here.com/6.2/geocode.json',
                               {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                'searchtext': search_text})

        data = message.json()
        if (data['Response']['View']==[]):
            raise forms.ValidationError("Nieprawidłowy adres")

        latitude = data['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = data['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']

        waypoint0 = 'geo!' + str(latitude) + ',' + str(longitude)
        waypoint1 = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)

        message2 = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                 'waypoint0': waypoint0, 'waypoint1': waypoint1,
                                 'mode': 'fastest;car;traffic:disabled'})

        data2 = message2.json()
        distance = data2['response']['route'][0]['summary']['distance']
        magazine_distance=Magazine.objects.get(id_magazine=1).radius*1000

        if distance > magazine_distance:
            raise forms.ValidationError("Firma jest za daleko")
        return self.cleaned_data

    class Meta():
        model = UserProfileInfo
        fields = ('company_name', 'phone_number', 'city', 'street', 'house_number', 'profile_pic',
                  'is_client')


class EditUserProfileForm(UserChangeForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Błąd logowania! Spróbuj ponownie")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
