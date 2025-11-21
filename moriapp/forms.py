from django import forms
from .models import UserProfile

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio','favorite_villager','icon']