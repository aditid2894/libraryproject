from django.shortcuts import render 
from django.db import models 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.utils import dictfetchall as dictfetchall, write_logs_error 
from apps.member.models import Member
from apps.member.serializers import MemberSerializer 
from datetime import datetime

# Create your views here.

class MemberCrud(APIView):
    def get (self, request, recno=None):
        try:
            if recno:
                mem=Member.objects.get(recno=recno)
                mem=MemberSerializer(mem).data 
            else:
                mem=Member.objects.all()
                mem=MemberSerializer(mem, many=True).data
            return Response ({"Success":True, "Message":mem}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Member get method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def post(self, request):
        try:
            request_data=request.data 
            mem_obj=Member.objects.create(
                entityrecno=request_data['entityrecno'],
                dateofjoin=request_data.get('dateofjoin', datetime.now().strftime("%Y%m%d")),
                noofbooks=request_data.get('noofbooks'),
                noofbooksstored=request_data.get('noofbooksstored'),
                active=request_data.get('active'),
               
            )
            
            message="Member Registered Successfully"
            return Response ({"Success":True, "Message":message}, status=200)
    
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Member post method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def patch(self, request):
        try:
            request_data=request.data 
            recno=request_data['recno']
            
            try:
                mem_obj=Member.objects.get(recno=recno)
            except:
                raise Exception("Member Not Found")
            
            
            entityrecno=request_data.get('entityrecno', mem_obj.entityrecno)
            dateofjoin=request_data.get('dateofjoin', mem_obj.dateofjoin)
            noofbooks=request_data.get('noofbooks', mem_obj.noofbooks)
            noofbooksstrored=request_data.get('noofbooksstrored', mem_obj.noofbooksstrored)
            active=request_data.get('active', mem_obj.active)
         
            
            mem_obj.entityrecno=entityrecno
            mem_obj.dateofjoin=dateofjoin
            mem_obj.noofbooks=noofbooks 
            mem_obj.noofbooksstrored=noofbooksstrored
            mem_obj.active=active
            mem_obj.save()
            
            resp=MemberSerializer(mem_obj).data
            return Response ({"Success":True, "Message":resp}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Member patch method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def delete(self, request):
        try:
                request_data=request.data 
                recno=request_data['recno']
                
                try:
                    mem_obj=Member.objects.get(recno=recno)
                except:
                    raise Exception("Member Not Found")
                
                mem_obj.active=False
                mem_obj.save()
                
                message="Member Deleted Successfully"
                
                return Response ({"Success":True, "Message":message}, status=200)
    
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Member delete method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)