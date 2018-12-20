from datetime import timedelta

from django.shortcuts import render
from django.urls import reverse_lazy
import itertools
from django.http import HttpResponse
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)

# Create your views here.
from . import models
from django.http import HttpResponse, HttpResponseForbidden
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from . import models
from order_app.models import Checkout, OrderedProducts
from products_app.models import Product
from admin_app.models import Magazine, Route
from admin_app.models import Truck
from accounts.models import UserProfileInfo
from datetime import datetime
import requests


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView(TemplateView):
    template_name = 'admin_app/admin_app_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class AdminCheckoutListView(ListView):
    model = Checkout
    template_name = 'admin_app/order_list.html'

    def get_queryset(self):
        return Checkout.objects.filter(confirmed=True)


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class AdminCheckoutDetailView(DetailView):
    context_object_name = 'order_details'
    model = Checkout
    template_name = 'admin_app/order_detail.html'
    # un_success_url = reverse_lazy("admin_app:order_list")


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class AdminProductListView(ListView):
    template_name = 'admin_app/product_list.html'
    model = Product


def areAllConsidered(tab):
    for i in range(0, len(tab)):
        if (tab[i] is not None):
            return False
    return True


def onNotConsidered(tab):
    iter = 0
    for i in range(0, len(tab)):
        if (tab[i] is not None):
            iter = iter + 1
    if (iter == 1):
        return True
    return False


"""""
def areAllConsideredIJ(tab):
    for i in range (0, len(tab)):
        if(tab[i][j] is not None):
            return False
    for j in range (0, len(tab)):
        if(tab[i][j] is not None):
            return False
    return True

"""


def maxCell(tab):
    max = 0
    imax = None
    jmax = None
    for i in range(0, len(tab)):
        for j in range(i, len(tab)):
            if (tab[i][j] is not None):
                if (tab[i][j] > max):
                    max = tab[i][j]
                    imax = i
                    jmax = j
    return (imax, jmax)


def wasCondidered(orders, ordersConsidered):
    for i in range(0, len(orders)):
        for j in range(0, len(ordersConsidered)):
            if orders[i] == ordersConsidered[j]:
                return True
    return False


def maxFromI(tab, i):
    max = 0
    jmax = None
    for j in range(0, len(tab)):
        if tab[i][j] > max:
            max = tab[i][j]
            jmax = j
    return j


def maxFromJ(tab, j):
    max = 0
    imax = None
    for i in range(0, len(tab)):
        if tab[i][j] > max:
            max = tab[i][j]
            imax = i
    return i


def deleteAllFromIndex(tab, index):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if (i == index or j == index):
                tab[i][j] = None


def ClarkeWright(date, claster):
    orders = None


    for c in Checkout.objects.all():
        if str(c.date) == date:
            if orders is None:
                orders = OrderedProducts.objects.filter(id_checkout=c) #tu trzeba przefiltrować jeszcze z clastrem
            else:
                orders = orders | OrderedProducts.objects.filter(id_checkout=c) #i tu

    if(orders is not None):
        tab = [None] * len(orders)
        for x in range(len(tab)):
            tab[x] = [None] * len(orders)
        ordersConsideredQuery = orders
        ordersConsidered = ordersConsideredQuery[::1]

        for i in range(0, len(orders) - 1):
            for j in range(i + 1, len(orders)):
                latitudei = UserProfileInfo.objects.get(user_id=orders[i].name_deliver).latitude
                longitudei = UserProfileInfo.objects.get(user_id=orders[i].name_deliver).longitude

                latitudej = UserProfileInfo.objects.get(user_id=orders[j].name_deliver).latitude
                longitudej = UserProfileInfo.objects.get(user_id=orders[j].name_deliver).longitude

                waypointi = 'geo!' + str(latitudei) + ',' + str(longitudei)
                waypointj = 'geo!' + str(latitudej) + ',' + str(longitudej)
                waypointm = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
                    Magazine.objects.get(id_magazine=1).longitude)

                messageim = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                         {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                          'waypoint0': waypointi, 'waypoint1': waypointm,
                                          'mode': 'fastest;car;traffic:disabled'})

                messagejm = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                         {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                          'waypoint0': waypointj, 'waypoint1': waypointm,
                                          'mode': 'fastest;car;traffic:disabled'})

                messageij = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                         {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                          'waypoint0': waypointj, 'waypoint1': waypointi,
                                          'mode': 'fastest;car;traffic:disabled'})

                dataim = messageim.json()
                distanceim = dataim['response']['route'][0]['summary']['distance']

                datajm = messagejm.json()
                distancejm = datajm['response']['route'][0]['summary']['distance']

                dataij = messageij.json()
                distanceij = dataij['response']['route'][0]['summary']['distance']

                saving = distanceim + distancejm - distanceij

                if ((orders[i].amount + orders[j].amount) > Truck.objects.get(id_truck=claster).capacity):
                    tab[i][j] = None;
                else:
                    tab[i][j] = saving

        allRoutes = []
        while (not areAllConsidered(ordersConsidered)):
            if (not onNotConsidered(ordersConsidered)):
                sumAmount = 0
                imax = maxCell(tab)[0]
                jmax = maxCell(tab)[1]
                sumAmount = (orders[imax].amount + orders[jmax].amount)
                ordersConsidered[imax] = None
                ordersConsidered[jmax] = None
                tab[imax][jmax] = None
                deleteAllFromIndex(tab, imax)
                deleteAllFromIndex(tab, jmax)
                route = [orders[imax].id, orders[jmax].id]
                latitudei = UserProfileInfo.objects.get(user_id=orders[imax].name_deliver).latitude
                longitudei = UserProfileInfo.objects.get(user_id=orders[imax].name_deliver).longitude

                latitudej = UserProfileInfo.objects.get(user_id=orders[jmax].name_deliver).latitude
                longitudej = UserProfileInfo.objects.get(user_id=orders[jmax].name_deliver).longitude

                for i in range(0, len(ordersConsidered) - 1):
                    if (ordersConsidered[i] is not None):
                        if (sumAmount + orders[i].amount < Truck.objects.get(id_truck=claster).capacity):
                            sumAmount = sumAmount + orders[i].amount

                            latitudex = UserProfileInfo.objects.get(user_id=orders[i].name_deliver).latitude
                            longitudex = UserProfileInfo.objects.get(user_id=orders[i].name_deliver).longitude

                            waypointi = 'geo!' + str(latitudei) + ',' + str(longitudei)
                            waypointj = 'geo!' + str(latitudej) + ',' + str(longitudej)
                            waypointx = 'geo!' + str(latitudex) + ',' + str(longitudex)

                            messageix = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                                     {'app_id': 'Z7uukAiQbHvHZ43KIBKW',
                                                      'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                                      'waypoint0': waypointi, 'waypoint1': waypointx,
                                                      'mode': 'fastest;car;traffic:disabled'})

                            messagejx = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                                     {'app_id': 'Z7uukAiQbHvHZ43KIBKW',
                                                      'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                                      'waypoint0': waypointj, 'waypoint1': waypointx,
                                                      'mode': 'fastest;car;traffic:disabled'})

                            dataix = messageix.json()
                            datajx = messagejx.json()

                            distanceix = dataix['response']['route'][0]['summary']['distance']
                            distancejx = dataix['response']['route'][0]['summary']['distance']
                            if (distanceix > distancejx):
                                route.index(0,orders[i].id)
                            else:
                                route.append(orders[i].id)
                            deleteAllFromIndex(tab, i)
                            ordersConsidered[i] = None
                print(route)
                allRoutes.append(route)
                #Route.objects.create(products_list=str(route), date=date, id_truck=Truck.objects.get(id_truck=claster))

            else:
                for i in range(0, len(ordersConsidered)):
                    if (ordersConsidered[i] is not None):
                        route = [orders[i].id]
                        #Route.objects.create(products_list=str(route), date=date, id_truck=Truck.objects.get(id_truck=claster))
                        print(route)
                        allRoutes.append(route)
                        ordersConsidered[i] = None
                        break
            print(allRoutes)
        MatchClients(date,claster,allRoutes)


def MatchClients(date, claster,routes):
    client_date = datetime.strptime(date, "%Y-%m-%d").date()-timedelta(days=1)
    clients_checkouts=Checkout.objects.filter(date=client_date) #tu teź claster
    clients_checkouts = clients_checkouts[::1]
    print(clients_checkouts)
    tab = [None] * len(routes)
    for x in range(len(routes)):
        tab[x] = [None] * len(clients_checkouts)
    for r in range(len(routes)):
        min=Magazine.objects.get(id_magazine=1).radius*1000*2
        client=None
        index=None
        latituder = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=routes[r][0]).name_deliver.id).latitude
        longituder = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=routes[r][0]).name_deliver.id).longitude
        waypointr = 'geo!' + str(latituder) + ',' + str(longituder)
        for c in range(len(clients_checkouts)):
            if(clients_checkouts[c] is not None):
                latitudet = UserProfileInfo.objects.get(user_id=clients_checkouts[c].name_client.id).latitude
                longitudet = UserProfileInfo.objects.get(user_id=clients_checkouts[c].name_client.id).longitude
                waypointt = 'geo!' + str(latitudet) + ',' + str(longitudet)

                messagert = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                         {'app_id': 'Z7uukAiQbHvHZ43KIBKW',
                                          'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                          'waypoint0': waypointr, 'waypoint1': waypointr,
                                          'mode': 'fastest;car;traffic:disabled'})

                datart = messagert.json()

                distancert = datart['response']['route'][0]['summary']['distance']
                if(distancert<min):
                    min=distancert
                    client=clients_checkouts[c]
                    index=c
        if(client is None):
            print(routes[r])
            Route.objects.create(products_list=str(routes[r]), date=date, id_truck=Truck.objects.get(id_truck=claster))
        else:
            clients_checkouts[index]=None
            routes[r].reverse()
            routes[r].append(client.id)
            routes[r].reverse()
            #routes[r].index(0,client.id)
            print(routes[r])
            Route.objects.create(products_list=str(routes[r]), date=date, id_truck=Truck.objects.get(id_truck=claster),client=True)
    for i in range (0, len(clients_checkouts)):
        if(clients_checkouts[i] is not None):
            route=[clients_checkouts[i].id]
            print(route)
            Route.objects.create(products_list=str(route), date=date, id_truck=Truck.objects.get(id_truck=claster),client=True)







#MatchClients('2018-12-20',2,[[63, 67, 62], [69, 70, 68], [71]])


