from django import forms


from .models import car, Driver


class carForm(forms.ModelForm):
    class Meta:
        model = car
        fields = "__all__"


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["name", "image", "date_of_birth", "phone_number", "driving_license_image"]
