from rest_framework import routers
from django.conf.urls import url


# MAKE SURE TO IMPORT YOUR VIEWS
from .views import MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet, basename='messages')
# router.register('conversations', ConversationViewSet, basename='conversations')

custom_urlpatterns = [
    # url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
    # # ?P means parameter and \d  means number/digits
    # url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', CategoryRecipes.as_view(),
    #     name='single_category_recipes')
]

urlpatterns = router.urls
# urlpatterns += custom_urlpatterns
