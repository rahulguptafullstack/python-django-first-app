from django import forms  
from home.models import Contact  
  
class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = "__all__"  
    
    def clean(self):
        cleaned_data = super().clean()
        email_address = cleaned_data.get("email")
        if not (email_address):
            raise forms.ValidationError("You must enter email.")