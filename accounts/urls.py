from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index_accounts, name='index_accounts'),
    path('base/', views.base_view, name='base_view'),
    path('user/create', views.user_create, name='user_create'),
    path('teacher/edit/', views.teacher_edit, name='teacher_edit'),
    path('student/edit/', views.student_edit, name='student_edit'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('logout/',views.logout_view, name='logout_view'),
    path('accounts/login/',views.login_view, name='login_view'),
    path('search/', views.search_view, name='search_view'),

]


