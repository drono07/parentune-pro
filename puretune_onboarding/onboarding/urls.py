from django.urls import path, include
from rest_framework.routers import DefaultRouter
from onboarding.views import (
    ParentViewSet,
    ChildViewSet,
    BlogViewSet,
    CustomHomeFeedUpdateView,
    HomeFeedView,
)

router = DefaultRouter()
router.register(r"parents", ParentViewSet)
router.register(r"children", ChildViewSet)
router.register(r"blogs", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "update-home-feed/",
        CustomHomeFeedUpdateView.as_view(),
        name="update-home-feed",
    ),
    path("home_feed/", HomeFeedView.as_view(), name="home_feed"),
]
