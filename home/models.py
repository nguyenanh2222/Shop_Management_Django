from django.db import models

# Create your models here.
class CuaHang(models.Model):
    Ten_Cua_Hang = models.CharField(max_length=500)
    Ma_Cua_Hang = models.CharField(max_length=500)
    Dia_Chi = models.CharField(max_length=500)
    Ngay_Tao = models.DateTimeField('publish date')    
# id = models.IntegerField
    def __str__(self):
        return self.Ten_Cua_Hang

class San_Pham(models.Model):
    Ten_San_Pham = models.CharField(max_length=500)
    Ma_San_Pham = models.CharField(max_length=500)
    def __str__(self):
        return self.Ten_San_Pham
    