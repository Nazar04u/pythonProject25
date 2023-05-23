from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
<<<<<<< HEAD
from .models import Goods, Comment, Question, Basket, BasketItems
=======
from .models import Goods, Comment, Question, Basket, BasketItems, UserOrder
>>>>>>> origin/main
from django import forms
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import SignUpForm, SignInForm, CommentForm, QuestionForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        goods = Goods.objects.filter(date__gte=timezone.now() - timezone.timedelta(days=7),
                                    date__lte=timezone.now())
        paginator = Paginator(goods, 4)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        if User.is_authenticated:
            user = self.request.user
            if Basket.objects.filter(user=user).count() == 0:
                basket = Basket(user=user, active=True)
                basket.save()
            else:
                basket = Basket.objects.get(user=user, active=True)
            return render(request, "realization/home.html", context={
                'page_obj': page_obj,
                'basket':basket,
                'user': user,
            })
        return render(request, "realization/home.html", context={
            'page_obj': page_obj,
        })


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'realization/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  #ADD method save in forms
            if user is not None:
                login(request, user)
            return redirect('home')
        return render(request, 'realization/signup.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'realization/signin.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                raise forms.ValidationError("Wrong data.")
        return render(request, 'realization/signin.html', context={
            'form': form,
        })


class DetailView(View):
    def get(self, request, pk, *args, **kwargs):
        good = Goods.objects.get(pk=pk)
        form = CommentForm()
        comment = Comment.objects.filter(good=good)
        if User.is_authenticated:
            user = self.request.user
            if Basket.objects.filter(user=user).count() == 0:
                basket = Basket(user=user, active=True)
                basket.save()
            else:
                basket = Basket.objects.get(user=user, active=True)
            return render(request, "realization/detail.html", context={
                'good': good,
                'form': form,
                'comment': comment,
                'basket': basket,
                'user': user,
            })
        return render(request, 'realization/detail.html', context={
            'good': good,
            'form': form,
            'comment': comment,
        })

    def post(self, request, pk, *args, **kwargs):
        comment = CommentForm(request.POST)
        if comment.is_valid():
            user = self.request.user
            good = get_object_or_404(Goods, pk=pk)
            commentar = request.POST['comment']
            assess = request.POST['assess']
            comment = Comment.objects.create(user=user, good=good, comment=commentar, assess=assess)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'realization/home.html', context={})


class QuestionView(View):
    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        return render(request, 'realization/question.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            if User.is_authenticated:
                user = self.request.user
                text = request.POST['text']
                form = Question.objects.create(user=user, text=text)
                return render(request, 'realization/thanks.html')
            return render(request, 'realization/signup.html', context={
                 'title': 'User is not login'
             })
        return render(request, 'realization/home.html', context={})


class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'realization/thanks.html')


class BasketView(View):
    def get(self, request, id, *args, **kwargs):
        basket = Basket.objects.get(id=id)
<<<<<<< HEAD
        basket_items = Basket.objects.get(basket=basket).item
=======
        basket_items = BasketItems.objects.filter(basket=basket)
>>>>>>> origin/main
        return render(request, 'realization/basket.html', context={
            "basket": basket,
            "basket_items": basket_items,
        })


def add_to_cart(request, item_id, *args, **kwargs):
    product = Goods.objects.get(id=item_id)
    user = request.user
    basket = Basket.objects.get(user=user, active=True)
    print(product)
<<<<<<< HEAD
    print(basket)
    basket_item, status = BasketItems.objects.get_or_create(item=product, basket=basket, quantity=1)
    print(basket_item)
    basket.items.add(product)
    basket.items.save()
=======
    basket_item, status = BasketItems.objects.get_or_create(item=product)
    user = request.user
    print(basket_item)
    order, status = UserOrder.objects.get_or_create(user=user, basket=basket, is_ordered=status)
    print(order.order_items)
    print(order)
    print(order.user)
    print(status)
    order.order_items.add(basket_item)
    print(order.order_items)
    order.save()
>>>>>>> origin/main
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def delete_from_cart(request, item_id, *args, **kwargs):
    product = Goods.objects.filter(id=item_id)
    basket_item = BasketItems.objects.filter(item=product)
    if basket_item.exists():
        basket_item[0].delete()
<<<<<<< HEAD
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
=======
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
>>>>>>> origin/main
