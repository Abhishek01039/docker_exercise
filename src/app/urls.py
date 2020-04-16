from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.indexView.as_view()),
    path('form/',views.form_Data)
]
