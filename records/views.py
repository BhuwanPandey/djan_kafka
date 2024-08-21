"""
This module defines the API views for the FaceEmbed model in the records application.

"""

from rest_framework import views
from rest_framework.pagination import PageNumberPagination

from records.models import FaceEmbed
from records.serializers import FaceEmbedSerializer


class FaceEmbedView(views.APIView):
    def get(self, request):
        items = FaceEmbed.objects.all().order_by("-id")
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Items per page
        # Paginate the queryset
        paginated_face_embeds = paginator.paginate_queryset(items, request)
        # Serialize the paginated data
        serializer = FaceEmbedSerializer(paginated_face_embeds, many=True)
        return paginator.get_paginated_response(serializer.data)
