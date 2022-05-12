from time import strftime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.utils import timezone
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Client, Photo, Trip, Purchase, Payment


def index(request):
    #request.session['destination'] = request.POST['destination']
    #request.session['origin'] = request.POST['origin']
    # latest_question_list = Questao.objects.all()
    return render(request, 'space_trip/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        planetionality = request.POST['planetionality']
        u = User.objects.create_user(username, password=password, email=email)
        c = Client(user=u, firstname=firstname, surname=surname, birthday=birthday, gender=gender, planetionality=planetionality)
        c.save()
        user = authenticate(username=username, password=password)
        return render(request, 'space_trip/login.html')
    else:
        return render(request, 'space_trip/register.html')


def user_login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('space_trip:index'))

        else:
            return render(request, 'space_trip/register.html')
    except MultiValueDictKeyError:
        return render(request, 'space_trip/login.html')


def profile(request):
    try:
        uploaded_file_url = request.user.photo.photo_url
        return render(request, 'space_trip/profile.html', {'uploaded_file_url': uploaded_file_url})
    except ObjectDoesNotExist:
        return render(request, 'space_trip/profile.html')

def editProfile(request):
    try:
        uploaded_file_url = request.user.photo.photo_url
        return render(request, 'space_trip/edit-profile.html', {'uploaded_file_url': uploaded_file_url})
    except ObjectDoesNotExist:
        return render(request, 'space_trip/edit-profile.html')

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('space_trip:index'))

@login_required(login_url='space_trip/register.html')
def uploadPhoto(request):
    if request.method == 'POST' and request.FILES.get('myfile') is not None:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        u = request.user
        try:
            photo = Photo.objects.get(user=u)
            photo.photo_url = uploaded_file_url
        except Photo.DoesNotExist:
            photo = Photo(user=u, photo_url=uploaded_file_url)
        photo.save()
        return render(request, 'space_trip/profile.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'space_trip/profile.html')

def destinations(request):
    return render(request, 'space_trip/destinations.html')

def moon(request):
    return render(request, 'space_trip/moon.html')

def mercury(request):
    return render(request, 'space_trip/mercury.html')

def venus(request):
    return render(request, 'space_trip/venus.html')

def earth(request):
    return render(request, 'space_trip/earth.html')

def mars(request):
    return render(request, 'space_trip/mars.html')

def jupiter(request):
    return render(request, 'space_trip/jupiter.html')

def saturn(request):
    return render(request, 'space_trip/saturn.html')

def uranus(request):
    return render(request, 'space_trip/uranus.html')

def neptune(request):
    return render(request, 'space_trip/neptune.html')

def gallery(request):
    return render(request, 'space_trip/gallery.html')

def promotions(request):
    return render(request, 'space_trip/promotions.html')

def tripManagement(request):
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_superuser:
        destination = request.POST['destination']
        origin = request.POST['origin']
        departure_date = request.POST['departure_date']
        return_date = request.POST['return_date']
        price = request.POST['price']
        spaceship = request.POST['spaceship']
        available_seats = request.POST['available_seats']
        trip = Trip(origin=origin, destination=destination, departure_date=departure_date, return_date=return_date, price=price, spaceship=spaceship, available_seats=available_seats)
        trip.save()
        return HttpResponseRedirect(reverse('space_trip:trip-list'))
    else:
        return render(request, 'space_trip/trip-management.html')

def catchDataFromIndex(request):
    if request.POST.get('destination') is not None and request.POST.get('origin') is not None:
        destination = request.POST['destination']
        origin = request.POST['origin']
        return render(request, 'space_trip/plan-trip.html', {'destination':destination,'origin':origin})
    return render(request, 'space_trip/index.html')

def planTrip(request):
    trips = Trip.objects.filter(origin=request.POST['origin'], destination=request.POST['destination'], departure_date=request.POST['departure_date'], return_date=request.POST['return_date'])
    if trips.count() > 0:
        origin = request.POST['origin']
        destination = request.POST['destination']
        departure_date = request.POST['departure_date']
        return_date = request.POST['return_date']
        return render(request, 'space_trip/available-trips.html', {'destination': destination, 'origin': origin, 'departure_date': departure_date, 'return_date': return_date})
    else:
        messages.error(request, 'Não existem viagens com estes atributos.')
        return render(request, 'space_trip/plan-trip.html')

def editUserData(request):
    user = request.user
    user.email = request.POST['email']
    user.save()
    user.client.save()
    return render(request, 'space_trip/profile.html')

def payment(request):
    return render(request, 'space_trip/payment.html')


def payment(request):
    return render(request, 'space_trip/payment.html')

def aboutUs(request):
    return render(request, 'space_trip/about-us.html')

def tripList(request):
    trip_list = Trip.objects.all()
    return render(request, 'space_trip/trip-list.html', {'trip_list': trip_list})

def userList(request):
    user_list = User.objects.all()
    return render(request, 'space_trip/client-management.html', {'user_list': user_list})

@permission_required('space_trip.trip-management', login_url=reverse_lazy('space_trip:login'))
def deleteTrip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.delete()
    return HttpResponseRedirect(reverse('space_trip:trip-list'))

@permission_required('space_trip.register', login_url=reverse_lazy('space_trip:login'))
def deleteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return HttpResponseRedirect(reverse('space_trip:client-management'))

def availableTrips(request):
    #number_of_passengers = int(request.POST.get('number_of_passengers'))
    if request.POST.get('destination') is not None and request.POST.get('origin') is not None and request.POST.get('departure_date') is not None and request.POST.get('return_date'):
            #and (number_of_passengers <= 60):
        destination = request.POST.get('destination')
        origin = request.POST.get('origin')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        trips = Trip.objects.filter(origin=origin, destination=destination, departure_date=departure_date, return_date=return_date)
        return render(request, 'space_trip/available-trips.html', {'trips': trips})
    else:
        messages.error(request, 'Não existem viagens disponíveis para os critérios selecionados')
        return render(request, 'space_trip/plan-trip.html')
    return render(request, 'space_trip/available-trips.html')

def purchase(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    try:
        selected_trip = Trip.objects.get(pk=request.POST['trip'])
    except (KeyError, Trip.DoesNotExist):
        return render(request, 'space_trip/available-trips.html', {'trip': trip, 'error_message': 'Não foi selecionada nenhuma viagem.'})
    else:
        selected_trip.available_seats -= selected_trip.number_of_passengers
        total_price = selected_trip.price * selected_trip.number_of_passengers
        user = request.user
        p = Purchase(selected_trip, user, total_price)
        p.save()
        return HttpResponseRedirect(reverse('space_trip:tripPurchaseSuccessful', args=(trip.id,)))

def tripPurchaseSuccessful(request):
    messages.success(request, 'Viagem comprada com sucesso!')
    return render(request, 'space_trip/trip-purchase-successful.html')
