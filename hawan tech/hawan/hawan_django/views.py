from django.http import HttpResponse

def home(request):
    return HttpResponse("hello, world. you are at hawan tech")

def about(request):
    return("hello , world . you are in the about page")

def contact(request):
    return("hello , world. you are in the contact page ")