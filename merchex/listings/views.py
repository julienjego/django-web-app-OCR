from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")


def listings(request):
    list = Listing.objects.all()
    return HttpResponse(
        f"""<h1>Page Listings</h1>
                        <ul>
                            <li>{list[0].title}</li>
                            <li>{list[1].title}</li>
                            <li>{list[2].title}</li>
                            <li>{list[3].title}</li>
                        </ul>"""
    )


def contact(request):
    return HttpResponse("<h1>Contact Us ! </h1>")
