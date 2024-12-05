from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required 
def index(request):
    return render(request, 'autenthic_app/index.html')

def home(request):
    return render(request, 'autenthic_app/home.html')