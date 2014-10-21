from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

# Create your views here.
def home(request):
    return render_to_response('gappscmu/home.html',
            {}, RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect('/')
