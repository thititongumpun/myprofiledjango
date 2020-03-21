from django.shortcuts import render
from .models import experience, sample

# Create your views here.
def home(request):
	return render(request, 'base.html')

def about(request):
	exp_obj = experience.objects.all()
	return render(request, 'about.html', {'context': exp_obj})


def sampleofwork(request):
	sample_obj = sample.objects.all()
	return render(request, 'sampleofwork.html', {'context2': sample_obj})