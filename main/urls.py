from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/register", views.UserRegisterApiView.as_view()),
    path("api/login", views.UserLogingApiView.as_view()),
    path("api/logout", views.UserLogOutView.as_view()),
    path("api/links", views.LinksApiView.as_view()),
    path("api/links/<int:id>", views.LinkApiView.as_view()),
    path("api/colors", views.ColorsApiView.as_view()),
    path("api/colors/<int:id>", views.ColorApiView.as_view()),
    path("api/products", views.ProductsApiView.as_view()),
    path("api/products/<int:id>", views.ProductApiView.as_view()),
    path("api/orders", views.OrderedItemsApiView.as_view()),
    path("api/orders/<int:id>", views.OrderedItemApiView.as_view())
]