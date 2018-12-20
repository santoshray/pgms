from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import json
import shutil
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

from userAccountApp.models import IdentityTypeRecord,AddressRecord,PersonalInfoRecord,UserAccountRecord,IdVerificationRecord,CompanyInfoRecord,EmergencyContactRecord

# Create your views here.

def index(request):
    res_dict = {}
    return render(request,'useraccount/index.html',context=res_dict)

def register(request):
    res_dict = {}

    if request.method == "GET":
        return render(request,'useraccount/index.html',context=res_dict)

    if request.method == "POST":
        post_content = request.POST
        print(post_content)
        user_record = UserAccountRecord()
        personal_info = PersonalInfoRecord()
        personal_info.first_name = post_content['firstName']
        personal_info.last_name = post_content['lastName']
        personal_info.gender = post_content['gender']
        personal_info.middle_name = post_content['middleName']
        personal_info.email = post_content['email']
        personal_info.phone = post_content['phone']

        personal_info.save()

        permanent_address = AddressRecord()
        permanent_address.addrLine1 = post_content['permanentAddressLine1']
        permanent_address.addrLine2 = post_content['permanentAddressLine2']
        permanent_address.pincode = post_content['permanentAddressPincode']
        permanent_address.city = post_content['permanentAddressCity']
        permanent_address.state = post_content['permanentAddressState']
        permanent_address.country = post_content['permanentAddressCountry']

        permanent_address.save()

        mailing_address = AddressRecord()
        mailing_address.addrLine1 = post_content['mailingAddressLine1']
        mailing_address.addrLine2 = post_content['mailingAddressLine2']
        mailing_address.pincode = post_content['mailingAddressPincode']
        mailing_address.city = post_content['mailingAddressCity']
        mailing_address.state = post_content['mailingAddressState']
        mailing_address.country = post_content['mailingAddressCountry']

        mailing_address.save()

        user_record.userInfo = personal_info
        user_record.permanentAddress = permanent_address
        user_record.mailingAddress = mailing_address
        user_record.profilePhotolist = str([])

        user_record.save()

        folder = personal_info.first_name+'_'+personal_info.last_name+'_'+str(user_record.id)
        abs_folder = os.path.join(MEDIA_ROOT,folder)
        os.mkdir(abs_folder)

        #profilePhoto
        uploaded_file = request.FILES['picture']
        print("uploaded_file = %s"%(uploaded_file.name))
        abs_upload_file_path = os.path.join(abs_folder,uploaded_file.name)
        fs = FileSystemStorage()
        file_url = MEDIA_URL+folder+'/'+uploaded_file.name
        print(file_url)

        #fs.save(uploaded_file.name,uploaded_file)
        fs.save(uploaded_file.name,uploaded_file)
        shutil.move(os.path.join(MEDIA_ROOT,uploaded_file.name),abs_upload_file_path)
        piclist =eval(user_record.profilePhotolist)
        piclist.append(file_url)
        user_record.profilePhotolist = str(piclist)
        return render(request,'useraccount/index.html',context=res_dict)


def edit(request):
    res_dict={}
    return render(request,'useraccount/index.html',context=res_dict)


def upload(request):
    res_dict={}
    if request.method == 'POST':
        uploaded_file = request.FILES['profilephoto']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)

    return render(request,'useraccount/fileUpload.html',context=res_dict)
