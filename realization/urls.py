from django.urls import path, include
from .views import HomeView, SignUpView, SignInView, DetailView, QuestionView, ThanksView, BasketView,add_to_cart


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>/', DetailView.as_view(), name='detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('question/', QuestionView.as_view(), name='question'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('basket/<int:id>/', BasketView.as_view(), name='basket'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart')
]







