import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import app.routing
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": URLRouter(
        app.routing.websocket_urlpatterns +
        chat.routing.websocket_urlpatterns
    ),
})