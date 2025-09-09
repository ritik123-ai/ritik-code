from rest_framework.routers import DefaultRouter
from service.views.product_views import ProductViewSet
from service.views.cart_views import CartViewSet
from service.views.order_views import OrderViewSet
from service.views.employee_views import EmployeeAPIView
from django.urls import path

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('cart', CartViewSet, basename='cart')
router.register('orders', OrderViewSet)

urlpatterns = router.urls +[
    path('employee/', EmployeeAPIView.as_view(), name='employee'),
    path('employee/<int:pk>/', EmployeeAPIView.as_view(), name='employee-detail')
]




