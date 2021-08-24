from django.shortcuts import render

# Create your views here.
#User Interfaces
def home(request):
    return render (request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def orderbook(request):
    return render(request, 'orderbook.html')

def ordersts(request):
    return render(request, 'ordersts.html')   

def signup(request):
    return render(request, 'signup.html')
    

#def addcustomer(request):
    