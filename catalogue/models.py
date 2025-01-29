from django.db import models
from django.contrib.auth.models import User as Vendor
from cloudinary.models import CloudinaryField


BEAN_CHOICES = [
    ('arabica', 'Arabica'),
    ('excelsa', 'Excelsa'),
    ('robusta', 'Robusta'),
    ('liberica', 'Liberica'),]
ROAST_LEVELS = [
    ('light', 'Light'),
    ('medium', 'Medium'),
    ('dark', 'Dark'),]

class Coffee(models.Model):
    product_ID = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="vendor_coffees")
    coffee_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=100)
    bean = models.CharField(choices=BEAN_CHOICES, max_length=30)
    taste_profile = models.CharField(max_length=255)
    roast = models.CharField(choices=ROAST_LEVELS, max_length=30)
    description = models.TextField()
    product_image = CloudinaryField('image', default='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    listing_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.coffee_name} by {self.vendor}'
    class Meta:
        ordering = ["vendor", "coffee_name"]


class VendorAbout(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name="vendorabout")
    about = models.TextField()
