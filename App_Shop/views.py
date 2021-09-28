from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Shop.forms import CatagoryForm,ProductForm,ProductFormAnother
from App_Shop.models import Category,Product
from App_Login.models import Seller
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
# Create your views here.

# class CreateQuiz(CreateView):
#     fields=('course_name','question_number',)
#     model=category
#     template_name='quiz/create.html'
#     def get_success_url(self):
#         print('pk')
#         print(self.get_object)
def is_seller(user):
    try:
        return user.is_authenticated and user.seller is not None
    except Seller.DoesNotExist:
        return False
@user_passes_test(is_seller)
def create_product(request,pk):
    category=Category.objects.get(pk=pk)
    form=ProductFormAnother()
    print('Hello')
    if 'save' in request.POST:
        form=ProductFormAnother(request.POST,request.FILES)
        # print(form)
        # check=Category.objects.filter(title=form)
        if form.is_valid():
            form=form.save(commit=False)
            form.seller=request.user
            form.category=category
            form.save()
            return HttpResponseRedirect(reverse('App_Login:home'))
    if 'another' in request.POST:
        form=ProductFormAnother(request.POST,request.FILES)
        # print(form)
        if form.is_valid():
            form=form.save(commit=False)
            form.seller=request.user
            form.category=category
            form.save()
            return HttpResponseRedirect(reverse('App_Shop:add_product',kwargs={'pk':pk}))
    return render(request,'quiz/create_ans.html',context={'form':form})

@user_passes_test(is_seller)
def create_category(request):
    form=CatagoryForm()
    if request.method == 'POST':
        form=CatagoryForm(request.POST)
        
        if form.is_valid():
            
            form=form.save(commit=False)
            print('test1')
            print(form)
            check=Category.objects.filter(title=form)
            print('check')
            print(check)
            if check:
                messages.info(request, "This catagory is already added please go to Add product in catagory.")
                return HttpResponseRedirect(reverse('App_Shop:home_product'))
            else:  
                form.seller=request.user
                form.save()
                pk=form.pk
                print('test2')
                print(form)
                return HttpResponseRedirect(reverse('App_Shop:add_product',kwargs={'pk':pk}))
    return render(request,'quiz/create.html',context={'form':form})



@user_passes_test(is_seller)
def create_another_product(request):
    catagory=Category.objects.all()
    print('Hello')
    if catagory.exists():

        form=ProductForm()
        if 'save' in request.POST:
            form=ProductForm(request.POST,request.FILES)
            # print(form)
            if form.is_valid():
                form=form.save(commit=False)
                form.seller=request.user
                form.save()
                return HttpResponseRedirect(reverse('App_Login:home'))
        if 'another' in request.POST:
            form=ProductForm(request.POST,request.FILES)
            # print(form)
            if form.is_valid():
                form=form.save(commit=False)
                form.seller=request.user
                form.save()
                return HttpResponseRedirect(reverse('App_Shop:add_another_product'))
        return render(request,'quiz/create_ans.html',context={'form':form})
    else:
        return HttpResponseRedirect(reverse('App_Shop:catagory'))

class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

def home(request):
    catagory=Category.objects.all()
    products=Product.objects.all()
    return render(request,'App_Shop/home1.html',context={'catagory':catagory,'products':products,})

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'

def also(request,catagory):
    catagory=Category.objects.filter(title=catagory)
    print(catagory)
    return render(request,'App_Shop/also.html',context={'catagory':catagory})

class Also(DetailView):
    model=Category
    
    template_name='App_Shop/also.html'

def collection(request):
    return render(request,'Collection/col1.html',context={})

def products(request):
    search=False
    if request.method == 'GET':
        a=[]
        print(request.GET)
        
        for i in request.GET:
            print('I :',i)
            a.append(i)
        cata=Category.objects.filter(title__in=a)
        product_search=Product.objects.filter(category__in=cata)
        print('Cata :',cata)
        print('Pro :',product_search)
    print('A :',a)
    print(a.__len__())
    products=Product.objects.all()
    return render(request,'App_Shop/product.html',context={'products':products,'product_search':product_search})

def contact(request):
    return render(request,'App_Shop/contact.html',context={})

def about(request):
    return render(request,'App_Shop/about.html',context={})

