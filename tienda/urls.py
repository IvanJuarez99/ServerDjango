


from django.urls import path
from tienda.views import productos

urlpatterns = [
    path ("productos", productos),

]