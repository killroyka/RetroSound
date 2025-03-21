from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import OuterRef, Exists
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Favorite


class ManageFavorite:
    @action(
        detail=True,
        methods=['get'],
        url_path='favorites',
        permission_classes=[IsAuthenticated, ]
    )
    def favorite(self, request, pk):
        instance = self.get_object()
        content_type = ContentType.objects.get_for_model(instance)
        favorite_obj, created = Favorite.objects.get_or_create(
            user=request.user, content_type=content_type, object_id=instance.id
        )

        if created:
            return Response(
                {'detail': 'Content added to favorites'},
                status=status.HTTP_201_CREATED
            )
        else:
            favorite_obj.delete()
            return Response(
                {'detail': 'Content deleted to favorites'},
                status=status.HTTP_200_OK
            )

    @action(
        detail=False,
        methods=['get'],
        url_path='favorites',
        permission_classes=[IsAuthenticated, ]
    )
    def favorites(self, request):
        queryset = self.get_queryset().filter(is_favorite=True)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)
        paginator = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(paginator)

    def annotate_qs_is_favorite_field(self, queryset):
        if self.request.user.is_authenticated:
            is_favorite_subquery = Favorite.objects.filter(
                object_id=OuterRef('pk'),
                user=self.request.user,
                content_type=ContentType.objects.get_for_model(queryset.model)
            )
            queryset = queryset.annotate(is_favorite=Exists(is_favorite_subquery))
        return queryset
