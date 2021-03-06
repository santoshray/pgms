from django.db import models

# Create your models here.

class IdentityTypeRecord(models.Model):
    id = models.AutoField(primary_key=True)
    docType = models.CharField(max_length=200,default="",null=True)

    def __str__(self):
        return  str(self.__dict__)

class AddressRecord(models.Model):
    id = models.AutoField(primary_key=True)
    addrLine1 = models.CharField(max_length=200,default="",null=True)
    addrLine2 = models.CharField(max_length=200,default="",null=True)
    pincode = models.CharField(max_length=10,default="",null=True)
    city = models.CharField(max_length=100,default="",null=True)
    state = models.CharField(max_length=100,default="",null=True)
    country = models.CharField(max_length=100,default="",null=True)

    def __str__(self):
        return  str(self.__dict__)


class IdVerificationRecord(models.Model):
    id = models.AutoField(primary_key=True)
    idType = models.ForeignKey(IdentityTypeRecord ,related_name="identityType",null=True,on_delete=models.CASCADE)
    idDocsURLlist = models.TextField(default='[]') #empty list converted to string
    #doclsit is an array of objects where each object has info {"type":"Passport","url":"/media/...","id_num":"345A.."}


    def __str__(self):
      return  str(self.__dict__)

class CompanyInfoRecord(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=254,default="",null=True)
    companyAddress = models.ForeignKey(AddressRecord,related_name="companyAddress",null=True,on_delete=models.CASCADE)

    def __str__(self):
      return  str(self.__dict__)

class PersonalInfoRecord(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=254,default="",null=True)
    last_name  = models.CharField(max_length=254,default="",null=True)
    middle_name = models.CharField(max_length=254,default="",null=True)
    email = models.EmailField(max_length=254,default="",null=True)
    gender = models.CharField(max_length=254,default="",null=True)
    phone = models.CharField(max_length=20,default="",null=True)

    def __str__(self):
      return  str(self.__dict__)


class EmergencyContactRecord(models.Model):
    id = models.AutoField(primary_key=True)
    contactInfo1 = models.ForeignKey(PersonalInfoRecord,related_name="emergencyInfo1",null=True,on_delete=models.CASCADE)
    contactAddress1 = models.ForeignKey(AddressRecord,related_name="emergencyAddress1",null=True,on_delete=models.CASCADE)
    relationship1 = models.CharField(max_length=254,default="nothing",null=True)
    contactInfo2 = models.ForeignKey(PersonalInfoRecord,related_name="emergencyInfo2",null=True,on_delete=models.CASCADE)
    contactAddress1 = models.ForeignKey(AddressRecord,related_name="emergencyAddress2",null=True,on_delete=models.CASCADE)
    relationship2 = models.CharField(max_length=254,default="",null=True)

    def __str__(self):
      return  str(self.__dict__)


class UserAccountRecord(models.Model):
    id = models.AutoField(primary_key=True)
    userInfo = models.ForeignKey(PersonalInfoRecord,related_name="userInfo",null=True,on_delete=models.CASCADE)
    permanentAddress = models.ForeignKey(AddressRecord,related_name="permanentAddress",null=True,on_delete=models.CASCADE)
    mailingAddress = models.ForeignKey(AddressRecord,related_name="mailingAddress",null=True,on_delete=models.CASCADE)
#    profilePhoto = models.FileField(upload_to='profile_pics/', default='profile_pics/None/no-img.jpg' )
    profilePhotolist = models.TextField(default='[]')
    idVerificationInfo = models.ForeignKey(IdVerificationRecord,related_name="idVerification",null=True,on_delete=models.CASCADE)
    companyInfo = models.ForeignKey(CompanyInfoRecord,related_name="companyInfo",null=True,on_delete=models.CASCADE)
    emergencyContactInfo = models.ForeignKey(EmergencyContactRecord,related_name="emergencyContactInfo",null=True,on_delete=models.CASCADE)
    occupation = models.CharField(max_length=254,default="occupation",null=True)

    def __str__(self):
      return  str(self.__dict__)
