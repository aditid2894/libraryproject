from django.db import models

# Create your models here.
class Entity(models.Model):
    def __str__(self):
        return str(self.recno)
    
    recno=models.AutoField(db_column='recno', primary_key=True)
    shortguid=models.CharField(db_column='shortguid', max_length=45)
    descn=models.CharField(db_column='descn', max_length=45)
    pincode=models.CharField(db_column='pincode', max_length=25)
    address=models.CharField(db_column='address', max_length=45)
    address1=models.CharField(db_column='address1', max_length=45)
    mobile=models.CharField(db_column='mobile', max_length=10)
    email=models.CharField(db_column='email', max_length=45)
    loginid=models.CharField(db_column='loginid', max_length=45)
    pwd=models.CharField(db_column='pwd', max_length=45)
    otp=models.CharField(db_column='otp', max_length=25)
    firebasetoken=models.CharField(db_column='firebasetoken', max_length=45)
    
    class Meta:
        managed=True
        db_table='entity'
        
        