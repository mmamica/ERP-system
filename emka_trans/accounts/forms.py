from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfileInfo
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','first_name','last_name','email','password')


class UserProfileInfoForm(forms.ModelForm):
	city=forms.CharField(max_length=100)
	street = forms.CharField(max_length=100)
	house_number = forms.IntegerField()
	class Meta():
		model=UserProfileInfo
		fields = ('company_name','phone_number','city','street','house_number','profile_pic',
														'is_client')

class EditUserProfileForm(UserChangeForm):
	class Meta():
		model=User
		fields = ('username','first_name','last_name','email','password')


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
	

