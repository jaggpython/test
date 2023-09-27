from django.contrib import admin  
from django.urls import path  
from studentdetails import views  

urlpatterns = [  
    path('student', views.student),  
    path('show',views.show),  
    # path('edit/<int:id>', views.edit),  
    # path('update/<int:id>', views.update),  
    # path('delete/<int:id>', views.destroy),  
]  