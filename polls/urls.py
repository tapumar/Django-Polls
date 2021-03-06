from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from .apiviews import ChoiceList, CreateVote, LoginView, PollViewSet,\
    UserCreate
from rest_framework_swagger.views import get_swagger_view
from .views import PollList, PollDetail, VoteDetail, vote

from .apps import PollsConfig

app_name = PollsConfig.name

schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('api/polls', PollViewSet, base_name='polls')

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("api", PollViewSet.as_view({'get': 'list'}), name=''),
    path(
        "api/polls/<int:pk>/choices/",
        ChoiceList.as_view(), name="choice_list"
    ),
    path(
        "api/polls/<int:pk>/choices/<int:choice_pk>/vote/",
        CreateVote.as_view(), name="create_vote"
    ),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Polls API')),
    path("", PollList.as_view(), name="polls_list"),
    path(r'polls/', PollList.as_view(), name="polls_list"),
    path(r'polls/<int:pk>/', VoteDetail.as_view(), name="polls_vote"),
    path(r'polls/<int:pk>/result', PollDetail.as_view(), name="polls_detail"),
    path('polls/<int:question_id>/vote/', vote, name='vote'),
]

urlpatterns += router.urls
