from django.urls import path
from . import views

urlpatterns = [
    # ... existing code ...
    path("drivers/", views.driver_list, name="driver_list"),
    path("drivers/add/", views.add_driver, name="add_driver"),
    path("drivers/<int:id>/edit/", views.edit_driver, name="edit_driver"),
    path("drivers/<int:id>/delete/", views.delete_driver, name="delete_driver"),
    # ... existing code ...
]
