from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('broker-list/', views.BrokerListView.as_view(), name='broker_list'),
    path('forex-documents/', views.ForexDocumentsListView.as_view(), name='forex_documents'),
    path('blog-post/', views.BlogPostListView.as_view(), name='blog_post'),
    path('tutorial-video-list/', views.TutorialVideoListView.as_view(), name='tutorial_video_list'),
]
