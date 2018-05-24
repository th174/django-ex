import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def hello_world(request):
    return HttpResponse("""
                        <h1>Hello World again!</h1>
                        <p>This application is hosted on Openshift</p>
                        <p>This application is configured with a webhook to rebuild whenever the code changes on master.</p>
                        """)
