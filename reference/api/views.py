from rest_framework import generics, mixins, permissions
from ..models import Reference
from .serializers import ReferenceSerializer
from .permissions import IsAuthorOrReadOnly

class ReferenceListView(generics.ListCreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    #permission----
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)

class ReferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    #permission----
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()