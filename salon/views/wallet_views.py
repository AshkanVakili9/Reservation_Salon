from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from user.models import User
from salon.models import Wallet
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from salon.serializers import WalletSerializer 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wallet_balance(request):
    user = request.user
    wallet = get_object_or_404(Wallet, user_id=user.id)
    serializer = WalletSerializer(wallet, many=False)
    return Response({'payload': serializer.data}, status=200)
    


@api_view(['POST'])
def update_wallet_balance(request):
    user = request.user

    amount = int(request.data.get('amount', 0))
    wallet = get_object_or_404(Wallet, user_id=user.id)
    # Deduct or add funds to the wallet based on the sign of the amount
    if amount < 0 and wallet.balance < abs(amount):
        return Response({'error': 'Insufficient balance.'}, status=400)

    wallet.balance += amount
    wallet.save()

    return Response({'message': f'Wallet balance updated for {user.full_name}.', 'new_balance': wallet.balance})
