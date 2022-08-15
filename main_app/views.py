from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import requests
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
  response = requests.get("https://api.tomtom.com/search/2/nearbySearch/.json?lat=37.337&lon=-121.89&radius=10000&categorySet=9361059&view=Unified&relatedPois=off&key=UldEI4VV32J6hKCoAPjuC0f2qbTAGiuJ")
  location = response.json()
  return render(request, 'locator.html', {'location': location})


