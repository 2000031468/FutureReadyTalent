#all the functions are sepcified here..!
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,Orderplaced
from .forms import CustomerRegistrationForm
from django.contrib import messages
#def home(request):# this is for the component bases
# return render(request, 'app/home.html')

class ProductView(View):
 def get(self,request):
  Cpesticides = Product.objects.filter(category='P')
  Fertlizers=Product.objects.filter(category='F')
  Pesticides=Product.objects.filter(category='PE')
  Equipment=Product.objects.filter(category='E')
  return render(request,'app/home.html',{'Cpesticides':Cpesticides,'Fertlizers':Fertlizers,'Pesticides':Pesticides,'Equipment':Equipment})
#class baseed callinhor rendering

#def product_detail(request):
# return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self,request,pk):
  product=Product.objects.get(pk=pk)
  return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def pestagri(request,data=None):
 if data==None:
  pest=Product.objects.filter(category='P')
 elif data=='Plantic' or data=='BigHaat':
  pest=Product.objects.filter(category='P').filter(brand=data)
 elif data=='below':
  pest=Product.objects.filter(category='P').filter(discounted_price__lt=500)
 elif data=='above':
  pest=Product.objects.filter(category='P').filter(discounted_price__gt=500)
 return render(request, 'app/pestagri.html',{'pest':pest})

#def login(request):
 #return render(request, 'app/login.html')
 # we are removing login since we are using default athuntication no need we directly write them in urls.py
# defaultly loginform is created by django we just use them
class CustomerRegistrationView(View):
 def get(self,request):
  form=CustomerRegistrationForm()
  return render(request,'app/customerregistration.html',{'form':form})
 def post(self,request):
  form=CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request,'Congratulations !! You have Registered Sucessfully')
   form.save()
  return render(request,'app/customerregistration.html',{'form':form})




#def customerregistration(request):
 #return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def fertilizers(request,data=None):
 if data == None:
  pest = Product.objects.filter(category='F')
 elif data == 'GeoLife' or data == 'Uravara':
  pest = Product.objects.filter(category='F').filter(brand=data)
 elif data=='below':
  pest=Product.objects.filter(category='F').filter(discounted_price__lt=1500)
 elif data=='above':
  pest=Product.objects.filter(category='F').filter(discounted_price__gt=1500)

 return render(request, 'app/fertilizers.html', {'pest': pest})
 #return render(request,'app/fertilizers.html')

def aboutus(request):
 return render(request,'app/aboutus.html')


def pestaqua(request,data=None):
 if data == None:
  pest = Product.objects.filter(category='PE')
 elif data == 'Aquagrow' or data == 'AquaVitals':
  pest = Product.objects.filter(category='PE').filter(brand=data)
 elif data=='below':
  pest=Product.objects.filter(category='PE').filter(discounted_price__lt=1500)
 elif data=='above':
  pest=Product.objects.filter(category='PE').filter(discounted_price__gt=1500)
 return render(request, 'app/pestaqua.html', {'pest': pest})
 #return render(request,'app/pestaqua.html')

def faq(request):
 return render(request,'app/faq.html')

def equip(request,data=None):
 if data == None:
  equip = Product.objects.filter(category='E')
 elif data == 'Aquagri' or data == 'Allexpress':
  equip = Product.objects.filter(category='E').filter(brand=data)
 elif data=='below':
  equip=Product.objects.filter(category='E').filter(discounted_price__lt=1500)
 elif data=='above':
  equip=Product.objects.filter(category='E').filter(discounted_price__gt=1500)

 return render(request, 'app/equip.html', {'equip': equip})
 #return render(request,'app/equip.html')