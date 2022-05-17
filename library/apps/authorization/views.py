from django.shortcuts import render
from django.db import models 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from apps.utils import dictfetchall as dictfetchall, write_logs_error 

class Login(APIView):
    def post(self, request):
        try:
            request_data=request.data 
            email=request_data['email']
            pwd=request_data['pwd']
            
            getentity=f"select * from entity where email='{email}'"
            with connection.cursor() as c:
                c.execute(getentity)
                row=dictfetchall(c)
                if len(row)>0:
                    entityrecno=row[0]['recno']
                    getmember=f"select recno from member where entityrecno={entityrecno} order by recno desc limit 1"
                    with connection.cursor() as c:
                        c.execute(getmember)
                        memberdata=dictfetchall(c)
                        if len(memberdata)>0:
                            memberRecno=memberdata[0]['recno']
                            row[0]['memberrecno']=memberRecno
                    user= row[0]
                    if user['pwd']==pwd:
                        return Response({"Success":True, "Message": row[0]}, status=200)
                    else:
                        raise Exception ('Email and password do not match')
                else:
                    raise Exception("No records found for this email try to register again!")
            
            
        except Exception as err:
            import os
            import sys
            exc_type, exc_obj, exc_tb=sys.exc_info()
            fname=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            write_logs_error('Entity delete method', request.data, str(err), exc_tb.tb_lineno)
            return Response ({"Success":False, "Message":str(err)}, status=200)