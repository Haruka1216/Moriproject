from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import VillagerCreateView, EventCreateView, CreatureCreateView

app_name = 'moriapp'


urlpatterns = [
    path('',views.index, name='index'), #トップページ
    path('villagers/', views.villager_list, name='villager_list'), #住民図鑑
    path('events/', views.event_list, name='event_list'), #イベント
    path('creatures/', views.creature_list,name='creature_list'), #魚虫図鑑
    path('contact/',views.contact, name='contact'), #お問い合わせ
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'), #ログイン
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'), #ログアウト
    path('profile/',views.profile_view,name='profile_view'), #プロフィール
    path('profile/edit/',views.profile_edit, name='profile_edit'),
    path('villager/add/', VillagerCreateView.as_view(), name='villager_add'), #住民を追加
    path('event/add/', EventCreateView.as_view(), name='event_add'), #イベントを追加
    path('creature/add/', CreatureCreateView.as_view(), name='creature_add'), #魚虫を追加
    
]
