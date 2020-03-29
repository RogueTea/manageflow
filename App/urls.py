from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("faq/", views.faqs, name="FAQs"),
    path("create/", views.create, name="create"),
    path("restricted/", views.restricted, name="restricted"),
]