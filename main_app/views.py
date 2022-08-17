import os
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Locator
import requests
from .forms import UserProfileForm
import json

# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def locator(request):
  api_key = os.environ['API_KEY']
  useraddress = requests.get(f'https://api.tomtom.com/search/2/geocode/query.json?key={api_key}')
  if request.method == 'POST':
    query = request.POST['query-address']
    useraddress = requests.get(f'https://api.tomtom.com/search/2/geocode/{query}.json?key={api_key}')
  address = useraddress.json()
  print(address['results'][0]['position']['lat'])
  lat = address['results'][0]['position']['lat']
  lon = address['results'][0]['position']['lon']
  response = requests.get(f"https://api.tomtom.com/search/2/nearbySearch/.json?lat={lat}&lon={lon}&radius=10000&categorySet=9361059&view=Unified&relatedPois=off&key={ api_key }")
  location = response.json()['results']
  for user in location:
    locator = Locator(name=user['poi']['name'], address=user['address']['streetNumber'], location=user['address']['countrySubdivision'], hours=user['address']['streetNumber'], website=user['poi']['phone'], phone=user['poi']['phone'])
  locator.save()
  all_locations = Locator.objects.all()
  print(request.POST)
  return render(request, 'locator.html', {'location': location, 'lat' : lat, 'all_locations': all_locations })

