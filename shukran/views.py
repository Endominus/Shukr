from django.shortcuts import render

from adal import AuthenticationContext

# Create your views here.
def index(request):
    return render(request, 'shukran/index.html')