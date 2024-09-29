
from django.urls import path
from . import views

urlpatterns = [
    path('',views.hire, name="hire"),
    path('check/',views.try_view, name="tryView"),
    path('professionals/',views.professional, name="professional"),
]