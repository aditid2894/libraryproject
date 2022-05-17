from django.shortcuts import render 
from django.db import models 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.utils import dictfetchall as dictfetchall, write_logs_error 
from apps.entity.models import Entity
from apps.entity.serializers import EntitySerializer
# Create your views here.

class EntityCrud(APIView):
    def get (self, request, recno=None):
        try:
            if recno:
                entity=Entity.objects.get(recno=recno)
                entity=EntitySerializer(entity).data 
            else:
                entity=Entity.objects.all()
                entity=EntitySerializer(entity, many=True).data
            return Response ({"Success":True, "Message":entity}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Entity get method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def post(self, request):
        try:
            request_data=request.data 
            entity_obj=Entity.objects.create(
                shortguid=request_data['shortguid'],
                descn=request_data.get('descn'),
                address=request_data.get('address'),
                address1=request_data.get('address1'),
                pincode=request_data.get('pincode'),
                mobile=request_data.get('mobile'),
                loginid=request_data.get('loginid'),
                email=request_data.get('email'),
                pwd=request_data.get('pwd'),
                otp=request_data.get('otp'),
                firebasetoken=request_data.get('firebasetoken')
            )
            
            message="Enity Added Successfully"
            return Response ({"Success":True, "Message":message}, status=200)
    
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Entity post method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def patch(self, request):
        try:
            request_data=request.data 
            recno=request_data['recno']
            
            try:
                entity_obj=Entity.objects.get(recno=recno)
            except:
                raise Exception("Entity Not Found")
            
            
            descn=request_data.get('descn', entity_obj.descn)
            address=request_data.get('address', entity_obj.address)
            address1=request_data.get('address1', entity_obj.address1)
            pincode=request_data.get('pincode', entity_obj.pincode)
            mobile=request_data.get('mobile', entity_obj.mobile)
            email=request_data.get('email', entity_obj.email)
            loginid=request_data.get('loginid', entity_obj.loginid)
            
            
            entity_obj.descn=descn
            entity_obj.address=address
            entity_obj.address1=address1 
            entity_obj.pincode=pincode
            entity_obj.mobile=mobile
            entity_obj.email=email
            entity_obj.loginid=loginid
            entity_obj.save()
            
            resp=EntitySerializer(entity_obj).data
            return Response ({"Success":True, "Message":resp}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Entity patch method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def delete(self, request):
        try:
                request_data=request.data 
                recno=request_data['recno']
                
                try:
                    entity_obj=Entity.objects.get(recno=recno)
                except:
                    raise Exception("Entity Not Found")
                
                entity_obj.active=False
                entity_obj.save()
                
                message="Entity Deleted Successfully"
                
                return Response ({"Success":True, "Message":message}, status=200)
    
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Entity delete method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
        
        