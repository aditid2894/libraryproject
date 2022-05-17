from django.shortcuts import render 
from django.db import models 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.utils import dictfetchall as dictfetchall, write_logs_error 
from apps.bookmaster.models import Bookmaster
from apps.bookmaster.serializers import BookmasterSerializer 
from datetime import datetime
from django.db import connection

# Create your views here.

class BookmasterCrud(APIView):
    def get (self, request, recno=None):
        try:
            if recno:
                bookmaster=Bookmaster.objects.get(recno=recno)
                bookmaster=BookmasterSerializer(bookmaster).data 
            else:
                bookmaster=Bookmaster.objects.all()
                bookmaster=BookmasterSerializer(bookmaster, many=True).data
            return Response ({"Success":True, "Message":bookmaster}, status=200)
        
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Bookmaster get method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def post(self, request):
        try:
            request_data=request.data 
            owner=request_data.get('owner')
            memberrecno=request_data.get('memberrecno')
            gifted=request_data.get('gifted', False)
            booktitle=request_data.get('booktitle')
            booksubject=request_data.get('booksubject')
            bookdetails=request_data.get('bookdetails')
            bookauthor=request_data.get('bookauthor')
            trdate=request_data.get('trdate', datetime.now().strftime("%Y%m%d"))
            readcount=request_data.get('readcount')
            requestcount=request_data.get('requestcount')
            status=request_data.get('status')
            image=request_data.get('image', None)
            rating=request_data.get('rating')
            active=request_data.get('active')
        
            addbook=f"INSERT INTO bookmaster(owner, memberrecno, gifted, booktitle, bookauthor, booksubject, bookdetails, readcount, requestcount, trdate, status, rating, image, active) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            with connection.cursor() as c:
                c.execute(addbook, [owner, memberrecno, gifted, booktitle, bookauthor, booksubject, bookdetails, readcount, requestcount, trdate, status, rating, image, active])
                
            
            message="Bookmaster Registered Successfully"
            return Response ({"Success":True, "Message":message}, status=200)
    
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Bookmaster post method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def patch(self, request):
        try:
            request_data=request.data 
            recno=request_data['recno']
            
            try:
                bookmaster_obj=Bookmaster.objects.get(recno=recno)
            except:
                raise Exception("Bookmaster Not Found")
            
            
            owner=request_data.get('owner', bookmaster_obj.owner)
            memberrecno=request_data.get('memberrecno', bookmaster_obj.memberrecno)
            gifted=request_data.get('gifted', bookmaster_obj.gifted)
            booktitle=request_data.get('booktitle', bookmaster_obj.booktitle)
            bookauthor=request_data.get('bookauthor', bookmaster_obj.bookauthor)
            booksubject=request_data.get('booksubject', bookmaster_obj.booksubject)
            bookdetails=request_data.get('bookdetails', bookmaster_obj.bookdetails)
            trdate=request_data.get('trdate', bookmaster_obj.trdate)
            readcount=request_data.get('readcount', bookmaster_obj.readcount)
            requestcount=request_data.get('requestcount', bookmaster_obj.requestcount)
            status=request_data.get('status', bookmaster_obj.status)
            rating=request_data.get('rating', bookmaster_obj.rating)
            active=request_data.get('active', bookmaster_obj.active)
         
            
            bookmaster_obj.owner=owner
            bookmaster_obj.gifted=gifted
            bookmaster_obj.booktitle=booktitle
            bookmaster_obj.bookauthor=bookauthor
            bookmaster_obj.booksubject=booksubject
            bookmaster_obj.bookdetails=bookdetails
            bookmaster_obj.trdate=trdate
            bookmaster_obj.readcount=readcount
            bookmaster_obj.requestcount=requestcount
            bookmaster_obj.status=status
            bookmaster_obj.rating=rating
            bookmaster_obj.memberrecno=memberrecno
            bookmaster_obj.active=active
            bookmaster_obj.save()
            
            resp=BookmasterSerializer(bookmaster_obj).data
            return Response ({"Success":True, "Message":resp}, status=200)

        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Bookmaster patch method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)
        
    def delete(self, request):
        try:
                request_data=request.data 
                recno=request_data['recno']
                
                try:
                    bookmaster_obj=Bookmaster.objects.get(recno=recno)
                except:
                    raise Exception("Bookmaster Not Found")
                
                bookmaster_obj.active=False
                bookmaster_obj.save()
                
                message="Bookmaster Deleted Successfully"
                
                return Response ({"Success":True, "Message":message}, status=200)
    
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Bookmaster delete method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)