import graphene
from graphene_django.types import DjangoObjectType
from game_store.models import Customer, Developer, Discount, Game, Genre, Inventory, Order, Platform, Publisher, Review

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer

class DeveloperType(DjangoObjectType):
    class Meta:
        model = Developer

class DiscountType(DjangoObjectType):
    class Meta:
        model = Discount

class GameType(DjangoObjectType):
    class Meta:
        model = Game

class GenreType(DjangoObjectType):
    class Meta:
        model = Genre

class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class PlatformType(DjangoObjectType):
    class Meta:
        model = Platform

class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher

class ReviewType(DjangoObjectType):
    class Meta:
        model = Review

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    all_developers = graphene.List(DeveloperType)
    all_discounts = graphene.List(DiscountType)
    all_games = graphene.List(GameType)
    all_genres = graphene.List(GenreType)
    all_inventories = graphene.List(InventoryType)
    all_orders = graphene.List(OrderType)
    all_platforms = graphene.List(PlatformType)
    all_publishers = graphene.List(PublisherType)
    all_reviews = graphene.List(ReviewType)

    def resolve_all_customers(self, info, **kwargs):
        return Customer.objects.all()

    def resolve_all_developers(self, info, **kwargs):
        return Developer.objects.all()

    def resolve_all_discounts(self, info, **kwargs):
        return Discount.objects.all()

    def resolve_all_games(self, info, **kwargs):
        return Game.objects.all()

    def resolve_all_genres(self, info, **kwargs):
        return Genre.objects.all()

    def resolve_all_inventories(self, info, **kwargs):
        return Inventory.objects.all()

    def resolve_all_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_all_platforms(self, info, **kwargs):
        return Platform.objects.all()

    def resolve_all_publishers(self, info, **kwargs):
        return Publisher.objects.all()

    def resolve_all_reviews(self, info, **kwargs):
        return Review.objects.all()

schema = graphene.Schema(query=Query)
