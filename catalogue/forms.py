from .models import Coffee
from .models import VendorAbout
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CoffeeAdd(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('coffee_name', 'origin', 'bean', 'taste_profile', 'roast', 'description', 'product_image')

class CoffeeUpdate(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('coffee_name', 'origin', 'bean', 'taste_profile', 'roast', 'description', 'product_image')

# Extend SIGNUP FORM
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30,
        label=_("Your company"),
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _("Coffee Company Ltd")}),
    )
    about = forms.CharField(
        help_text = "Tell us about your business. This will be displayed below your coffee listings.",
        widget=forms.Textarea(attrs={"placeholder": _("Founded in 2025, Coffee Company Ltd is... ")}),
        required=True,
    )

    def save(self, request):
        # Call the parent save method to create the user
        user = super(CustomSignupForm, self).save(request)

        # Update the user's first_name
        user.first_name = self.cleaned_data["first_name"]
        user.save()

        # Create the VendorAbout instance and associate it with the user
        about_text = self.cleaned_data["about"]
        VendorAbout.objects.create(vendor_id=user.pk, about=about_text)

        return user