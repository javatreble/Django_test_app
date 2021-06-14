from django.forms import ModelForm, Textarea

from testApp.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "message"]
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Would love to talk about Philip K. Dick"
                }
            )
        }