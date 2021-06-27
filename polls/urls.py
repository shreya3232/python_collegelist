from django.urls import path
from .views import college_list

urlpatterns = [
    path('college/', college_list),

]
