from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Meeting
from .serializers import MeetingSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/books",
        "GET /api/books/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def get_meetings(request):
    meetings = Meeting.objects.all()
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    serializer = MeetingSerializer(meeting, many=False)
    return Response(serializer.data)