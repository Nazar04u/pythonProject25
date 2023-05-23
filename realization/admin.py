from django.contrib import admin
from .models import Goods, Comment, Question, Basket, UserOrder, BasketItems

class BasketItemsAdmin(admin.ModelAdmin):
    pass

class UserOrderAdmin(admin.ModelAdmin):
    pass

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
admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(BasketItems, BasketItemsAdmin)