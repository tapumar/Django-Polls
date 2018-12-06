from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from .apiviews import ChoiceList, CreateVote, LoginView, PollViewSet, UserCreate
from rest_framework_swagger.views import get_swagger_view
from .views import PollList, PollDetail

schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(),
        name="create_vote"),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Polls API')),
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
]

urlpatterns += router.urls
