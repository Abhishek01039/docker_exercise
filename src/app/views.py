from django.shortcuts import render
from django.http import HttpResponse
from .models import person
from . import forms
from .forms import detail
from django.views.generic import View,TemplateView,ListView,DetailView
# Create your views here.
# This is a class based view 
# class CBV(View):
#     def get(self,request):
#         return render(request,'index.html')

# this is a template based view
class indexView(TemplateView):
    template_name="index.html"
    

def form_Data(request):
    dat=detail()
    if request.method=='POST':
        dat1=detail(request.POST) 
        if dat1.is_valid():
            dat1.save()
            return HttpResponse("Submitted")
        else:
            return render(request,'app/form.html',{'dat':dat1})        
    return render(request,'app/form.html',{'dat':dat})