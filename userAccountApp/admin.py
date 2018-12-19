from django.contrib import admin
from userAccountApp.models import IdentityTypeRecord,AddressRecord,PersonalInfoRecord,UserAccountRecord,IdVerificationRecord,CompanyInfoRecord,EmergencyContactRecord
# Register your models here.

admin.site.register(IdentityTypeRecord)
admin.site.register(AddressRecord)
admin.site.register(PersonalInfoRecord)
admin.site.register(UserAccountRecord)
admin.site.register(IdVerificationRecord)
admin.site.register(CompanyInfoRecord)
admin.site.register(EmergencyContactRecord)
