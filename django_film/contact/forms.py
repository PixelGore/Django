from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


from .models import Contact

class ContactForm(forms.ModelForm):
    """Email subscribtion form"""
    
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('email', )
        widgets = {
            "email": forms.TextInput(attrs={'class':'editContent', 'placeholder': 'Your Email ...'})
        }
        labels = {
            'email':''
        }
