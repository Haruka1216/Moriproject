from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'moriapp'


urlpatterns = [
    path('',views.index, name='index'), #トップページ
    path('villagers/', views.villager_list, name='villager_list'), #住民図鑑
    path('events/', views.event_list, name='event_list'), #イベント
    path('creatures/', views.creature_list,name='creature_list'), #魚虫図鑑
    path('contact/',views.contact, name='contact'), #お問い合わせ
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',views.profile_view,name='profile_view'),
    path('profile/edit/',views.profile_edit, name='profile_edit')
    
]
