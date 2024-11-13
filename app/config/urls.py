from django.urls import include, path
from rest_framework import routers

from common import views as common_views
from desk.views import ReportDeskViewSet
from report.views import ReportViewSet
from staff.views import StaffViewSet
from user import views as user_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'groups', user_views.GroupViewSet)
router.register(r'permissions', user_views.PermissionViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'desks', ReportDeskViewSet)
router.register(r'tags', common_views.TagViewSet)
router.register(r'categories', common_views.CategoryViewSet)
router.register(r'attachments', common_views.AttachmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', user_views.RegisterView.as_view(), name='register'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
