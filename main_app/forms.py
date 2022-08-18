from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review, UserProfile
from .models import Locator




class LocatorForm(forms.ModelForm):
	class Meta:
		model = Locator
		fields = ('shopId', 'name', 'freeformAddress', 'streetNumber', 'streetName', 'municipality', 'countrySubdivision', 'website', 'phone')

class UserProfileForm(forms.ModelForm):
	user_id = forms.CharField(max_length=500, required=True, widget = forms.HiddenInput())
	name = forms.CharField(max_length=500, required=True, widget = forms.HiddenInput())
	streetNumber = forms.CharField(max_length=1000, required=True, widget = forms.HiddenInput())
	streetName = forms.CharField(max_length=1000, required=True, widget = forms.HiddenInput())
	municipality = forms.CharField(max_length=1000, required=True, widget = forms.HiddenInput())
	countrySubdivision = forms.CharField(max_length=800, required=True, widget = forms.HiddenInput())
	website= forms.CharField(max_length=400, required=True, widget = forms.HiddenInput())
	phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': '*Telephone..'}))
	
	class Meta:
		model = UserProfile
		fields = ('user_id','name', 'streetNumber', 'streetNumber', 'streetName', 'municipality', 'countrySubdivision', 'website', 'phone')

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review']