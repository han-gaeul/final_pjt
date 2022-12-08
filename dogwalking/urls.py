from django.urls import path
from . import views

app_name = "dogwalking"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:dogwakling_pk>/", views.detail, name="detail"),
    path("<int:dogwakling_pk>/update/", views.update, name="update"),
    path("<int:dogwakling_pk>/delete/", views.delete, name="delete"),
    # tag
    path("tag/", views.TagCloudTV.as_view(), name="tag_cloud"),
    path("tag/<str:tag>/", views.TaggedObjectLV.as_view(), name="tagged_object_list"),
    # comment
    path(
        "<int:dogwakling_pk>/comment/create/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:dogwakling_pk>/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    # like
    path("<int:dogwalking_pk>/like/", views.like, name="like"),
    # 산책요청
    path("alarm/", views.alarm, name="alarm"),
    path("<int:pk>/send/", views.send, name="send"),
    path("alarm/<int:pk>/", views.a_detail, name="a_detail"),
    path("alarm/<int:pk>/a_delete/", views.a_delete, name="a_delete"),
]
