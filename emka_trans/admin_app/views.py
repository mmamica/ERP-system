from datetime import timedelta, date

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from order_app.models import Checkout, OrderedProducts
from products_app.models import Product
from admin_app.models import Magazine, Route
from admin_app.models import Truck
from accounts.models import UserProfileInfo, User
from datetime import datetime
import requests
import re


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView(TemplateView):
    """

     Allows the admin to see all the checkouts and routes for today.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_today``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index.html`

    """
    template_name = 'admin_app/admin_app_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())
        context['date_ordered'] = date.today() + timedelta(1)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView1(TemplateView):
    """

     Allows the admin to see the checkouts and routes for the first slot for today.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_today``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_1.html`

    """
    template_name = 'admin_app/admin_app_index_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(1)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView2(TemplateView):
    """

     Allows the admin to see the checkouts and routes for the second slot for today.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_today``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_2.html`

    """
    template_name = 'admin_app/admin_app_index_2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(1)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView3(TemplateView):
    """

     Allows the admin to see the checkouts and routes for the third slot for today.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_today``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_3.html`

    """
    template_name = 'admin_app/admin_app_index_3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(1)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView20(TemplateView):
    """

     Allows the admin to see all the checkouts and routes for for tomorrow.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_tomorrow``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_20.html`

    """
    template_name = 'admin_app/admin_app_index_20.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))
        context['date_ordered'] = date.today() + timedelta(2)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView21(TemplateView):
    """

     Allows the admin to see the checkouts and routes for the first slot for tomorrow.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_tomorrow``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_21.html`

    """
    template_name = 'admin_app/admin_app_index_21.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(2)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView22(TemplateView):
    """

     Allows the admin to see the checkouts and routes for the second slot for tomorrow.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_tomorrow``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_22.html`

    """
    template_name = 'admin_app/admin_app_index_22.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(2)
        context['trucks'] = Truck.objects.all()


        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView23(TemplateView):
    """

     Allows the admin to see the checkouts and routes for the third slot for tomorrow.

        **Context**
            ``magazine``
                A String with Here maps request with magazine coordinates.
            ``checkout``
                Instances of :model:`order_app.Checkout`
            ``ordered_products``
                Instances of :model:`order_app.OrderedProducts`
            ``profile``
                Instances of :model:`accounts.UserProfileInfo`
            ``routes_tomorrow``
                Instances of :model:`admin_app.Route`
            ``date_ordered``
                A date equal to a date after tomorrow. (taking a server date)
            ``trucks``
                Instances of :model:`admin_app.Truck`
        **Template:**
            :template:`admin_app/admin_app_index_23.html`

    """
    template_name = 'admin_app/admin_app_index_23.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(2)
        context['trucks'] = Truck.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class AdminCheckoutListView(ListView):
    """
     Allows the admin to see the list of the checkout details.

        **Template:**
            :template:`admin_app/order_list.html`
    """
    model = Checkout
    template_name = 'admin_app/order_list.html'

    def get_queryset(self):
        return Checkout.objects.filter(confirmed=True)


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class AdminCheckoutDetailView(DetailView):
    """
     Allows the admin to see the checkout details.

        **Template:**
            :template:`admin_app/order_detail.html`
    """
    context_object_name = 'order_details'
    model = Checkout
    template_name = 'admin_app/order_detail.html'
    # un_success_url = reverse_lazy("admin_app:order_list")


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class AdminProductListView(ListView):
    """
     Allows the admin to see the list of whole available products.

        **Template:**
            :template:`admin_app/product_list.html`
    """
    template_name = 'admin_app/product_list.html'
    model = Product


@csrf_exempt
def areAllConsidered(tab):
    """
    Checks if all elements in a list are None.
    :param tab: List
    :return: Boolean
    """
    for i in range(0, len(tab)):
        if (tab[i] is not None):
            return False
    return True


@csrf_exempt
def onNotConsidered(tab):
    """
    Checks if there is only one not None value in a list.
    :param tab: List
    :return: Boolean
    """
    iter = 0
    for i in range(0, len(tab)):
        if (tab[i] is not None):
            iter = iter + 1
    if (iter == 1):
        return True
    return False



@csrf_exempt
def maxCell(tab):
    """
    Finds the cell with the biggest value
    :param tab: 2D-Array
    :return: Tuple
    """
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


@csrf_exempt
def maxFromI(tab, i):
    """
    Finds the index of the biggest value in the matrix from the row i.
    :param tab: 2D-Array
    :param i: integer
    :return: integer
    """
    max = 0
    jmax = None
    for j in range(0, len(tab)):
        if tab[i][j] > max:
            max = tab[i][j]
            jmax = j
    return j


@csrf_exempt
def maxFromJ(tab, j):
    """
    Finds the index of the biggest value in the matrix from the column j.
    :param tab: 2D-Array
    :param j: integer
    :return: integer
    """
    max = 0
    imax = None
    for i in range(0, len(tab)):
        if tab[i][j] > max:
            max = tab[i][j]
            imax = i
    return i


@csrf_exempt
def deleteAllFromIndex(tab, index):
    """
    Deletes all cells from a row number index anf from the column number index.
    :param tab: 2D-Array
    :param index: integer
    :return:
    """
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if (i == index or j == index):
                tab[i][j] = None


@csrf_exempt
def clarkeWright(date, claster):
    """
    For each cluster it finds optimized routes using Clarke and Wright algorithm.
    :param date: string (%Y-%m-%d)
    :param claster: integer
    :return:
    """
    ordersOryg = None
    orders = []
    for c in Checkout.objects.all():
        if str(c.date) == date:
            if ordersOryg is None:
                ordersOryg = OrderedProducts.objects.filter(id_checkout=c)
            else:
                ordersOryg = ordersOryg | OrderedProducts.objects.filter(id_checkout=c)

    if (ordersOryg is not None):
        for o in ordersOryg:
            if (UserProfileInfo.objects.get(user=o.name_deliver).id_cluster.id_truck == claster and o.route == False):
                o.route = True
                o.save()
                orders.append(o)
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

                #if ((orders[i].amount + orders[j].amount) > Truck.objects.get(id_truck=claster).capacity):
                    #tab[i][j] = None;
                #else:
                tab[i][j] = saving

        allRoutes = []
        while (not areAllConsidered(ordersConsidered)):
            if (not onNotConsidered(ordersConsidered)):
                print(tab)
                sumAmount = 0
                imax = maxCell(tab)[0]
                jmax = maxCell(tab)[1]
                print(imax)
                print(jmax)
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
                                route.index(0, orders[i].id)
                            else:
                                route.append(orders[i].id)
                            deleteAllFromIndex(tab, i)
                            ordersConsidered[i] = None
                allRoutes.append(route)
            else:
                for i in range(0, len(ordersConsidered)):
                    if (ordersConsidered[i] is not None):
                        route = [orders[i].id]
                        allRoutes.append(route)
                        ordersConsidered[i] = None
                        break
        matchClients(date, claster, allRoutes)
        addHour(date)
        calculateHour(date)
        sendMail(date)


@csrf_exempt
def matchClients(date, claster, routes):
    """
    Matches routes with the date given as an attribute to the checkouts.
    :param date: string (%Y-%m-%d)
    :param claster: integer
    :param routes: List
    :return:
    """
    client_date = datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=1)
    clients_checkouts_oryg = Checkout.objects.filter(date=client_date)  # tu teź claster
    clients_checkouts_oryg = clients_checkouts_oryg[::1]
    clients_checkouts = []
    for o in clients_checkouts_oryg:
        if UserProfileInfo.objects.get(user=o.name_client).id_cluster.id_truck == claster and o.route_client == False:
            o.route_client = True
            o.save()
            clients_checkouts.append(o)
    tab = [None] * len(routes)
    for x in range(len(routes)):
        tab[x] = [None] * len(clients_checkouts)
    for r in range(len(routes)):
        min = Magazine.objects.get(id_magazine=1).radius * 1000 * 2
        client = None
        index = None
        latituder = UserProfileInfo.objects.get(
            user_id=OrderedProducts.objects.get(id=routes[r][0]).name_deliver.id).latitude
        longituder = UserProfileInfo.objects.get(
            user_id=OrderedProducts.objects.get(id=routes[r][0]).name_deliver.id).longitude
        waypointr = 'geo!' + str(latituder) + ',' + str(longituder)
        for c in range(len(clients_checkouts)):
            if (clients_checkouts[c] is not None):
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
                if (distancert < min):
                    min = distancert
                    client = clients_checkouts[c]
                    index = c
        if (client is None):
            routes[r].append('m')
            routes[r].reverse()
            routes[r].append('m')
            routes[r].reverse()
            route = Route.objects.create(products_list=str(routes[r]), date=client_date,
                                         id_truck=Truck.objects.get(id_truck=claster),
                                         colour='#87a8dd')
            route.save()
            for i in range(1, len(routes[r]) - 1):
                o = OrderedProducts.objects.get(id=routes[r][i])
                o.id_route = route.id_route
                o.save()

        else:
            clients_checkouts[index] = None
            routes[r].reverse()
            routes[r].append(client.id)
            routes[r].reverse()
            routes[r].append('m')
            routes[r].reverse()
            routes[r].append('m')
            routes[r].reverse()
            route = Route.objects.create(products_list=str(routes[r]), date=client_date,
                                         id_truck=Truck.objects.get(id_truck=claster),
                                         client=True, colour='#546b91',
                                         hour=int(Checkout.objects.get(id=routes[r][1]).hour))
            route.save()
            for i in range(2, len(routes[r]) - 1):
                o = OrderedProducts.objects.get(id=routes[r][i])
                o.id_route = route.id_route
                o.save()
    for i in range(0, len(clients_checkouts)):
        if (clients_checkouts[i] is not None):
            route = [clients_checkouts[i].id]
            routes[r].append('m')
            routes[r].reverse()
            routes[r].append('m')
            routes[r].reverse()
            route = Route.objects.create(products_list=str(route), date=client_date,
                                         id_truck=Truck.objects.get(id_truck=claster),
                                         client=True, colour='#273244', hour=int(Checkout.objects.get(id=routes[r][1]).hour))
            route.save()
            for i in range(2, len(routes[r]) - 1):
                o = OrderedProducts.objects.get(id=routes[r][i])
                o.id_route = route.id_route
                o.save()


@csrf_exempt
def runClarkeWright(request):
    """
    It runs a clarkeWright function for each cluster.
    :param request: HttpRequest
    :return: HttpResponse
    """
    date = datetime.today() + timedelta(2)  # moje testowe dane są na 20.12.2018 dlatego tak to robię
    date = str(date.strftime('%Y-%m-%d'))
    for t in Truck.objects.all():
        clarkeWright(date, t.id_truck)
    return HttpResponse()


@csrf_exempt
def addHour(date):
    """
    Adds an hour to automatically generated routes for the day given as an attribute of the function
    :param date: string (%Y-%m-%d)
    :return:
    """

    date = (datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=1))
    for t in Truck.objects.all():
        routes = Route.objects.filter(date=date, id_truck=t, hour=0)
        for r in routes:
            print(r)
            for h in range(1, 6):
                hours = Route.objects.filter(date=date,
                                             hour=h, id_truck=t)
                if (len(hours) == 0):
                    r.hour = h
                    r.save()
                    break


@csrf_exempt
def calculateHour(date):
    """
    Calculates the time route time. It adds the time needed to repack the truck.
    :param date: string (%Y-%m-%d)
    :return:
    """

    date = (datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=1))
    hours=0
    for r in Route.objects.filter(date=date):
        list=r.products_list.split(',')
        if(r.client):
            latitude1=str(Magazine.objects.get(id_magazine=1).latitude)
            longitude1=str(Magazine.objects.get(id_magazine=1).longitude)

            latitude2 = UserProfileInfo.objects.get(user_id=Checkout.objects.get(id=int(list[1])).name_client).latitude
            longitude2 = UserProfileInfo.objects.get(user_id=Checkout.objects.get(id=int(list[1])).name_client).longitude

            waypoint1 = 'geo!' + str(latitude1) + ',' + str(longitude1)
            waypoint2 = 'geo!' + str(latitude2) + ',' + str(longitude2)

            message = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                    {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                     'waypoint0': waypoint1, 'waypoint1': waypoint2,
                                     'mode': 'fastest;car;traffic:disabled'})

            data = message.json()
            distance = data['response']['route'][0]['summary']['distance']
            hour=distance/60000
        else:
            latitude1=str(Magazine.objects.get(id_magazine=1).latitude)
            longitude1=str(Magazine.objects.get(id_magazine=1).longitude)

            latitude2 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[1])).name_deliver).latitude
            longitude2 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[1])).name_deliver).longitude

            waypoint1 = 'geo!' + str(latitude1) + ',' + str(longitude1)
            waypoint2 = 'geo!' + str(latitude2) + ',' + str(longitude2)

            message = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                    {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                     'waypoint0': waypoint1, 'waypoint1': waypoint2,
                                     'mode': 'fastest;car;traffic:disabled'})

            data = message.json()
            distance = data['response']['route'][0]['summary']['distance']
            hour=distance/60000


        for i in range(2,len(list)-3):
            latitude1 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[i])).name_deliver).latitude
            longitude1 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[i])).name_deliver).longitude

            latitude2 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[i+1])).name_deliver).latitude
            longitude2 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[i+1])).name_deliver).longitude

            waypoint1 = 'geo!' + str(latitude1) + ',' + str(longitude1)
            waypoint2 = 'geo!' + str(latitude2) + ',' + str(longitude2)

            message = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                                    {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                     'waypoint0': waypoint1, 'waypoint1': waypoint2,
                                     'mode': 'fastest;car;traffic:disabled'})

            data = message.json()
            distance = data['response']['route'][0]['summary']['distance']
            hour=hour+distance/60000

        latitude1 = str(Magazine.objects.get(id_magazine=1).latitude)
        longitude1 = str(Magazine.objects.get(id_magazine=1).longitude)

        latitude2 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[len(list)-2])).name_deliver).latitude
        longitude2 = UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[len(list)-2])).name_deliver).longitude

        waypoint1 = 'geo!' + str(latitude1) + ',' + str(longitude1)
        waypoint2 = 'geo!' + str(latitude2) + ',' + str(longitude2)

        message = requests.get('https://route.api.here.com/routing/7.2/calculateroute.json',
                               {'app_id': 'Z7uukAiQbHvHZ43KIBKW', 'app_code': 'nadFSh5EHBHkTdUQ3YnTEg',
                                'waypoint0': waypoint1, 'waypoint1': waypoint2,
                                'mode': 'fastest;car;traffic:disabled'})

        data = message.json()
        distance = data['response']['route'][0]['summary']['distance']
        hour = hour + distance / 60000
        hour = hour + (len(list)-2)*0.1
        hour = round(hour,2)
        r.time=hour
        r.save()



@csrf_exempt
def sendMail(date):
    """
    Sends mails to clients and suppliers about the delivery or pickup date and hour after generating routes.
    :param date: string (%Y-%m-%d)
    :return:
    """

    date = (datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=1))
    mails=set()
    for r in Route.objects.filter(date=date):
        list=r.products_list.split(',')
        if(r.client):
            mail=UserProfileInfo.objects.get(user_id=Checkout.objects.get(id=int(list[1])).name_client).user.email
            username = UserProfileInfo.objects.get(user_id=Checkout.objects.get(id=int(list[1])).name_client).company_name
            email = mail
            date = r.date
            hour = r.hour
            if(hour==1):
                hour="10:00"
            elif(hour==2):
                hour="13:00"
            else:
                hour="16:00"
            subject, from_email, to = 'Subject', 'pacman.package.sender@gmail.com', email
            html_content = render_to_string('admin_app/mail.html',
                                            {'user': username, 'email': email, 'date': date, 'hour': hour})  # render with dynamic value
            text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            #msg.send() #commented not to send an email while checking test data

        else:
            mail=UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[1])).name_deliver).user.email
            mails.add(mail)

        for i in range(2,len(list)-2):
            mail=UserProfileInfo.objects.get(user_id=OrderedProducts.objects.get(id=int(list[i])).name_deliver).user.email
            mails.add(mail)

        for m in mails:
            email = m
            date = r.date
            hour = r.hour
            if(hour==1):
                hour="10:00"
            elif(hour==2):
                hour="13:00"
            else:
                hour="16:00"
            subject, from_email, to = 'Subject', 'pacman.package.sender@gmail.com', email
            html_content = render_to_string('admin_app/mail_deliver.html',
                                            {'email': email, 'date': date, 'hour': hour})  # render with dynamic value
            text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            #msg.send() #commented not to send an email while checking test data



@csrf_exempt
def runUpdate(request):
    """
    Updates the route if it was manually edited.
    :param request: HttpRequest
    :return: HttpResponse
    """
    body_unicode = request.body.decode('utf-8')
    pattern = r'array=(.*)&id=(\d*)&array2=(.*)&id2=(\d*)'
    print(body_unicode)
    r = re.compile(pattern)
    m = r.match(body_unicode)
    array = m.group(1)
    id = m.group(2)
    array2=m.group(3)
    id2=m.group(4)
    print(body_unicode)
    if(array!=''):
        list = array.split('%2C')
        if (Route.objects.get(id_route=id).client):
            route = Route.objects.get(id_route=id).products_list.split(',')
            client=int(route[1])
            list.insert(0,client)

        for x in range(len(list)):
            list[x]=int(list[x])

        list.insert(0,'m')
        list.append('m')
        r=Route.objects.get(id_route=id)
        r.products_list=list
        r.save()
    elif(array2!=''):
        list = array2.split('%2C')
        if (Route.objects.get(id_route=id2).client):
            route = Route.objects.get(id_route=id2).products_list.split(',')
            client = int(route[1])
            list.insert(0, client)

        for x in range(len(list)):
            list[x] = int(list[x])

        list.insert(0, 'm')
        list.append('m')
        r = Route.objects.get(id_route=id2)
        r.products_list = list
        r.save()
    date2=date.today()+timedelta(2)
    date2=str(date2)
    calculateHour(date2)
    return HttpResponse()