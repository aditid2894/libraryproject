from datetime import datetime




def write_logs_error(apiName, data, err, lineno):
    now=datetime.now()
    dt_string= now.strftime("%d/%m/%Y  %H:%M:%S")
    date=now.strftime("%d%m%Y")
    f= open (f"./Logs/custom{date}.log", "a")
    f.writelines([f'\n \n ERROR at {apiName} at : {dt_string} \n', f'Request Data : {data} \n', f'ERROR is {err} at {lineno}' ])
    f.close()
    
    
def dictfetchall(cursor):
    columns= [col[0] for col in cursor.description]
    
    return[
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]