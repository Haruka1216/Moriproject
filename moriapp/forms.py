from django import forms
from .models import UserProfile
from .models import Villager, Event, Creature

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio','favorite_villager','icon']

class VillagerForm(forms.ModelForm):
    class Meta:
        model = Villager
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class CreatureForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = '__all__'
