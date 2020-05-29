from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.contrib import messages
from home.models import Contact
from home.forms import ContactForm

# Create your views here.
# home page function
def index(request):
    # return HttpResponse('Home Page')
    # passing data 
    context = {'name': 'Rahul Gupta'}
    return render(request,'index.html', context)
# about page function
def about(request):
    return render(request,'pages/about.html')
# contact page function
def contact(request):
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            name        =   request.POST.get('name')
            subject     =   request.POST.get('subject')
            email       =   request.POST.get('email')
            message     =   request.POST.get('message')
            # create object
            contactObject   = Contact(name=name, subject=subject, email=email, message=message, created_at=datetime.now())
            # save the contact
            contactObject.save()
            messages.success(request, 'Thanks for contacting us.') 
    else:  
        form = ContactForm()  
    return render(request,'pages/contact.html',{'form':form, 'request':request}) 