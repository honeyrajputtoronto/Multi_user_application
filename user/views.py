from django.contrib.auth import get_user_model
User = get_user_model

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        
        try:
            data = request.data
            
            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            re_password = data['re_password']
            is_realtor = data['is_realtor']
            
            if is_realtor == 'True':
                is_realtor = True
            else:
                is_realtor = False
                
            if password == re_password:
                if password<=8:
                    if not User.objects.filter(email=email).exists():
                        if not is_realtor:
                            User.objects.create_user(name=name, email=email, password=password)
                            
                            return Response(
                                {'Success': 'User created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                            
                        else: 
                            User.object.create_realtor(name=name, email=email, password=password)
                            return Response(
                                {'Success': 'Realtor account created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        
                        
                    else:
                        return Response(
                            {'error': 'user with this email address already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        ) 
                    
                    
                    
                else:
                    return Response(
                        {'error': 'password must be atleast less than 8 characters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                
            else: 
                return Response(
                    {'error': 'password doesn"t matches'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            
        except:
            return Response(
                {'error': 'something went wrong when registering the account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            
            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
            
            
        except:
            return Response(
                {'error': 'something went wrong when retrieving user details'},
                statu=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    