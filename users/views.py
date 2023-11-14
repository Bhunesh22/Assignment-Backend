# from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
# from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import User
# from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated ])
def user_data(request):
    serializer = UserSerializer(request.user)
    user = {}
    data = serializer.data
    if len(data) != 0:
        user['user_id'] = data['id']
        user['email'] = data['email']
        user['user_name'] = data['user_name']
        user['user_type'] = data['user_type']
        user['broker'] = data['broker']
        response = {"status": "success","data": user}
        return Response(response, status=status.HTTP_200_OK)
    return Response({"status":"failed"}, status=status.HTTP_400_BAD_REQUEST)


## --------------------------------------------------##
## User Registeration
@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def RegisterUser(request):
    if request.method == 'POST':
        # user_serializer = {
        #     'email': request.data['email'],
        #     'password': request.data['password'],
        #     'user_name': request.data['user_name'],
        #     'user_type': request.data['user_type'],
        #     'broker': request.data['broker'],
        # }
        check_if_user_exists = CheckUserExists(request.data['email'])
        if len(check_if_user_exists) == 0:
            serializer = UserCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            response = {'message': 'User with this email is already exist'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        response = {'message': 'Invalid Input Data', 'error': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

def CheckUserExists(email):
    userdata = User.objects.filter(email=email).values()
    return userdata

def get_tokens_for_user(user):
       refresh = RefreshToken.for_user(user)
       return {
              "refresh": str(refresh),
              "access": str(refresh.access_token)
              }


@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        user_detail = UserSerializer(user).data
        print(user_detail)
        if user is not None:
            res_data = get_tokens_for_user(User.objects.get(email=email))
            response = {
                        "status": status.HTTP_200_OK,
                        "message": "success",
                        "user_id": user_detail['id'],
                        "data": res_data
                        }
            return Response(response, status = status.HTTP_200_OK)
        else :
            response = {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": "Invalid Email or Password",
                    }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)