from salon.models import *
from salon.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def addSiteReview(request):
    user = request.user
    data = request.data.copy()
    data['user'] = user.id
    serializer = SiteReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Successful, Site Review added."}, status=201)
    return Response({"message": "Failed", "payload": serializer.errors}, status=400)
