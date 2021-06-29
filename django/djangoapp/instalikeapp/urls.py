from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:user_id>/', views.mypage, name='mypage'),
    # path('mypage/', views.mypage, name='mypage'),
    # ex: /polls/5/results/
    path('<int:user_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:user_id>/vote/', views.vote, name='vote'),
]
