import os
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import requests
from .forms import UserProfileForm
import json

# Create your views here
def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserProfileForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserProfileForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def locator(request):
  api_key = os.environ['API_KEY']
  response = requests.get(f"https://api.tomtom.com/search/2/nearbySearch/.json?lat=37.337&lon=-121.89&radius=10000&categorySet=9361059&view=Unified&relatedPois=off&key={ api_key }")
  location = response.json()['results']
  lon = response.json()['summary']['geoBias']['lon']
  lat = response.json()['summary']['geoBias']['lat']
  return render(request, 'locator.html', {'location': location, 'lon': lon, 'lat': lat})
