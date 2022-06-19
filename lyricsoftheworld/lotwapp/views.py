from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def topfive(request):
    return render(request, 'topfive.html')

def northamerica(request):
    return render(request, 'northamerica.html')

def southamerica(request):
    return render(request, 'southamerica.html')

def africa(request):
    return render(request, 'africa.html')

def europe(request):
    return render(request, 'europe.html')

def asia(request):
    return render(request, 'asia.html')

def australia(request):
    return render(request, 'australia.html')