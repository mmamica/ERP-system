from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns=[
	url(r'^register_user/$', views.RegisterView.as_view(), name='register_user'),
	url(r'^user_login/$',views.LoginView.as_view(), name='user_login'),
	url(r'profile/(?P<username>[\w]+)$', views.get_user_profile, name='show_profile'),
	url(r'profile/$',views.MyProfileView.as_view(), name='my_profile'),
	url(r'profile/edit/$', views.EditProfileView.as_view() ,name='edit_my_profile'),
	url(r'profile/password/$', views.ChangePasswordView.as_view(), name='change_password'),
]