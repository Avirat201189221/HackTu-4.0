from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def fund(request):
    return render(request,"fund.html")

def nA(request):
    return render(request,"news-Articles.html")