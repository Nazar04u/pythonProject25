from django.contrib import admin
<<<<<<< HEAD
from .models import Goods, Comment, Question, Basket, BasketItems
=======
from .models import Goods, Comment, Question, Basket, UserOrder, BasketItems
>>>>>>> origin/main

class BasketItemsAdmin(admin.ModelAdmin):
    pass

<<<<<<< HEAD
=======
class UserOrderAdmin(admin.ModelAdmin):
    pass
>>>>>>> origin/main

class BasketAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'text')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'good')

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount')


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Basket, BasketAdmin)
<<<<<<< HEAD
=======
admin.site.register(UserOrder, UserOrderAdmin)
>>>>>>> origin/main
admin.site.register(BasketItems, BasketItemsAdmin)