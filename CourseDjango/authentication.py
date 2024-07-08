from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

User = get_user_model()


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-Key')  # Получаем API ключ из заголовка запроса

        if not api_key:
            return None  # Если API ключ отсутствует, возвращаем None

        if api_key != 'your_predefined_api_key':
            raise AuthenticationFailed('Invalid API key')

        user = AnonymousUser()
        user.username = 'api_user'
        user.is_authenticated = True

        return (user, None)
