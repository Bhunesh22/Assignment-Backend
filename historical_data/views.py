from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import HistoricalDataSerializers
from .models import HistoriclaData
from rest_framework import status
import datetime

# Create your views here.

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def HistoricalPriceData(request):
        from_date  = request.GET.get('from_date')
        to_date = request.GET.get('to_date')
        print(from_date, "from_date")
        print(to_date, "to_date")
        # print(datetime.date(1986, 7, 28), "time")
        if from_date == "None" and to_date == "None":
            print(1)
            data = HistoriclaData.objects.all().values("index", "price", "date", "instrument_name")
            if len(data) != 0 :
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Data Not Avaliable"}, status=status.HTTP_400_BAD_REQUEST)
        elif from_date == "None" and to_date != "None":
            print(2)
            data = HistoriclaData.objects.filter(date__date__range = (("2017-01-02"), (to_date))).values("index", "price", "date", "instrument_name")
            if len(data) != 0 :
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Data Not Avaliable"}, status=status.HTTP_400_BAD_REQUEST)
        elif from_date != "None" and to_date == "None":
            print(3)
            data = HistoriclaData.objects.filter(date__date__range = ((from_date), ("2021-12-31"))).values("index", "price", "date", "instrument_name")
            if len(data) != 0 :
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Data Not Avaliable"}, status=status.HTTP_400_BAD_REQUEST)
        elif from_date != "None" and to_date != "None":
            print(4)
            data = HistoriclaData.objects.filter(date__date__range = ((from_date), (to_date))).values("index", "price", "date", "instrument_name")
            if len(data) != 0 :
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Data Not Avaliable"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Data Not Avaliable"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def AddData(request):
    if request.method == 'POST':
        # print(request.data)
        for i in request.data:
            print(i)
            serializer = HistoricalDataSerializers(data=i)
            if serializer.is_valid():
                serializer.save()
                # print(serializer.data)
                # return Response(serializer.data, status=status.HTTP_201_CREATED)
            # print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)
        # return Response({"status": "success"}, status=status.HTTP_200_OK)
