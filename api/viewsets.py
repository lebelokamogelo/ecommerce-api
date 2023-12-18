from rest_framework import mixins, viewsets
from products.models import Review
from .serializers import ReviewSerializer
from .permissions import OwnerBy

class ReviewViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [OwnerBy]
