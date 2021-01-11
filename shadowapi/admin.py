from django.contrib import admin
from . models import Register, Login, Data

# Register your models here.
admin.site.register((Register, Data))
