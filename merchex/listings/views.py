from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})
    

def about(request):
    return HttpResponse('<h1>About-us ooh!</h1>')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', {'listings': listings})
    

def contact(request):
    return HttpResponse('<h1>Page des contacts</h1>')
