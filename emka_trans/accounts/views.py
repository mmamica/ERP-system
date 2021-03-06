from _decimal import Decimal

from django.shortcuts import render
from accounts.forms import UserForm, UserProfileInfoForm, EditUserForm, LoginForm, EditProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.base import TemplateView, View
from django.utils.decorators import method_decorator
import requests
from admin_app.models import Magazine,Truck


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):

    """
        Changes the user's password.

        ``form``
            An instance of :model:`accounts.PasswordChangeForm`.

        :template: `accounts/change_password.html`
        :template: `accounts/my_account.html`

    """

    template_name = 'accounts/change_password.html'
    form_class = PasswordChangeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return HttpResponseRedirect(reverse('accounts:edit_my_profile'))
        else:
            return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    """
        Allows the user to edit selected profile elements.

        ``profile_form``
            An instance of `accounts.EditProfileForm`.
        ``user_form``
            An instance of `accounts.EditUserForm`.

        :template:`accounts/edit_my_profile.html`

    """

    template_name = 'accounts/edit_my_profile.html'
    profile_form_class = EditProfileForm
    user_form_class = EditUserForm

    def get(self, request, *args, **kwargs):
        instance_form = UserProfileInfo.objects.get(user=request.user)
        profile_form = self.profile_form_class(instance=instance_form)
        user_form = self.user_form_class(instance=request.user)
        return render(request, self.template_name, {'profile_form': profile_form, 'user_form': user_form})

    def post(self, request, *args, **kwargs):
        instance_form = UserProfileInfo.objects.get(user=request.user)
        profile_form = self.profile_form_class(request.POST, instance=instance_form)
        user_form = self.user_form_class(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            user.save()
            profile.save()

            return HttpResponseRedirect(reverse('accounts:my_profile'))
        return render(request, self.template_name, {"profile_form": profile_form,
                                                    "user_form": user_form})


def get_user_profile(request, username):

    """
    Displays the profile of selected user

    :param request: HttpRequest
    :param username: string
    :template:`accounts/profile.html`
    """
    user = User.objects.get(username=username)
    status = False
    user_id = user.id
    user_profile = UserProfileInfo.objects.get(user=user_id)

    if user_profile.is_client:
        status = True

    return render(request, 'accounts/profile.html', {"user": user, "user_profile": user_profile, "status": status})


class IndexView(TemplateView):
    """
        Displays index page.

        :template:`accounts/index.html`
    """

    template_name = 'accounts/index.html'


@method_decorator(login_required, name='dispatch')
class MyProfileView(TemplateView):

    """
        Displays the profile of the logged in user.

        :template:`accounts/my_account.html`
    """

    template_name = 'accounts/my_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        status = False
        user_id = user.id
        user_profile = UserProfileInfo.objects.get(user=user_id)
        if user_profile.is_client:
            status = True
        context['user'] = user
        context['user_profile'] = user_profile
        return context


@method_decorator(login_required, name='dispatch')
class LogoutView(View):

    """
        Logs out the user.

        :template:`accounts/index.html`
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegisterView(View):
    """
        Registers new user.
        Coordinates are calculated based on the address given by the user

        **Context**

        ``user_form``
            An instance of `accounts.UserForm`.

        ``registered``
            Boolean determining whether the registration was successful.

        **Template:**
        :template: `accounts/register_user.html`
    """

    template_name = 'accounts/register_user.html'
    registered = False

    def post(self, request):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.id_cluster = None

            # make query from form fields
            city = profile_form.cleaned_data['city']
            street = profile_form.cleaned_data['street']
            house_number = profile_form.cleaned_data['house_number']
            search_text = city + ' ' + street + ' ' + ' ' + str(house_number)

            message = requests.get('https://geocoder.api.here.com/6.2/geocode.json',
                                   {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                    'searchtext': search_text})

            data = message.json()
            latitude = data['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
            longitude = data['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']

            for t in Truck.objects.all():
                status1=checkDiv(t.start_latitude,t.start_longitude)
                status2=checkDiv(t.end_latitude,t.end_longitude)
                if (status1==1):
                    if((status2==1 and t.start_longitude>t.end_longitude) or status2==4):
                        if(isBigger(t.start_latitude,t.start_longitude, latitude,longitude) or not isBigger(t.end_latitude,t.end_longitude, latitude,longitude)):
                            profile.id_cluster = t
                    if (status2 == 2 or status2==3 or (status2==1 and t.start_longitude<t.end_longitude)):
                        if (isBigger(t.start_latitude, t.start_longitude, latitude, longitude) and isBigger(t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t
                if (status1==2):
                    if ((status2 == 2 and t.start_longitude < t.end_longitude) or status2 == 3):
                        if (not isBigger(t.start_latitude, t.start_longitude, latitude, longitude) and isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t
                    if ((status2 == 2 and t.start_longitude > t.end_longitude)):
                        if (not isBigger(t.start_latitude, t.start_longitude, latitude, longitude) or isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t
                    if (status2 == 4 or status2 == 1 or (status2 == 2 and t.start_longitude < t.end_longitude)):
                        if (not isBigger(t.start_latitude, t.start_longitude, latitude, longitude) or not isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t

                if (status1==3):
                    if (status2 == 4 or status2==1 ):
                        if (not isBigger(t.start_latitude, t.start_longitude, latitude, longitude) and not isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t
                    if (status2 == 2 or status2 == 3):
                        if (not isBigger(t.start_latitude, t.start_longitude, latitude, longitude) or isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t

                if (status1==4):
                    if ((status2 == 4 and t.start_longitude < t.end_longitude) or status2 == 3 or status2==2):
                        if (isBigger(t.start_latitude, t.start_longitude, latitude, longitude) and not isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t
                    if (status2 == 1 or (status2 == 4 and t.start_longitude > t.end_longitude)):
                        if (isBigger(t.start_latitude, t.start_longitude, latitude, longitude) or isBigger(
                                t.end_latitude, t.end_longitude, latitude, longitude)):
                            profile.id_cluster = t


            profile.latitude = float(latitude)
            profile.longitude = float(longitude)


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            user.save()
            profile.save()

            self.registered = True
        else:
            print(user_form.errors, profile_form.errors)
        return render(request, self.template_name,
                      {'user_form': user_form, 'profile_form': profile_form,
                       'registered': self.registered})

    def get(self, request):
        registered = self.registered
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        return render(request, self.template_name,
                      {'user_form': user_form, 'profile_form': profile_form,
                       'registered': registered})


class LoginView(TemplateView):

    """
        Allows the user to log in.

        **Context**
            ``form``
                An instance of `accounts.LoginForm`.

        **Template:**
            :template:`accounts/login.html`
            :template:`accounts/index.html`

    """
    template_name = 'accounts/login.html'

    def post(self, request):
        form = LoginForm(request.POST or None)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponseRedirect("Account not active")
        else:
            return render(request, self.template_name, {'form': form})


def checkDiv(latitude, longitude):
    """
        Calculates the quarter in the coordinate system.
        The center of the coordinate system is the location of the warehouse.

    :param latitude: float
    :param longitude: float
    :return: int
    """
    if latitude > Magazine.objects.get(id_magazine=1).latitude:
        if longitude < Magazine.objects.get(id_magazine=1).longitude:
            return 1
        if longitude > Magazine.objects.get(id_magazine=1).longitude:
            return 2
    else:
        if longitude < Magazine.objects.get(id_magazine=1).longitude:
            return 4
        if longitude > Magazine.objects.get(id_magazine=1).longitude:
            return 3


def isBigger(latitude, longitude,latitude_point, longitude_point):
    """
        Calculates if point with coordinates (latitude, longitude) is above the radius vector.

    :param latitude: float
    :param longitude: float
    :param latitude_point: float
    :param longitude_point: float
    :return: boolean
    """
    ya=latitude
    yb=float(Magazine.objects.get(id_magazine=1).latitude)
    xa=longitude
    xb=float(Magazine.objects.get(id_magazine=1).longitude)
    a=(ya-yb)/(xa-xb)
    b=ya-a*xa
    if(latitude_point>(a*longitude_point+b)):
        return True
    else:
        return False

