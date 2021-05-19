from django.urls import path, include

from . import views

app_name = 'nest'

urlpatterns = [
    path('nest/', views.NestedAmountsView.as_view(), name='nest'),
]
