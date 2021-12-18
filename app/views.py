from django.db.models.query import QuerySet
from .models import *
from .serializer import *
from rest_framework import generics ,viewsets
from rest_framework import permissions
from .permissions import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q


class TasksViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerilizer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner = user)
    


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(owner = user)
    
  
class CategoryDetailUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = CategorySerilizer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(owner = user)

class CategoryDelete(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()   #Category.objects.all()
        if self.request.user.is_superuser:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskStatus(APIView):
    def get(self,request,*args, **kwargs):
        user = self.request.user
        Done = Task.objects.filter(Q(status="Done") & Q(owner = user))
        Working = Task.objects.filter(Q(status="Working") & Q(owner = user))
        Incomplete = Task.objects.filter(Q(status="Incomplete") & Q(owner = user))
        serializer_Done = TaskSerilizer(Done,many=True,context={'request': request})
        serializer_Working = TaskSerilizer(Working,many=True,context={'request': request})
        serializer_Incomplete = TaskSerilizer(Incomplete,many=True,context={'request': request})
        return Response({'tasks': [{'Done' : serializer_Done.data},{'Working':serializer_Working.data},{'Incomplete':serializer_Incomplete.data}]})

    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
