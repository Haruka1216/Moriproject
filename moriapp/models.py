from django.contrib.auth.models import User
from django.db import models

#住民モデル
class Villager(models.Model):
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)
    birthday = models.CharField(max_length=20)
    catchphrase = models.CharField(max_length=100)
    image = models.ImageField(upload_to='villagers/')

    def __str__(self):
        return self.name
    
#イベントモデル
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='events/',blank=True)

    def __str__(self):
        return self.title
    
#魚・虫モデル
class Creature(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=[('fush','魚'),('bug','虫')])
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='creatures/')

    def __str__(self):
        return self.name


#プロフィール
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    favorite_villager = models.CharField(max_length=100, blank=True)
    icon = models.ImageField(upload_to='profile_icons/', blank=True, null=True)

    def __str__(self):
        return self.user.username