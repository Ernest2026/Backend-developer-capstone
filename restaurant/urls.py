from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurant/booking/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]