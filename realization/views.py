from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from .models import Goods, Comment, Question, Basket, BasketItems, Order
from django import forms
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import SignUpForm, SignInForm, CommentForm, QuestionForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q


class HomeView(View):
    def get(self, request, *args, **kwargs):
        goods = Goods.objects.filter(date__gte=timezone.now() - timezone.timedelta(days=7),
                                    date__lte=timezone.now())
        paginator = Paginator(goods, 4)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        user = self.request.user
        if user.is_authenticated:
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


def logout_view(request):
    logout(request)
    return render(request, 'realization/home.html')

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
                basket_items = basket.items.all()
            else:
                basket = Basket.objects.get(user=user, active=True)
                basket_items = basket.items.all()
            return render(request, "realization/detail.html", context={
                'good': good,
                'form': form,
                'comment': comment,
                'basket': basket,
                'basket_items': basket_items,
                'user': user,
            })
        return render(request, 'realization/home.html', context={
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
        form = SignUpForm()
        return render(request, "realization/signup.html", {"form": form})


class QuestionView(View):
    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        return render(request, 'realization/question.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            user = self.request.user
            if user.is_authenticated:
                text = request.POST['text']
                form = Question.objects.create(user=user, text=text)
                return render(request, 'realization/thanks.html')
            form = SignUpForm()
            return render(request, "realization/signup.html", {"form": form})
        form = SignUpForm()
        return render(request, "realization/signup.html", {"form": form})


class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'realization/thanks.html')


class BasketView(View):
    def get(self, request, id, *args, **kwargs):
        basket = Basket.objects.get(id=id)
        items = basket.items.all()
        return render(request, 'realization/basket.html', context={
            "basket": basket,
            'items': items,
        })


def add_to_cart(request, item_id, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        product = Goods.objects.get(id=item_id)
        basket = Basket.objects.get(user=user, active=True)
        basket.items.add(product)
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    form = SignUpForm()
    return render(request, "realization/signup.html", {"form": form})


def delete_from_cart(request, item_id, *args, **kwargs):
    user = request.user
    basket = Basket.objects.get(user=user, active=True)
    basket.items.remove(item_id)
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def submit_purchase(request, *args, **kwargs):
    if request.method == "POST":
        user = request.user
        total_price = float(request.POST.get("total_price"))
        basket = Basket.objects.get(user=user)
        order = Order.objects.create(basket=basket, total_price=total_price)
        order.basket_items = basket.items
        order.save()
        basket.items.clear()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class FilterPageView(View):
    def get(self, request, tag, *args, **kwargs):
        goods = Goods.objects.filter(tags__name=tag)
        if User.is_authenticated:
            user = self.request.user
            if Basket.objects.filter(user=user).count() == 0:
                basket = Basket(user=user, active=True)
                basket.save()
            else:
                basket = Basket.objects.get(user=user, active=True)
            return render(request, "realization/filtered_pages.html", context={
                'goods': goods,
                'basket': basket,
                'user': user,
            })
        form = SignUpForm()
        return render(request, "realization/signup.html", {"form": form})


class SearchView(View):

    def post(self, request, *args, **kwargs):
        q = request.POST['q']
        goods = Goods.objects.filter(Q(name__icontains=q))
        user = self.request.user
        if user.is_authenticated:
            if Basket.objects.filter(user=user).count() == 0:
                basket = Basket(user=user, active=True)
                basket.save()
            else:
                basket = Basket.objects.get(user=user, active=True)
            return render(request, "realization/searched_page.html", context={
                'goods': goods,
                'basket':basket,
                'user': user,
            })
        form = SignUpForm()
        return render(request, "realization/signup.html", {"form": form})