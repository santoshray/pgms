from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import json
import shutil
from importlib import import_module
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore

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
        if post_content['infotype'] == 'profile':
            res_dict = pgms_add_profile_info(request)

        if(post_content['infotype'] == 'idverification'):
            res_dict = pgms_add_idverification_info(request)

        if(post_content['infotype'] == 'company'):
            res_dict = pgms_add_company_info(request)

        if(post_content['infotype'] == 'emergency_contact'):
            res_dict = pgms_add_emergency_contact_info(request)

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

def residentlist(request):
    res_dict={}

    user_record  =  UserAccountRecord.objects.get(pk=21)
    print(user_record)
    if user_record:
        res_dict["status"] = "NO_ERROR"
        res_dict["payload"] = {}
        res_dict["payload"]["user_record"] = user_record
#        res_dict["payload"]["profilephoto"] =

        print(eval(user_record.profilePhotolist))


    return render(request,'useraccount/residentlist.html',context=res_dict)


def pgms_add_profile_info(request):

    res_dict = {}

    print("FUNCTION : pgms_add_profile_info called")

    if request.method == "POST":
        post_content = request.POST

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

    res_dict["status"] = "NO_ERROR"
    res_dict["payload"] = {}
    res_dict["payload"]["id"] = user_record.id
    res_dict["payload"]["email"] = personal_info.email
    print(res_dict)
    return res_dict


def pgms_add_idverification_info(request):
    res_dict = {}
    print("FUNCTION : pgms_add_idverification_info called")

    if request.method == "POST":
        post_content = request.POST
        print(post_content)
        user_record = UserAccountRecord.objects.get(userInfo__email=post_content['email'],pk=int(post_content["id"]))
        print("user_record.userInfo::")
        print(user_record.userInfo)
        if user_record:
            idVerification_record = IdVerificationRecord()
            idtype_record =IdentityTypeRecord()
            idtype_record.docType = post_content["idType"]
            idtype_record.save()
            idVerification_record.idType = idtype_record
            idVerification_record.idDocsURLlist  = '[]'
            idVerification_record.save()

        user_record.idVerificationInfo = idVerification_record
        user_record.save()

    res_dict["status"] = "NO_ERROR"
    res_dict["payload"]={}
    res_dict["payload"]["email"] = post_content['email']
    res_dict["payload"]["id"] = user_record.id
    return res_dict

def pgms_add_company_info(request):
    res_dict = {}
    print("FUNCTION : pgms_add_company_info called")

    if request.method == "POST":
        post_content = request.POST
        user_record = UserAccountRecord.objects.get(userInfo__email=post_content['email'],pk=int(post_content["id"]))
        print("user_record.userInfo::\n\n")
        print(user_record.userInfo)
        if user_record:
            company_record = CompanyInfoRecord()
            company_address_record =AddressRecord()
            company_address_record.addrLine1 = post_content["companyAddressLine1"]
            company_address_record.addrLine2 = post_content["companyAddressLine2"]
            company_address_record.pincode =post_content["companyPincode"]
            company_address_record.city = post_content["companyCity"]
            company_address_record.state =post_content["companyState"]
            company_address_record.country =post_content["companyCountry"]
            company_address_record.save()
            company_record.companyName = post_content["companyName"]
            company_record.companyAddress = company_address_record
            company_record.save()
            user_record.companyInfo = company_record
            user_record.occupation = post_content["occupation"]
            user_record.save()

            res_dict["status"] = "NO_ERROR"
            res_dict["status_string"] = ["Company Information saved successfully"]
            res_dict["payload"]={}
            res_dict["payload"]["email"] = post_content['email']
            res_dict["payload"]["id"] = user_record.id
        else :
            res_dict["status"] = "ERROR"
            res_dict["status_string"] = ["User not found. Please register"]
            res_dict["payload"]={}

        return res_dict

def pgms_add_emergency_contact_info(request):
    res_dict = {}
    print("FUNCTION : pgms_add_emergency_contact_info called")

    if request.method == "POST":
        post_content = request.POST
        user_record = UserAccountRecord.objects.get(userInfo__email=post_content['email'],pk=int(post_content["id"]))
        print("user_record.userInfo::\n\n")
        print(user_record.userInfo)
        if user_record:
            ec1_record = EmergencyContactRecord()
            ec1_address =AddressRecord()
            ec1_address.addrLine1 = post_content["ec1Line1"]
            ec1_address.addrLine2 = post_content["ec1Line2"]
            ec1_address.pincode =post_content["ec1Pincode"]
            ec1_address.city = post_content["ec1City"]
            ec1_address.state =post_content["ec1State"]
            ec1_address.country =post_content["ec1Country"]
            ec1_address.save()
            ec1_contact = PersonalInfoRecord()
            ec1_contact.first_name = post_content["ec1firstName"]
            ec1_contact.last_name = post_content["ec1lastName"]
            ec1_contact.middle_name = post_content["ec1middleName"]
            ec1_contact.email = post_content["ec1email"]
            ec1_contact.gender = post_content["ec1gender"]
            ec1_contact.phone = post_content["ec1phone"]
            ec1_contact.save()

            ec1_record.relationship1 = post_content["ec1Relationship"]
            ec1_record.contactInfo1 = ec1_contact
            ec1_record.contactAddress1 = ec1_address
            ec1_record.save()
            user_record.emergencyContactInfo = ec1_record
            user_record.save()

            res_dict["status"] = "NO_ERROR"
            res_dict["status_string"] = ["Emergency Contact Info saved successfully"]
            res_dict["payload"]={}
            res_dict["payload"]["email"] = post_content['email']
            res_dict["payload"]["id"] = user_record.id
        else :
            res_dict["status"] = "ERROR"
            res_dict["status_string"] = ["User not found. Please register"]
            res_dict["payload"]={}

        return res_dict
