from django.contrib.auth.models import User, Group
from django.db.models import Avg, Count

from quickstart.models import Documents, RateDocuments
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, DocumentsSerializer, RateDocumentsSerializer, \
    MDocumentsSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = RateDocuments.objects.values('document').annotate(Avg('rate'), Count('user'))
    # qs1 = RateDocuments.objects.values('document').annotate(Avg('rate'), Count('user'))
    serializer_class = DocumentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class RateDocumentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = RateDocuments.objects.all()
    serializer_class = RateDocumentsSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def documents_list(request):
    """
        List all code snippets, or create a new snippet.
        """
    if request.method == 'GET':
        snippets = Documents.objects.all()
        serializer = MDocumentsSerializer(snippets, context={'rate': 3}, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MDocumentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
