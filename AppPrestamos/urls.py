from django.urls import path
from . import views

app_name = "AppPrestamos"


urlpatterns = [
    path("index/", views.index, name="index"),
    # path("login", views.login_request, name="Login"),
    # path("registro", views.registro, name="Registro"),
    # path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
]
