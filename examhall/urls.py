from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('signup/', views.signup, name='admin_signup'),
    path('login/', views.login, name='admin_login'),
    path('', RedirectView.as_view(url='dashboard/')),
    path('dashboard/', views.index, name='admin_dashboard'),
    path('manage_block/', views.manage_block, name='manage_block'),
    path('manage_room/', views.manage_room, name='manage_room'),
    path('manage_course/', views.manage_course, name='manage_course'),
    path('manage_department/', views.manage_department, name='manage_department'),
    path('manage_students/', views.manage_student, name='manage_student'),
    path('manage_teachers/', views.manage_teacher, name='manage_teacher'),
    path('logout/', views.logout, name='admin_logout'),
]