import os
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Locator, UserProfile, Review
import requests
from .forms import UserProfileForm, LocatorForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json


def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



@login_required
def locator(request):
  api_key = os.environ['API_KEY']
  useraddress = requests.get(f'https://api.tomtom.com/search/2/geocode/query.json?key={api_key}')
  if request.method == 'POST':
    query = request.POST['query-address']
    useraddress = requests.get(f'https://api.tomtom.com/search/2/geocode/{query}.json?key={api_key}')
  address = useraddress.json()
  lat = address['results'][0]['position']['lat']
  lon = address['results'][0]['position']['lon']
  response = requests.get(f"https://api.tomtom.com/search/2/nearbySearch/.json?lat={lat}&lon={lon}&radius=10000&categorySet=9361059&view=Unified&relatedPois=off&key={ api_key }")
  location = response.json()['results']
  return render(request, 'locations/locator.html', {'location': location, 'lat' : lat })



@login_required
def locator_detail(request, shop_id):
  try:
    shop = Locator.objects.get(shopId=shop_id)
    review_form = ReviewForm()
    return render(request,'locations/detail.html', { 'shop': shop, 'review_form': review_form })
  except Locator.DoesNotExist:
    form = LocatorForm(request.POST)
    if form.is_valid():
      shop = form.save(commit=False)
      shop.save()
    review_form = ReviewForm()
    return render(request,'locations/detail.html', { 'shop': shop, 'review_form': review_form })



@login_required
def add_review(request, shop_id):
  shop = Locator.objects.get(shopId=shop_id)
  print(request.POST)
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.locator_id = shop.id
    new_review.user_id = request.user.id
    new_review.save()    
  return redirect('detail', shop_id=shop_id)



class ReviewUpdate(UpdateView, LoginRequiredMixin):
  model = Review
  fields = ['review']

class ReviewDelete(DeleteView, LoginRequiredMixin):
   model = Review
   success_url = '/'
  