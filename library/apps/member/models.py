from django.db import models

# Create your models here.
class Member(models.Model):
    def __str__(self):
        return str(self.recno)
    
    recno=models.AutoField(db_column='recno', primary_key=True)
    entityrecno=models.IntegerField(db_column='entityrecno')
    dateofjoin=models.IntegerField(db_column='dateofjoin')
    noofbooks=models.IntegerField(db_column='noofbooks')
    noofbooksstored=models.IntegerField(db_column='noofbooksstored')
    active=models.BooleanField(db_column='active', default=True)
    

    
    class Meta:
        managed=True
        db_table='member'
        
        