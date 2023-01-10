from django.shortcuts import render, redirect
from django.core.mail import send_mail
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ItemForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect("band-detail", band.id)
    else:
        form = BandForm()

    return render(request, "listings/band_create.html", {"form": form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect("band-detail", band.id)
    else:
        form = BandForm(instance=band)

    return render(request, "listings/band_update.html", {"form": form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == "POST":
        band.delete()
        return redirect("band-list")

    return render(request, "listings/band_delete.html", {"band": band})


def about(request):
    return render(request, "listings/about.html")


def item_list(request):
    items = Listing.objects.all()
    return render(request, "listings/item_list.html", {"items": items})


def item_detail(request, id):
    item = Listing.objects.get(id=id)
    return render(request, "listings/item_detail.html", {"item": item})


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("item-detail", item.id)

    else:
        form = ItemForm()

    return render(request, "listings/item_create.html", {"form": form})


def item_update(request, id):
    item = Listing.objects.get(id=id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item-detail", item.id)
    else:
        form = ItemForm(instance=item)

    return render(request, "listings/item_update.html", {"form": form})


def item_delete(request, id):
    item = Listing.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect("item-list")

    return render(request, "listings/item_delete.html", {"item": item})


def contact(request):
    if request.method == "POST":
        # créer une instance de notre formulaire et le remplir
        # avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f"""Message from {form.cleaned_data["name"]
                        or "anonyme"} via MerchEx Contact Us form""",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")
    # si le formulaire n'est pas valide, nous laissons l'exécution
    # continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        form = ContactUsForm()

    return render(request, "listings/contact.html", {"form": form})


def contact_success(request):
    return render(request, "listings/contact_success.html")
