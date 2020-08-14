from django.urls import path
from . import views
from .views import HomeView, PostDetailView, PostByCategory
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:pk>/', PostByCategory.as_view(), name='post_by_category'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:pk>/approve/',
         views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
    path('comment/<int:pk>/reply/', views.add_reply_to_comment,
         name='add_reply_to_comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('travel/', views.travel, name='travel'),
    path('single/', views.single, name='single'),
    path('fashion/', views.fashion, name='fashion'),
    path('newsletter/', views.news_letter, name='news-letter'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
