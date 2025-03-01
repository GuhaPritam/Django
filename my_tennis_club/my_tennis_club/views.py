from django.http import HttpResponse

def home(request):
    return HttpResponse("Hellow, HOME page")

def about(request):
    return HttpResponse("Hellow, ABOUT page")

def contact(request):
    return HttpResponse("Hellow, CONTACT page")