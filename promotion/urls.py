from django.urls import path
from .views import home, about, sampleofwork

urlpatterns = [
	path('', home, name='home-page'),
	path('about/', about, name='about-page'),
	path('sampleofwork/', sampleofwork, name='sampleofwork-page')
]