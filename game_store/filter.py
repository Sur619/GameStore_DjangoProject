import django_filters
from game_store.models import Game, Order, Inventory, Review, Customer


class GameFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    platform = django_filters.CharFilter(field_name='platform__name', lookup_expr='exact')
    genre = django_filters.CharFilter(field_name='genres__name', lookup_expr='exact')
    publisher = django_filters.CharFilter(field_name='publisher__name', lookup_expr='exact')
    developer = django_filters.CharFilter(field_name='developer__name', lookup_expr='exact')

    class Meta:
        model = Game
        fields = {
            'title': ['icontains'],  # Filtering by title
            'price': ['lt', 'gt'],  # Filtering by price
            'platform': ['exact'],  # Filtering by platform
            'genres': ['exact'],  # Filtering by genre
            'publisher': ['exact'],  # Filtering by publisher
            'developer': ['exact'],  # Filtering by developer
            'release_date': ['date__gt', 'date__lt'],  # Filtering by release date
        }


class OrderFilter(django_filters.FilterSet):
    created_at__gt = django_filters.DateTimeFilter(field_name='order_date', lookup_expr='gte')
    created_at__lt = django_filters.DateTimeFilter(field_name='order_date', lookup_expr='lte')

    class Meta:
        model = Order
        fields = {
            'game__title': ['icontains'],  # Filtering by game title
            'customer__username': ['icontains'],  # Filtering by customer username
            'total_amount': ['lt', 'gt'],  # Filtering by total amount
        }


class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields = {
            'game__title': ['icontains'],  # Filtering by game title
            'quantity': ['lt', 'gt'],  # Filtering by quantity
            'price': ['lt', 'gt'],  # Filtering by price
        }


class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = {
            'game__title': ['icontains'],  # Filtering by game title
            'customer__username': ['icontains'],  # Filtering by customer username
            'rating': ['exact'],  # Filtering by rating
            'created_at': ['date__gt', 'date__lt'],  # Filtering by creation date range
        }


class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            'username': ['icontains'],  # Filtering by username
            'email': ['icontains'],  # Filtering by email
            'date_joined': ['date__gt', 'date__lt'],  # Filtering by date joined
        }
