from django.db import models
from django.utils import timezone
from userAccountApp.models import UserAccountRecord

# d = timezone.now()
# d
#datetime.datetime(2018, 9, 3, 7, 11, 38, 268128, tzinfo=<UTC>)
#d.today()
#timezone.now().date()
#datetime.date(2018, 9, 3)

# Create your models here.
class TransactionRecord(models.Model):
    id = models.AutoField(primary_key=True)
    mode = models.CharField(max_length=254,default="",null=True) #Cash , cheque  , Online
    amount = models.FloatField(default=0.0)
    startDate = models.DateField(max_length=50,unique=False,default=timezone.now().today())
    endDate = models.DateField(max_length=50,unique=False,default=timezone.now().today())
    comments  = models.TextField(default="")

    def __str__(self):
      return  str(self.__dict__)

class ExpenseRecord(models.Model):
    id = models.AutoField(primary_key=True)
    expense_type = models.CharField(max_length=254,default="",null=True)
    txn_info = models.ForeignKey(TransactionRecord,related_name="transaction",null=True,on_delete=models.CASCADE)

    def __str__(self):
      return  str(self.__dict__)

class ManagementTransactionRecord(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=254,default="",null=True) #deposit withdrawl
    txn_info = models.ForeignKey(TransactionRecord,related_name="deposit",null=True,on_delete=models.CASCADE)

    def __str__(self):
      return  str(self.__dict__)

# Contains all the money paid or refunded by or to tenant (Resident) .
class TenantTransactionRecord(models.Model):
    id = models.AutoField(primary_key=True)
    txn_type = models.CharField(max_length=254,default="",null=True) #deposit ,monthly rent # Refund
    txn_info = models.ForeignKey(TransactionRecord,related_name="tenantPayments",null=True,on_delete=models.CASCADE)
    tenant = models.ForeignKey(UserAccountRecord,related_name="tenant_info",null=True,on_delete=models.CASCADE)
