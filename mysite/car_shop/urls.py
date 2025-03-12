from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSEt, basename='user_list')
router.register(r'car/make', CarMakeViewSet, basename='car_maker_list')
router.register(r'car/model', CarModelViewSet, basename='car_model_list')
router.register(r'generation', GenerationViewSet, basename='generation_list')
router.register(r'cart', FavoriteViewSet, basename='cart_list')
router.register(r'cart/item', FavoriteItemViewSet, basename='cart_item_list')
router.register(r'review', ReviewViewSet, basename='review_list')


urlpatterns = [
    path('', include(router.urls)),
    path('car/', CarListAPIView.as_view(), name='care_list'),
    path('car/<int:pk>/', CarDetailAPIView.as_view(), name='car_detail'),
    path('car/create/', CarCreateAPIView.as_view(), name='car_create_list'),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('owner/', OwnerAPIView.as_view(), name='owner_create'),
    path('client/', ClientAPIView.as_view(), name='client_create'),
    path('owner/register/', OwnerRegisterView.as_view(), name='owner_register'),
    path('client/register', ClientRegisterView.as_view(), name='client_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]

