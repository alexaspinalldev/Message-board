# Shell command
from django.contrib.auth.models import User
from django.urls import reverse
from catalogue.models import Coffee
from django.test import Client

# Create a superuser
user = User.objects.create_superuser(
    username="myUsername3",
    password="myPassword",
    email="test1@test.com"
)

# Create a Coffee instance
coffee = Coffee.objects.create(
    coffee_name="Test coffee",
    vendor=user,
    origin="Africa",
    bean="robusta",
    taste_profile="Tasty",
    roast="light",
    description="description test",
    listing_approved=True
)

# Verify Coffee object creation
print(f"Coffee created: {coffee}")

# Simulate a client request
client = Client()
client.login(username="myUsername3", password="myPassword")  # Log in as the superuser

# Get the coffee detail page
response = client.get(reverse('coffee_detail', args=[coffee.product_ID]))
print(f"Response status code: {response.status_code}")

# Test the response
if response.status_code == 200:
    print("Test passed: Coffee detail page rendered successfully.")
else:
    print(f"Test failed: Unexpected status code {response.status_code}")


# ^This script didn't work
# "NoReverseMatch: Reverse for 'coffee_detail' not found. 'coffee_detail' is not a valid view function or pattern name."














# class TestCoffeeViews(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_superuser(
#             username="myUsername",
#             password="myPassword",
#             email="test@test.com"
#         )
#         self.coffee = Coffee(
#             coffee_name=="Test coffee",
#             vendor=self.user,
#             origin="Africa",
#             bean="robusta",
#             taste_profile="Tasty",
#             roast="light",
#             description="description test",
#             listing_approved=True,
#         )
#         self.coffee.save()

#     def test_render_coffee_detail_page(self):
#         response = self.client.get(reverse(
#             'coffee_detail', args=['product_id']))
#         self.assertEqual(response.status_code, 200)

# TestCoffeeViews()