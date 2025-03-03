from django.shortcuts import render

def all_app(request):
    return render(request, 'app/app.html')