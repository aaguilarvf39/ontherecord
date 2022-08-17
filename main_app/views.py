import os
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
  query = "1419 Westwood Blvd Los Angeles CA 90024-4911"
  useraddress = requests.get(f'https://api.tomtom.com/search/2/geocode/{query}.json?key={api_key}')
  address = useraddress.json()
  print(address['results'][0]['position']['lat'])
  lat = address['results'][0]['position']['lat']
  lon = address['results'][0]['position']['lon']
  response = requests.get(f"https://api.tomtom.com/search/2/nearbySearch/.json?lat={lat}&lon={lon}&radius=10000&categorySet=9361059&view=Unified&relatedPois=off&key={ api_key }")
  location = response.json()['results']
  print(location)
  return render(request, 'locator.html', {'location': location, 'lat' : lat })


def profile(request):
	
	up_form = UserProfileForm(instance=request.user.userprofile)
	result = "error"
	message = "Something went wrong. Please check and try again"

	if request.is_ajax() and request.method == "POST":
		up_form = UserProfileForm(data = request.POST, instance=request.user.userprofile)
		
		#if both forms are valid, do something
		if up_form.is_valid():
			user = up_form.save()

			up = request.user.userprofile
			up.has_profile = True
			up.save()

			result = "perfect"
			message = "Your profile has been updated"
			
		
	return render(request, 'profile.html')