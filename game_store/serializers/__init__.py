from game_store.serializers.customer import CustomerSerializer
from game_store.serializers.developer import DeveloperSerializer
from game_store.serializers.discount import DiscountSerializer
from game_store.serializers.game import GameSerializer
from game_store.serializers.genre import GenreSerializer
from game_store.serializers.inventory import InventorySerializer
from game_store.serializers.order import OrderSerializer
from game_store.serializers.platform import PlatformSerializer
from game_store.serializers.publisher import PublisherSerializer
from game_store.serializers.review import ReviewSerializer

__all__ = [
    'CustomerSerializer', 'DeveloperSerializer', 'GameSerializer', 'GenreSerializer', 'InventorySerializer',
    'OrderSerializer',
    'PlatformSerializer', 'PublisherSerializer', 'ReviewSerializer',
]
