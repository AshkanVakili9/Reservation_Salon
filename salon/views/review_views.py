from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from salon.models import Court
from salon.models import Review
from salon.serializers import ReviewSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated



@api_view(['GET'])
def getReviewByCourtId(request, court_id):
    data = Review.objects.filter(court=court_id).all()
    serializer = ReviewSerializer(data, many=True)
    return Response(serializer.data, status=200)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addReview(request, court_id):
    user = request.user
    court = get_object_or_404(Court, id=court_id)
    
    data = request.data
    
    # (1) Review already exists
    alreadyExists = court.review_set.filter(user=user).exists()
   
    if alreadyExists:
        content = {"detail": "Review already exists"}
        return Response(content, status=400)

    # (2) No rating or 0
    elif data["rating"] == 0:
        content = {"detail": "please select a rating between 1 to 5"}
        return Response(content, status=400)

    # (3) create a Review
    else:
        review = Review.objects.create(
            user=user,
            court=court,
            name=data["name"],
            rating=data["rating"],
            comment=data["comment"],
        )

    reviews = court.review_set.all()
    court.numReviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating

    court.rating = total / len(reviews)
    court.save()

    return Response("Review Added ")




@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def getReview(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            court = get_object_or_404(Review, pk=pk)
            serializer = ReviewSerializer(court)
            return Response(serializer.data)
        else:
            courts = Review.objects.all()
            serializer = ReviewSerializer(courts, many=True)
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        court = get_object_or_404(Review, pk=pk)
        court.delete()
        return Response({"detail": "Delete Successful."},status=status.HTTP_204_NO_CONTENT)
