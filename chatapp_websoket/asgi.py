# import os
#
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp_websoket.settings")
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()
#
# import chat.routing
#
# application = ProtocolTypeRouter({
#   "http": django_asgi_app,
#   "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 chat.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })


import os
import django
from channels.http import AsgiHandler
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp_websoket.settings')
django.setup()
from channels.auth import AuthMiddlewareStack

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})

#
#
# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp_websoket.settings')
#
# application = get_asgi_application()

