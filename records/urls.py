from django.urls import path
from records.views import FaceEmbedView


urlpatterns = [
    path('face_embed/', FaceEmbedView.as_view(),name="face-embed"),
]
