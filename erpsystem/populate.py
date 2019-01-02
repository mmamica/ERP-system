import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','emka_trans.settings')

import django
django.setup()

from accounts.models import UserProfileInfo
from django.contrib.auth.models import User
from faker import Faker
from admin_app.models import Truck
from products_app.models import Product
import random

fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        username=fakegen.company()
        email=username+'@gmail.com'
        password='top_secret'
        user= User.objects.create_user(username=username,email=email,password=password);
        truck=Truck.objects.create(id_truck=entry+10,
                                        capacity=random.randint(100,10000),
                                        return_date=fakegen.date(pattern="%Y-%m-%d", end_datetime=None))
        useruser=UserProfileInfo.objects.get_or_create(
            user=user,
            company_name=username,
            phone_number=fakegen.phone_number(),
            longitude=random.randint(20.0,21.0),
            latitude=(random.randint(50.0,51.0)),
            is_client=random.choice([True, False]),
            id_cluster=truck)[0]
        if (useruser.isclient==True):
            user_product=Product.object.get_or_create(
                name=
            )[0]

        else

        
if __name__=='__main__':
    print('population script')
    populate(5)
    print('population completed!')
