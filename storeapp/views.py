from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from django_filters import rest_framework as filters
from django_property_filter import PropertyFilterSet, PropertyNumberFilter
from .models import Box
from .serializers import BoxSerializer, ListBoxesSerializer, ListBoxesStaffSerializer
from rest_framework.response import Response
from rest_framework import status
    
class MyBoxFilter(PropertyFilterSet):
    class Meta:
        model = Box
        fields = {
            'length': ['lt', 'gt'],
            'breadth': ['lt', 'gt'],
            'height': ['lt', 'gt'],
        }
        property_fields = [
            ('area', PropertyNumberFilter, ['lt','gt']),
            ('volume', PropertyNumberFilter, ['lt','gt']),
        ]

class BoxFilter(MyBoxFilter):
    MyBoxFilter.Meta.fields = {
            'length': ['lt', 'gt'],
            'breadth': ['lt', 'gt'],
            'height': ['lt', 'gt'],
            'created_at': ['lt','gt'],
            'creator': ['exact'],
        }

class CreateBoxAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UpdateBoxAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class AllBoxes(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Box.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BoxFilter
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ListBoxesStaffSerializer
        return ListBoxesSerializer

class MyBoxes(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ListBoxesStaffSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MyBoxFilter

    def get_queryset(self):
        queryset = Box.objects.filter(creator=self.request.user)
        return queryset

class DeleteBox(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN) 
        return Response(status=status.HTTP_204_NO_CONTENT)

