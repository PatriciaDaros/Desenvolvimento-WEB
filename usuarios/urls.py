from django.urls import path
from . import views

urlpatterns = [
    # Quando eu acessar o cadastro/ vou acessar qual
    # função no arquivo views, e o=quando eu for me referir 
    # a essa função como vou chamar ela?
    path('cadastro/', views.cadastro, name="cadastro"),

]
