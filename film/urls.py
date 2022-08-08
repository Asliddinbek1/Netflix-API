from django.urls import path, include


from film.views import ActorViewSet, MovieViewSet, MovieActorAPIView, CommentAPIView
from rest_framework.routers import DefaultRouter
# from rest_framework.authentication import Custo

router = DefaultRouter()
router.register('actor', ActorViewSet)
router.register('movie', MovieViewSet)
# router.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movie/<int:id>/actors/', MovieActorAPIView.as_view({'get': 'list'}) ),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:id>/', CommentAPIView.as_view()),
    
]
