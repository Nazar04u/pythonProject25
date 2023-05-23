from django.contrib import admin
from .models import Goods, Comment, Question, Basket, BasketItems

class BasketItemsAdmin(admin.ModelAdmin):
    list_display = ('basket', 'goods', 'quantity')


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'active', 'admin_names', 'admin_total')

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
admin.site.register(BasketItems, BasketItemsAdmin)