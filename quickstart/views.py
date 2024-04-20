from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes

from .serializers import RecordSerializer
from .models import Record

from nanoid import generate


class RecordView(APIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()

    @api_view(('POST',))
    def add(request):
        record_uuid = generate(size=11)
        print(str(record_uuid))
        data = {
            'uuid': record_uuid,
            'contents': request.data.get('contents'), 
        }
        serializer = RecordSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(('GET',))
    def get(request, uuid):
        try:            
            data = Record.objects.get(uuid=uuid)
            serializer = RecordSerializer(data)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Folder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

