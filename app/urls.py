from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("add-subject", views.add_subject, name="add_subject")
]