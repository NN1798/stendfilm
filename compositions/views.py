from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .services.service_views import get_last_comment, check_comment_frequency, CompositionFilter

from .models import Composition, Rating, Comment
from .serializers import CompositionSerializer, CreateRatingSerializer, CommentSerializer
from .permissions import IsStaff


class CompositionModelViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    permission_classes = [
        IsStaff,
    ]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CompositionFilter
    search_fields = ['title']


class RatingCreateAPIView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            last_comment = get_last_comment(
                request.user.id, self.get_queryset()
            )
            last_comment_time = last_comment.created_at if last_comment else None

            if last_comment_time is not None and not check_comment_frequency(last_comment_time):
                return Response({'error': 'Слишком частые комментарии.'}, status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
