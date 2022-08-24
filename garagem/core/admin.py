from django.contrib import admin

from core.models import Marca
from core.models import Categoria
from core.models import Carro


admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Carro)
