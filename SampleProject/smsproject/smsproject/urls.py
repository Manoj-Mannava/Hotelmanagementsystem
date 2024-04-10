from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Change the root URL to userSignup
    path('', views.userSignup, name='root'),
    path('bookedrooms/', views.bookedrooms, name='bookedrooms'),
    path('home/', views.homefunction, name='home'),
    path('about/', views.aboutfunction, name='about'),
    path('contact/', views.contactfunction, name='contact'),
    path('userSignup/', views.userSignup, name='userSignup'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('user0/', views.user0, name='user0'),
    path('user1/', views.user1, name='user1'),
    path('user2/', views.user2, name='user2'),
    path('Admin1/', views.Admin1, name='Admin1'),
    path('roomEntry/', views.roomEntry, name='roomEntry'),
    path('Admin2/', views.Admin2, name='Admin2'),
    path('deleteAdminrooms/', views.deleteAdminRooms, name='deleteAdminRooms'),
    path('Admin3/', views.Admin3, name='Admin3'),
    path('bookingProcess/', views.bookingProcess, name='bookingProcess'),
    path('roomConformed/', views.roomConformed, name='roomConformed'),
    path('hotelSelect/', views.hotelSelect, name='hotelSelect'),

    # Admin pages
    path('adminSignup/', views.adminSignup, name='adminSignup'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('index/', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
