from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import OrdersDataSerializers
from .models import Orders
from rest_framework import status


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def Holdings(request):
        data = Orders.objects.filter(user=request.user).values('tradingsymbol', 'exchange', 'isin','quantity', 'authorised_date','average_price', 'last_price', 'close_price', 'pnl', 'day_change', 'day_change_percentage')
        if len(data) != 0 :
            response = {
                        "status": "success",
                        "data": data
                        }
            return Response(response, status=status.HTTP_200_OK)
        if len(data) == 0:
            response = {
                        "status": "fail",
                        "message": "Data Not Avaliable"
                        }
            return Response(response, status=status.HTTP_200_OK)
        return Response({"error": "Something is wrong in data"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def Order_palce(request):
    if request.method == 'POST':
        serializer = OrdersDataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                        "status": "success",
                        "data": {
                                "message":"Order Placed Successfully",
                                "order_id": serializer.data["order_id"]
                                }
                        }
            return Response(response, status=status.HTTP_201_CREATED)
            # print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
