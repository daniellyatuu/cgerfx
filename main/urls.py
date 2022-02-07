from django.urls import path
from . import views

app_name='main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('learn-more-deriv/', views.LearnMoreDerivView.as_view(), name='learn_more_deriv'),
    path('learn-more-xm/', views.LearnMoreXMView.as_view(), name='learn_more_xm'),
    path('beginner-guide/', views.BeginnerGuideView.as_view(), name='beginner_guide'),
    path('trader-must-read/', views.TraderMustReadView.as_view(), name='trader_must_read'),
    path('broker-list/', views.BrokerListView.as_view(), name='broker_list'),
    path('forex-documents/', views.ForexDocumentsListView.as_view(), name='forex_documents'),
    path('blog-post/', views.BlogPostListView.as_view(), name='blog_post'),
    path('tutorial-video-list/', views.TutorialVideoListView.as_view(), name='tutorial_video_list'),
]
