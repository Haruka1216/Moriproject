from django.shortcuts import render,redirect
from .models import Villager, Event, Creature
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm
from .forms import ProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Villager, Event, Creature
from .forms import VillagerForm, EventForm, CreatureForm

def index(request):
    return render(request, 'moriapp/index.html')


def villager_list(request):
    villagers = Villager.objects.all()
    return render(request, 'moriapp/villager_list.html', {'villagers': villagers})


def event_list(request):
    events = Event.objects.all()
    return render(request, 'moriapp/event_list.html', {'events': events})


def creature_list(request):
    creatures = Creature.objects.all().order_by('name')
    return render(request, 'moriapp/creature_list.html', {'creatures': creatures})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"お問い合わせ: {name}",
                message=f"名前: {name}\nメール: {email}\n内容:\n{message}",
                from_email='tdn2532019@stu.o-hara.ac.jp',
                recipient_list=['tdn2532019@stu.o-hara.ac.jp'],
                fail_silently=False,
            )
            return render(request, 'moriapp/contact_done.html')
    else:
        form = ContactForm()
    
    return render(request, 'moriapp/contact.html', {'form': form})

@login_required
def profile_view(request):
   profile, created = UserProfile.objects.get_or_create(user=request.user)
   return render(request, 'moriapp/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
   profile, created = UserProfile.objects.get_or_create(user=request.user)
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES, instance=profile)
       if form.is_valid():
           form.save()
           return redirect('moriapp:profile_view')
   else:
       form = ProfileForm(instance=profile)
   return render(request, 'moriapp/profile_edit.html', {'form': form})


#投稿ページ
class VillagerCreateView(LoginRequiredMixin, CreateView):
    model = Villager
    form_class = VillagerForm
    template_name = 'moriapp/create_form.html'
    success_url = reverse_lazy('moriapp:index')

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'moriapp/create_form.html'
    success_url = reverse_lazy('moriapp:index')

class CreatureCreateView(LoginRequiredMixin, CreateView):
    model = Creature
    form_class = CreatureForm
    template_name = 'moriapp/create_form.html'
    success_url = reverse_lazy('moriapp:index')