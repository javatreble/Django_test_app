from django.urls import path

from testApp.views import ContactCreate, thanks, download

app_name='contacts'
urlpatterns = [
    path("contact/", ContactCreate.as_view(), name="contact"),
    path("thanks/", thanks, name="thanks"),
    path("download/", download, name="download"),

]