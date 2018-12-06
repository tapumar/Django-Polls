from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import ChoiceList, CreateVote, LoginView, PollViewSet, UserCreate

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(),
        name="create_vote"),
]

urlpatterns += router.urls
