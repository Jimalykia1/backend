from django.contrib import admin

from Store.models import product
from django.http import HttpResponse

admin.site.register(product)

def home(request):
    pass