from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:id>/<slug:slug>', views.category, name='category'),
    path('details/<str:id>/<slug:slug>', views.details, name='details'),
    path('talktous/', views.talktous, name='talktous'),
    path('search/', views.search, name='search'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('password/', views.password_update, name='password'),
    path('booking/', views.booking, name='booking'),
    path('booked/', views.booked, name='booked'),
    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.pay, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('delete/', views.delete, name='delete'),
    path('history/', views.history, name='history'),
    path('del_history/', views.del_history, name='del_history'),
]
 


