from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Coffee
from .forms import CoffeeAdd
from .forms import CoffeeUpdate
from django.utils import timezone

# Create your views here.
# Main list of all approved listings
class CoffeeList(generic.ListView):
    queryset = Coffee.objects.filter(listing_approved=True)
    template_name = "coffee_list.html"
    paginate_by = 16



# Filtered list for the user
class CoffeeMyList(generic.ListView):
    template_name = "coffee_list.html"
    paginate_by = 16

    def get_queryset(self):
        # Access the currently logged-in user
        user = self.request.user
        # Filter Coffee objects for the current user and approved listings
        return Coffee.objects.filter(listing_approved=True, vendor=user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            # Add a message and redirect if no listings exist
            messages.error(request, "You do not have any approved listings.")
        return super().get(request, *args, **kwargs)



# Detail view of an individual coffee listing
def coffee_detail(request, product_ID):
    queryset = Coffee.objects.filter(listing_approved=True)
    coffee = get_object_or_404(queryset, product_ID=product_ID)

    return render(
        request,
        "coffee_detail.html",
        {"coffee": coffee,
        "page_title": coffee.coffee_name},)



# Add a new coffee listing
def coffee_add(request):
    """
    view to add a new coffee listing. The button is only visible to authenticated users.
    """
    if request.method == "POST":
        coffee_to_add = CoffeeAdd(data=request.POST, files=request.FILES)

        if coffee_to_add.is_valid():
            coffee = coffee_to_add.save(commit=False)
            coffee.vendor = request.user # Explicitly adding the required values as "using commit=False creates an unsaved instance of the Coffee object"
            coffee.updated_at = timezone.now()
            coffee.created_at = timezone.now()
            coffee.listing_approved = True # In production this would be false in order to be moderated
            coffee.save()
            new_coffee_id = coffee.pk

            messages.add_message(request, messages.SUCCESS, 'Your listing was added')
    else:
        messages.add_message(request, messages.ERROR, 'Error adding listing')

    return HttpResponseRedirect(reverse('Coffee detail', args=[new_coffee_id]))



# Edit a coffee listing
def coffee_edit(request, product_ID):
    """
    view to edit a coffee listing. The button is only visible to authenticated users who are also the Coffee Vendor.
    """
    if request.method == "POST":
        queryset = Coffee.objects
        coffee = get_object_or_404(queryset, product_ID=product_ID)
        coffee_update = CoffeeUpdate(data=request.POST, files=request.FILES)
        editingVendor = coffee.vendor
        idToUpdate = product_ID
        existingCreated_at = coffee.created_at

        if coffee_update.is_valid() and coffee.vendor == request.user:
            coffee = coffee_update.save(commit=False)
            coffee.vendor = editingVendor # Explicitly adding the fixed values as "using commit=False creates an unsaved instance of the Coffee object" and Vendor is required.
            coffee.product_ID = idToUpdate
            coffee.updated_at = timezone.now()
            coffee.created_at = existingCreated_at
            coffee.listing_approved = True # In production this would be false in order to be moderated
            coffee.save()
            messages.add_message(request, messages.SUCCESS, 'The listing was updated')
    else:
        messages.add_message(request, messages.ERROR, 'Error updating listing')

    return HttpResponseRedirect(reverse('Coffee detail', args=[product_ID]))



# Delete a coffee listing
def coffee_delete(request, product_ID):
    """
    view to delete a coffee listing. The button is only visible to authenticated users who are also the Coffee Vendor.
    """
    queryset = Coffee.objects
    coffee = get_object_or_404(queryset, product_ID=product_ID)

    if coffee.vendor == request.user: #Validate the request on the backend
        coffee.delete()
        messages.add_message(request, messages.SUCCESS, 'Your coffee listing was deleted')
    else:
        messages.add_message(request, messages.ERROR, 'Invalid action')

    return HttpResponseRedirect(reverse('Catalogue'))