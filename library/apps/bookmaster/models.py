from django.db import models

# Create your models here.
class Bookmaster(models.Model):
    def __str__(self):
        return str(self.recno)
    
    recno=models.AutoField(db_column='recno', primary_key=True)
    owner=models.IntegerField(db_column='owner')
    memberrecno=models.IntegerField(db_column='memberrecno')
    gifted=models.BooleanField(db_column='gifted', default=False)
    booktitle=models.CharField(db_column='booktitle', max_length=255)
    bookauthor=models.CharField(db_column='bookauthor', max_length=50)
    booksubject=models.CharField(db_column='booksubject', max_length=45)
    bookdetails=models.CharField(db_column='bookdetails', max_length=1000)
    trdate=models.IntegerField(db_column='trdate')
    readcount=models.IntegerField(db_column='readcount')
    requestcount=models.IntegerField(db_column='requestcount')
    status=models.CharField(db_column='status', max_length=5)
    image=models.BinaryField(db_column='image')
    rating=models.IntegerField(db_column='rating')
    active=models.BooleanField(db_column='active', default=True)
    

    
    class Meta:
        managed=True
        db_table='bookmaster'
        
        