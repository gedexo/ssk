from django.urls import path

from . import views


app_name = "web"


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("products/", views.ProductListView.as_view(), name="products"),
    path("updates/", views.UpdatesView.as_view(), name="update"),
    path("update/<str:slug>/", views.UpadateDetailView.as_view(), name="update_detail"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]