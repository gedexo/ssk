from django import forms
from .models import Contact,ProductEnquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        
class ProductEnquiryForm(forms.ModelForm):
    class Meta:
        model = ProductEnquiry
        fields = "__all__"