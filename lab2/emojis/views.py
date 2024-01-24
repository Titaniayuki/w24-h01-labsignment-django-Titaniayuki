from django.shortcuts import render # Import this shortcut function

def index(request):
    return render(request, "index.html")