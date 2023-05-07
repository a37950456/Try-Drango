from django.urls import path, re_path # url
from .views import (
    blog_post_list_view,
    blog_post_detial_view,
    blog_post_update_view,
    blog_post_delete_view
    )

urlpatterns = [
    path('', blog_post_list_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
    re_path(r'^(?P<slug>\w+)/$', blog_post_detial_view)
]