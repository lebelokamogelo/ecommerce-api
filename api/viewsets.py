from rest_framework import mixins, viewsets
from products.models import Review
from .serializers import ReviewSerializer
from .permissions import OwnerBy
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [OwnerBy]
