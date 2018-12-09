from django.db import models

# Create your models here.

class IdentityTypeRecord(models.Model):
    id = models.AutoField(primary_key=True)
    docType = models.CharField(max_length=200,default="nothing",null=True)

    def __str__(self):
        return  str(self.__dict__)


class AddressRecord(models.Model):
    id = models.AutoField(primary_key=True)
    addrLine1 = models.CharField(max_length=200,default="nothing",null=True)
    addrLine2 = models.CharField(max_length=200,default="nothing",null=True)
    pincode = models.CharField(max_length=10,default="nothing",null=True)
    state = models.CharField(max_length=100,default="nothing",null=True)
    country = models.CharField(max_length=100,default="nothing",null=True)

    def __str__(self):
        return  str(self.__dict__)



class UserAccountRecord(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=254,default="nothing",null=True)
    last_name  = models.CharField(max_length=254,default="nothing",null=True)
    middle_name = models.CharField(max_length=254,default="nothing",null=True)
    email = models.EmailField(max_length=254,null=True)
    phone = models.CharField(max_length=20,default="99999999",null=True)
    permanentAddress = models.ForeignKey(AddressRecord,related_name="permanentAddress",null=True)
    mailingAddress = models.ForeignKey(AddressRecord,related_name="mailingAddress",null=True)
    profilePhoto = models.FileField(upload_to='profile_pics/', default='profile_pics/None/no-img.jpg' )
    idType = models.ForeignKey(IdentityTypeRecord ,related_name="identityType",null=True)
    idDocs = models.FileField(upload_to='profile_data/', default='profile_data/None/file' )


    def __str__(self):
      return  str(self.__dict__)
