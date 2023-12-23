from django.urls import path
from adminpannel import views

urlpatterns = [

    path('dashboard', views.index, name='admin_home'),
    path('reg',views.reg_user, name='register'),
    path('login',views.login_user, name='login'),
    path('logout',views.logoutUser, name='logoutUser'),
    path('create_about',views.create_about, name='create_about'),
    path('show_about',views.show_about, name='show_about'),
    path('about_edit/<int:id>', views.about_edit, name= 'about_edit'),
    path('about_update/<int:id>', views.about_update, name= 'about_update'),
    path('delete_about/<int:id>',views.delete_about, name= 'delete_about'),
    path('about_status/<int:id>',views.about_status, name= 'about_status'),
    path('about_inactive/<int:id>',views.about_inactive, name= 'about_inactive'),
    path('create_speakers',views.create_speakers, name='create_speakers'),
    path('show_speakers',views.show_speakers, name='show_speakers'),
    path('speakers_edit/<int:id>', views.speakers_edit, name= 'speakers_edit'),
    path('speakers_update/<int:id>', views.speakers_update, name= 'speakers_update'),
    path('delete_speakers/<int:id>',views.delete_speakers, name= 'delete_speakers'),
    path('speakers_status/<int:id>',views.speakers_status, name= 'speakers_status'),
    path('speakers_inactive/<int:id>',views.speakers_inactive, name= 'speakers_inactive'),


    
]
