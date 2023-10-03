from django.contrib import admin
from noticia import models
"""from .models import Autor"""

# Register your models here.
from django.contrib import admin
from .models import Autor

# Register your models here.

admin.site.register(Autor)