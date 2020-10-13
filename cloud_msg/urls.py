from rest_framework import routers
from django.conf.urls import url
from django.urls import path


# MAKE SURE TO IMPORT YOUR VIEWS
from .views import MessageViewSet, UserProfileViewSet, UserSearch

router = routers.DefaultRouter()
router.register('messages', MessageViewSet, basename='messages')
router.register('UserProfiles', UserProfileViewSet, basename='UserProfiles')
# router.register('conversations', ConversationViewSet, basename='conversations')

custom_urlpatterns = [
    # url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
    # # ?P means parameter and \d  means number/digits
    # url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', CategoryRecipes.as_view(),
    #     name='single_category_recipes')
    path(r'user_search/<str:search_string>', UserSearch.as_view(), name="user_search")
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns
