from datetime import timedelta, date
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
from accounts.models import UserProfileInfo
from datetime import datetime
import requests



"""

A view for displaying a form and rendering a template response.

"""
@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class Manual(TemplateView):
    template_name = 'admin_app/manual.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['truck'] = Truck.objects.all()
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['date_ordered'] = date.today() + timedelta(2)
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView(TemplateView):
    template_name = 'admin_app/admin_app_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())
        context['date_ordered'] = date.today() + timedelta(1)

        # później do obcięcia ten minus
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView1(TemplateView):
    template_name = 'admin_app/admin_app_index_1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(1)

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView2(TemplateView):
    template_name = 'admin_app/admin_app_index_2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(1)

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView3(TemplateView):
    template_name = 'admin_app/admin_app_index_3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_today'] = Route.objects.filter(
            date=date.today())  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(1)

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView20(TemplateView):
    template_name = 'admin_app/admin_app_index_20.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))
        context['date_ordered'] = date.today() + timedelta(2)
        # później do obcięcia ten minus
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView21(TemplateView):
    template_name = 'admin_app/admin_app_index_21.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(2)

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView22(TemplateView):
    template_name = 'admin_app/admin_app_index_22.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(2)

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(staff_member_required(), name='dispatch')
class IndexView23(TemplateView):
    template_name = 'admin_app/admin_app_index_23.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "admin_app"
        context['magazine'] = 'geo!' + str(Magazine.objects.get(id_magazine=1).latitude) + ',' + str(
            Magazine.objects.get(id_magazine=1).longitude)
        context['checkout'] = Checkout.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['ordered_products'] = OrderedProducts.objects.all()
        context['profile'] = UserProfileInfo.objects.all()
        context['routes_tomorrow'] = Route.objects.filter(
            date=date.today() + timedelta(1))  # później do obcięcia ten minus
        context['date_ordered'] = date.today() + timedelta(2)

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


@csrf_exempt
def areAllConsidered(tab):
    for i in range(0, len(tab)):
        if (tab[i] is not None):
            return False
    return True


@csrf_exempt
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


@csrf_exempt
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


@csrf_exempt
def wasCondidered(orders, ordersConsidered):
    for i in range(0, len(orders)):
        for j in range(0, len(ordersConsidered)):
            if orders[i] == ordersConsidered[j]:
                return True
    return False


@csrf_exempt
def maxFromI(tab, i):
    max = 0
    jmax = None
    for j in range(0, len(tab)):
        if tab[i][j] > max:
            max = tab[i][j]
            jmax = j
    return j


@csrf_exempt
def maxFromJ(tab, j):
    max = 0
    imax = None
    for i in range(0, len(tab)):
        if tab[i][j] > max:
            max = tab[i][j]
            imax = i
    return i


@csrf_exempt
def deleteAllFromIndex(tab, index):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if (i == index or j == index):
                tab[i][j] = None


@csrf_exempt
def ClarkeWright(date, claster):
    ordersOryg = None
    orders = []

    for c in Checkout.objects.all():
        if str(c.date) == date:
            if ordersOryg is None:
                ordersOryg = OrderedProducts.objects.filter(id_checkout=c)  # tu trzeba przefiltrować jeszcze z clastrem
            else:
                ordersOryg = ordersOryg | OrderedProducts.objects.filter(id_checkout=c)  # i tu

    if (ordersOryg is not None):
        print(ordersOryg)
        for o in ordersOryg:
            if (UserProfileInfo.objects.get(user=o.name_deliver).id_cluster.id_truck == claster and o.route == False):
                o.route = True
                o.save()
                orders.append(o)
        print(orders)
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
                                route.index(0, orders[i].id)
                            else:
                                route.append(orders[i].id)
                            deleteAllFromIndex(tab, i)
                            ordersConsidered[i] = None
                print(route)
                allRoutes.append(route)
                # Route.objects.create(products_list=str(route), date=date, id_truck=Truck.objects.get(id_truck=claster))

            else:
                for i in range(0, len(ordersConsidered)):
                    if (ordersConsidered[i] is not None):
                        route = [orders[i].id]
                        # Route.objects.create(products_list=str(route), date=date, id_truck=Truck.objects.get(id_truck=claster))
                        print(route)
                        allRoutes.append(route)
                        ordersConsidered[i] = None
                        break
            print(allRoutes)
        MatchClients(date, claster, allRoutes)
        addHour(date)


@csrf_exempt
def MatchClients(date, claster, routes):
    client_date = datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=1)
    clients_checkouts_oryg = Checkout.objects.filter(date=client_date)  # tu teź claster
    clients_checkouts_oryg = clients_checkouts_oryg[::1]
    clients_checkouts = []
    print(clients_checkouts_oryg)
    for o in clients_checkouts_oryg:
        if UserProfileInfo.objects.get(user=o.name_client).id_cluster.id_truck == claster and o.route_client == False:
            o.route_client = True
            o.save()
            clients_checkouts.append(o)
    print(clients_checkouts)
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
            print(routes[r])
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
            print(routes[r])
            routes[r].append('m')
            routes[r].reverse()
            routes[r].append('m')
            routes[r].reverse()
            print(routes[r][1])
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
            print(route)
            route = Route.objects.create(products_list=str(route), date=client_date,
                                         id_truck=Truck.objects.get(id_truck=claster),
                                         client=True, colour='#273244', hour=int(Checkout.objects.get(id=routes[r][1])))
            route.save()
            for i in range(2, len(routes[r]) - 1):
                o = OrderedProducts.objects.get(id=routes[r][i])
                o.id_route = route.id_route
                o.save()


@csrf_exempt
def runClarkeWright(request):
    date = datetime.today() + timedelta(2)  # moje testowe dane są na 20.12.2018 dlatego tak to robię
    date = str(date.strftime('%Y-%m-%d'))
    for t in Truck.objects.all():
        ClarkeWright(date, t.id_truck)
    return HttpResponse()


def addHour(date):  # to trzeba jeszcze przetestować, bo coś nie pykło
    routes = []
    for t in Truck.objects.all():
        routes = Route.objects.filter(date=date, id_truck=t, hour=0)
        for r in routes:
            for h in range(1, 6):
                hours = Route.objects.filter(date=(datetime.strptime(date, "%Y-%m-%d").date() + timedelta(days=1)),
                                             hour=h, id_truck=t)
                if (len(hours) == 0):
                    r.hour = h
                    r.save()
                    break

# MatchClients('2018-12-20',2,[[63, 67, 62], [69, 70, 68], [71]])
