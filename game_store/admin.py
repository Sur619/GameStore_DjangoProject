from django.contrib import admin

from game_store.models import Game, Customer, Developer, Discount, Genre, Inventory, Order, Platform, Publisher, Review

# Register your models here.

admin.site.register(Game)
admin.site.register(Customer)
admin.site.register(Developer)
admin.site.register(Discount)
admin.site.register(Genre)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Platform)
admin.site.register(Publisher)
admin.site.register(Review)