from django.test import TestCase
from catalogue.forms import CoffeeAdd
from catalogue.forms import CoffeeUpdate
from catalogue.forms import CustomSignupForm

# Shell scripts
# Coffee add:
coffee_form_data = {
    "coffee_name": "Test Coffee",
    "origin": "Bangladesh",
    "bean": "robusta",
    "taste_profile": "Floral, bright acidity, with hints of jasmine and stone fruit.",
    "roast": "light",
    "description": "Test case",
    "product_image": "default",
}
coffee_add_form = CoffeeAdd(data=coffee_form_data)
print(coffee_add_form.is_valid())
print(coffee_add_form.errors)

# Coffee edit:
coffee_update_form = CoffeeUpdate(data=coffee_form_data)
print(coffee_add_form.is_valid())
print(coffee_add_form.errors)

# CustomSignupForm:
signup_form_data = {
    # Customised fields
    "first_name": "Test user",
    "about": "Test about",
    # Parent class fields
    "username": "testuser",
    "email_address": "testuser@gmmail.com",
    "password1": "passwordz123§",
    "password2": "passwordz123§",
}
coffee_add_form = CustomSignupForm(data=signup_form_data)
print(coffee_add_form.is_valid())
print(coffee_add_form.errors)








# class TestCoffeeAddForm(TestCase):
#     def test_form_is_valid(self):
#         coffee_add_form = CoffeeAdd({
#         "coffee_name": "Test Coffee",
#         "origin": "Bangladesh",
#         "bean": "robusta",
#         "taste_profile": "Floral, bright acidity, with hints of jasmine and stone fruit.",
#         "roast": "light",
#         "description": "Test case",
#     },)
#         self.assertTrue(coffee_add_form.is_valid())