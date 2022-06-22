from django.urls import path
from app import views
from django.conf import settings # image related configuration package for dynamic response in webpage
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,PasswordChange

urlpatterns = [
    #path('', views.home), this is for when it is a component based fun
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    #int pk is for primary key
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=PasswordChange,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('fertilizers/',views.fertilizers,name='fertilizers'),
    path('fertilizers/<slug:data>', views.fertilizers, name='fertilizersdata'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('pestagri/',views.pestagri,name='pestagri'),
    path('pestagri/<slug:data>', views.pestagri, name='pestagridata'),
    path('pestaqua/',views.pestaqua,name='pestaqua'),
    path('pestaqua/<slug:data>',views.pestaqua,name='pestaquadata'),
    path('faq/',views.faq,name='faq'),
    path('equip/',views.equip,name='equip'),
    path('equip/<slug:data>',views.equip,name='equipdata'),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#image related configuration for dynamic response in webpage
