from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from poll import views as poll_views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
   
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('<int:id>/',views.detail_view,name='detail'),
    path('vote/<poll_id>/',poll_views.vote,name='vote'),
    path('results/<poll_id>/',poll_views.results,name='results'),
    path('create/',poll_views.create,name='create'),
    path('poll/',poll_views.home,name='home'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)