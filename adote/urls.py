from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Se a pessoa acessar auth/ redireciona para o arquivo usuários. urls
    path('auth/', include('usuarios.urls')),

]
