from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from game_store.models import Customer, Developer, Discount, Game, Genre, Inventory, Order, Platform, Publisher, Review


class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(username='testuser', email='test@example.com')

    def test_customer_creation(self):
        self.assertEqual(self.customer.username, 'testuser')
        self.assertEqual(self.customer.email, 'test@example.com')
        self.assertIsNotNone(self.customer.date_joined)

    def test_customer_updating(self):
        self.customer.username = 'newuser'
        self.customer.save()
        updated_customer = Customer.objects.get(id=self.customer.id)
        self.assertEqual(updated_customer.username, 'newuser')

    def test_customer_deletion(self):
        customer_id = self.customer.id
        self.customer.delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(id=customer_id)


class DeveloperModelTest(TestCase):

    def setUp(self):
        self.developer = Developer.objects.create(name='Test Developer')

    def test_developer_creation(self):
        self.assertEqual(self.developer.name, 'Test Developer')

    def test_developer_updating(self):
        self.developer.name = 'Updated Developer'
        self.developer.save()
        updated_developer = Developer.objects.get(id=self.developer.id)
        self.assertEqual(updated_developer.name, 'Updated Developer')

    def test_developer_deletion(self):
        developer_id = self.developer.id
        self.developer.delete()
        with self.assertRaises(Developer.DoesNotExist):
            Developer.objects.get(id=developer_id)


class DiscountModelTest(TestCase):

    def setUp(self):
        self.platform = Platform.objects.create(name='Test Platform')
        self.genre = Genre.objects.create(name='Action')
        self.publisher = Publisher.objects.create(name='Test Publisher')
        self.developer = Developer.objects.create(name='Test Developer')
        self.game = Game.objects.create(
            title='Test Game',
            platform=self.platform,
            publisher=self.publisher,
            developer=self.developer,
            release_date='2022-01-01',
            price=Decimal('59.99'),
            description='Test Description'
        )
        self.game.genres.add(self.genre)
        self.discount = Discount.objects.create(
            game=self.game,
            code='DISCOUNT20',
            discount_percentage=Decimal('20.00'),
            start_date='2022-01-01',
            end_date='2022-12-31'
        )

    def test_discount_creation(self):
        self.assertEqual(self.discount.code, 'DISCOUNT20')
        self.assertEqual(self.discount.discount_percentage, Decimal('20.00'))
        self.assertEqual(self.discount.start_date, '2022-01-01')
        self.assertEqual(self.discount.end_date, '2022-12-31')

    def test_discount_updating(self):
        self.discount.code = 'DISCOUNT30'
        self.discount.save()
        updated_discount = Discount.objects.get(id=self.discount.id)
        self.assertEqual(updated_discount.code, 'DISCOUNT30')

    def test_discount_deletion(self):
        discount_id = self.discount.id
        self.discount.delete()
        with self.assertRaises(Discount.DoesNotExist):
            Discount.objects.get(id=discount_id)


class GameModelTest(TestCase):

    def setUp(self):
        self.platform = Platform.objects.create(name='Test Platform')
        self.genre = Genre.objects.create(name='Action')
        self.publisher = Publisher.objects.create(name='Test Publisher')
        self.developer = Developer.objects.create(name='Test Developer')
        self.game = Game.objects.create(
            title='Test Game',
            platform=self.platform,
            publisher=self.publisher,
            developer=self.developer,
            release_date='2022-01-01',
            price=Decimal('59.99'),
            description='Test Description'
        )
        self.game.genres.add(self.genre)

    def test_game_creation(self):
        self.assertEqual(self.game.title, 'Test Game')
        self.assertEqual(self.game.platform, self.platform)
        self.assertEqual(self.game.publisher, self.publisher)
        self.assertEqual(self.game.developer, self.developer)
        self.assertEqual(self.game.release_date, '2022-01-01')
        self.assertEqual(self.game.price, Decimal('59.99'))
        self.assertEqual(self.game.description, 'Test Description')
        self.assertIn(self.genre, self.game.genres.all())

    def test_game_updating(self):
        self.game.title = 'Updated Game'
        self.game.save()
        updated_game = Game.objects.get(id=self.game.id)
        self.assertEqual(updated_game.title, 'Updated Game')

    def test_game_deletion(self):
        game_id = self.game.id
        self.game.delete()
        with self.assertRaises(Game.DoesNotExist):
            Game.objects.get(id=game_id)


class GenreModelTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Action')

    def test_genre_creation(self):
        self.assertEqual(self.genre.name, 'Action')

    def test_genre_updating(self):
        self.genre.name = 'Adventure'
        self.genre.save()
        updated_genre = Genre.objects.get(id=self.genre.id)
        self.assertEqual(updated_genre.name, 'Adventure')

    def test_genre_deletion(self):
        genre_id = self.genre.id
        self.genre.delete()
        with self.assertRaises(Genre.DoesNotExist):
            Genre.objects.get(id=genre_id)


class InventoryModelTest(TestCase):

    def setUp(self):
        self.platform = Platform.objects.create(name='Test Platform')
        self.genre = Genre.objects.create(name='Action')
        self.publisher = Publisher.objects.create(name='Test Publisher')
        self.developer = Developer.objects.create(name='Test Developer')
        self.game = Game.objects.create(
            title='Test Game',
            platform=self.platform,
            publisher=self.publisher,
            developer=self.developer,
            release_date='2022-01-01',
            price=Decimal('59.99'),
            description='Test Description'
        )
        self.game.genres.add(self.genre)
        self.inventory = Inventory.objects.create(
            game=self.game,
            quantity=10,
            price=Decimal('59.99')
        )

    def test_inventory_creation(self):
        self.assertEqual(self.inventory.game, self.game)
        self.assertEqual(self.inventory.quantity, 10)
        self.assertEqual(self.inventory.price, Decimal('59.99'))

    def test_inventory_updating(self):
        self.inventory.quantity = 5
        self.inventory.save()
        updated_inventory = Inventory.objects.get(id=self.inventory.id)
        self.assertEqual(updated_inventory.quantity, 5)

    def test_inventory_deletion(self):
        inventory_id = self.inventory.id
        self.inventory.delete()
        with self.assertRaises(Inventory.DoesNotExist):
            Inventory.objects.get(id=inventory_id)


class OrderModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(username='testuser', email='test@example.com')
        self.platform = Platform.objects.create(name='Test Platform')
        self.genre = Genre.objects.create(name='Action')
        self.publisher = Publisher.objects.create(name='Test Publisher')
        self.developer = Developer.objects.create(name='Test Developer')
        self.game = Game.objects.create(
            title='Test Game',
            platform=self.platform,
            publisher=self.publisher,
            developer=self.developer,
            release_date='2022-01-01',
            price=Decimal('59.99'),
            description='Test Description'
        )
        self.game.genres.add(self.genre)
        self.order = Order.objects.create(
            customer=self.customer,
            game=self.game,
            quantity=1,
            total_amount=Decimal('59.99')
        )

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.game, self.game)
        self.assertEqual(self.order.quantity, 1)
        self.assertEqual(self.order.total_amount, Decimal('59.99'))
        self.assertIsNotNone(self.order.order_date)

    def test_order_updating(self):
        self.order.quantity = 2
        self.order.total_amount = Decimal('119.98')
        self.order.save()
        updated_order = Order.objects.get(id=self.order.id)
        self.assertEqual(updated_order.quantity, 2)
        self.assertEqual(updated_order.total_amount, Decimal('119.98'))

    def test_order_deletion(self):
        order_id = self.order.id
        self.order.delete()
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id=order_id)


class PlatformModelTest(TestCase):

    def setUp(self):
        self.platform = Platform.objects.create(name='Test Platform')

    def test_platform_creation(self):
        self.assertEqual(self.platform.name, 'Test Platform')

    def test_platform_updating(self):
        self.platform.name = 'Updated Platform'
        self.platform.save()
        updated_platform = Platform.objects.get(id=self.platform.id)
        self.assertEqual(updated_platform.name, 'Updated Platform')

    def test_platform_deletion(self):
        platform_id = self.platform.id
        self.platform.delete()
        with self.assertRaises(Platform.DoesNotExist):
            Platform.objects.get(id=platform_id)


class PublisherModelTest(TestCase):

    def setUp(self):
        self.publisher = Publisher.objects.create(name='Test Publisher')

    def test_publisher_creation(self):
        self.assertEqual(self.publisher.name, 'Test Publisher')

    def test_publisher_updating(self):
        self.publisher.name = 'Updated Publisher'
        self.publisher.save()
        updated_publisher = Publisher.objects.get(id=self.publisher.id)
        self.assertEqual(updated_publisher.name, 'Updated Publisher')

    def test_publisher_deletion(self):
        publisher_id = self
        self.publisher.delete()
        with self.assertRaises(Publisher.DoesNotExist):
            Publisher.objects.get(id=publisher_id)


class ReviewModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(username='testuser', email='test@example.com')
        self.platform = Platform.objects.create(name='Test Platform')
        self.genre = Genre.objects.create(name='Action')
        self.publisher = Publisher.objects.create(name='Test Publisher')
        self.developer = Developer.objects.create(name='Test Developer')
        self.game = Game.objects.create(
            title='Test Game',
            platform=self.platform,
            publisher=self.publisher,
            developer=self.developer,
            release_date='2022-01-01',
            price=Decimal('59.99'),
            description='Test Description'
        )
        self.game.genres.add(self.genre)
        self.review = Review.objects.create(
            game=self.game,
            customer=self.customer,
            rating=5,
            comment='Great game!',
        )

    def test_review_creation(self):
        self.assertEqual(self.review.game, self.game)
        self.assertEqual(self.review.customer, self.customer)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Great game!')
        self.assertIsNotNone(self.review.created_at)

    def test_review_updating(self):
        self.review.rating = 4
        self.review.comment = 'Good game!'
        self.review.save()
        updated_review = Review.objects.get(id=self.review.id)
        self.assertEqual(updated_review.rating, 4)
        self.assertEqual(updated_review.comment, 'Good game!')

    def test_review_deletion(self):
        review_id = self.review.id
        self.review.delete()
        with self.assertRaises(Review.DoesNotExist):
            Review.objects.get(id=review_id)
