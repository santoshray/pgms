from django.shortcuts import render
from django.http import HttpResponse
import re
import json
import datetime
from pgAccountApp.models import ExpenseRecord,TransactionRecord,ManagementTransactionRecord,TenantTransactionRecord
from userAccountApp.models import IdentityTypeRecord,AddressRecord,PersonalInfoRecord,UserAccountRecord,IdVerificationRecord,CompanyInfoRecord,EmergencyContactRecord
# Create your views here.

def index(request):
    res_dict = {}
    return render(request,'pgaccount/index.html',context=res_dict)

"""
<QueryDict: {
'expense_type': ['grocery'],
'txn_mode': ['cash'],
'startDate': ['2018-12-27'],
'endDate': ['2018-12-27'],
'amount': ['0.5'],
'description': ['s']}>
'csrfmiddlewaretoken': ['2t242iYLuZ1CXd5DJvhTYsQGTnew17mWz8grqiVD1lST3otzAv2Ox1dSOU8YHaXj'],
"""
def expense(request):
    res_dict = {}
    result = []
    display(request)

    if (request.method == 'GET'):
        res_dict["status"] = "NO_ERROR"
        res_dict["payload"] = {}
        res_dict["payload"]["display"] = "expense_form"
        return render(request,'pgaccount/expense.html',context=res_dict)

    if(request.method == 'POST'):
        post_content = request.POST
        expense_record = ExpenseRecord()
        expense_record.expense_type = post_content["expense_type"]
        txn_record = create_and_update_txn_record(post_content)
        if txn_record:
            tenantTxn_record = txn_record
            tenantTxn_record.save()
            expense_record.txn_info = txn_record
            expense_record.save()
            res_dict["status"] = "NO_ERROR"
            desc = []
            res_dict["payload"] = {}
            desc.append("Expense transaction is successful")
            res_dict["payload"]["reason"] = desc
            print(res_dict)
            return render(request,'pgaccount/expense.html',context=res_dict)
        else:
            res_dict["status"] = "ERROR"
            res_dict["payload"] = {}
            desc = []
            desc.append("Transaction could not be done")
            res_dict["payload"]["reason"] = desc
            #TBD : handle thre return in the  tenantTxn.html
            print(res_dict)
            return render(request,'pgaccount/expense.html',context=res_dict)

def tenantTransaction(request):

    res_dict = {}
    desc = []
    if (request.method == 'GET'):
        res_dict["status"] = "NO_ERROR"
        res_dict["payload"] = {}
        res_dict["payload"]["display"] = "tenant_query"

        return render(request,'pgaccount/tenantTxn.html',context=res_dict)

    if (request.method == "POST"):
        post_content = request.POST

        if post_content["infotype"] == "tenant_info":
            res_dict = pgaccount_get_user_record(request)
            print("FUNCTION = %s"%("tenantTransaction"))
            print(res_dict)
            return render(request,'pgaccount/tenantTxn.html',context=res_dict)

        elif post_content["infotype"] == "tenantTxn":
            tenantTxn_record = TenantTransactionRecord()
            tenantTxn_record.txn_type = post_content["expense_type"]
            tenantTxn_record.tenant = UserAccountRecord.objects.get(pk=int(post_content["tenant_id"]))
            print (tenantTxn_record.tenant)
            txn_record = create_and_update_txn_record(post_content)

            if txn_record:
                tenantTxn_record.txn_info = txn_record
                tenantTxn_record.save()
                res_dict["status"] = "NO_ERROR"
                desc = []
                res_dict["payload"] = {}
                desc.append("Tenant transaction is successful")
                res_dict["payload"]["reason"] = desc
                print(res_dict)
                return render(request,'pgaccount/tenantTxn.html',context=res_dict)
            else:
                res_dict["status"] = "ERROR"
                res_dict["payload"] = {}
                desc = []
                desc.append("Transaction could not be done")
                res_dict["payload"]["reason"] = desc
                #TBD : handle thre return in the  tenantTxn.html
                print(res_dict)
                return render(request,'pgaccount/tenantTxn.html',context=res_dict)


def managementTransaction(request):
    res_dict = {}
    result = []
    display(request)

    if (request.method == 'GET'):
        res_dict["status"] = "NO_ERROR"
        res_dict["payload"] = {}
        res_dict["payload"]["display"] = "expense_form"
        return render(request,'pgaccount/managementTxn.html',context=res_dict)

    if(request.method == 'POST'):
        post_content = request.POST
        mgmtTxn_record = ManagementTransactionRecord()
        mgmtTxn_record.type = post_content["expense_type"]
        txn_record = create_and_update_txn_record(post_content)
        if txn_record:
            mgmtTxn_record.txn_info = txn_record
            mgmtTxn_record.save()
            res_dict["status"] = "NO_ERROR"
            desc = []
            res_dict["payload"] = {}
            desc.append("Management transaction is successful")
            res_dict["payload"]["reason"] = desc
            print(res_dict)
            return render(request,'pgaccount/managementTxn.html',context=res_dict)
        else:
            res_dict["status"] = "ERROR"
            res_dict["payload"] = {}
            desc = []
            desc.append("Transaction could not be done")
            res_dict["payload"]["reason"] = desc
            #TBD : handle thre return in the  tenantTxn.html
            print(res_dict)
            return render(request,'pgaccount/managementTxn.html',context=res_dict)

        mgmtTxn_record.txn_info = txn_record
        mgmtTxn_record.save()

        return render(request,'pgaccount/managementTxn.html',context=res_dict)


# Internal functions



    """
        start_date  =  post_content["startDate"]
        d_obj = validate_date(start_date)
        if d_obj != None:
            tr.startDate= datetime.datetime(int(d_obj["year"]) ,int(d_obj["month"]) ,int(d_obj["day"]))
        else:
            result.append("Start date should be of format mm/dd/yyyy")

"""
#validate_date(d)
# returns object{"month":"mm","day":"dd","year":"yyyy"} if d is "mm/dd/yyyy"
# if d is not "mm/dd/yyyy" or "yyyy-mm-dd" function return None

def validate_date(d):
    rex_date = "\s*(\d\d)\/(\d\d)\/(\d\d\d\d)\s*"
    m = re.search(rex_date,d)
    d_obj = None
    if m:
        date_list = d.split('/')
        d_obj ={}
        d_obj["month"] = date_list[0]
        d_obj["day"] = date_list[1]
        d_obj["year"] = date_list[2]

    rex_date = "\s*(\d\d\d\d)\-(\d\d)\-(\d\d)\s*"
    m = re.search(rex_date,d)
    if m :
        date_list = d.split('-')
        d_obj ={}
        d_obj["month"] = date_list[1]
        d_obj["day"] = date_list[2]
        d_obj["year"] = date_list[0]

    return d_obj

def display(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    print(ip)
    """
    if request.method == 'POST':
        print(request.POST)

    if request.method == 'GET':
        print(request.GET)

    print("Cookies")
    print(request.COOKIES)
    print("META Information")
    print(request.META)

    print("FILES Information")
    print(request.FILES)
    """

    print("path = %s"%(request.path))
    print("path_info = %s"%(request.path_info))
    print("content_type = %s"%(request.content_type))
    print("content_params = %s"%(request.content_params))


def get_user_record(email,phone):
    if email != "":
        print ("FUNCTION : get_user_record ,  email = %s"%email)

        try:
            ur =UserAccountRecord.objects.get(userInfo__email=email)
        except :
            ur =None

        if ur != None:
            return ur

    if phone !="":
        try:
            ur =UserAccountRecord.objects.get(userInfo__phone=phone)
            print (ur)
        except :
            ur =None

        if ur != None:
            return ur

    return None


def pgaccount_get_user_record(request) :
    res_dict = {}

    if request.method == 'POST':
        post_content = request.POST

        email  = post_content["email"]
        phone = post_content["phone"]

        u  = get_user_record(email,phone)
        if u != None: # There should be only on unique user record with a phone or email id
            user_info_obj = {}
            user_info_obj["name"] = u.userInfo.first_name + " "+ u.userInfo.middle_name+" "+u.userInfo.last_name
            user_info_obj["email"] = u.userInfo.email
            user_info_obj["phone"] = u.userInfo.phone
            user_info_obj["id"] = u.id
            profilePhotolist = eval(u.profilePhotolist)
            if len(profilePhotolist) > 0 :
                user_info_obj["profilephoto"] = profilePhotolist[0]
            else:
                user_info_obj["profilephoto"] = ""

            res_dict["status"] = "NO_ERROR"
            res_dict["payload"] = {}
            res_dict["payload"]["user_info"] = user_info_obj
        else :
            desc = []
            res_dict["status"] = "ERROR"
            res_dict["payload"] = {}
            desc.append("No user record found")
            res_dict["payload"]["reason"] = desc

    else :
        res_dict["status"] = "ERROR"

    return res_dict


def create_and_update_txn_record(post_content):
    print("create_and_update_txn_record")
    txn_record = TransactionRecord()
    txn_record.amount = float(post_content['amount'])
    txn_record.comments = post_content["description"]
    txn_record.mode = post_content["txn_mode"]
    start_date  =  post_content["startDate"]
    d_obj = validate_date(start_date)
    if d_obj != None:
        txn_record.startDate= datetime.datetime(int(d_obj["year"]) ,int(d_obj["month"]) ,int(d_obj["day"]))
    else:
        result.append("Start date should be of format yyyy-mm-dd")

    end_date  =  post_content["endDate"]
    d_obj = validate_date(end_date)
    if d_obj != None:
        txn_record.endDate= datetime.datetime(int(d_obj["year"]) ,int(d_obj["month"]) ,int(d_obj["day"]))
    else:
        result.append("End date should be of format yyyy-mm-dd")

    print(txn_record.startDate)
    print(txn_record.endDate)

    txn_record.save()

    return txn_record


def financeSummary(request):

    res_dict = {}
    result = []
    display(request)

    if (request.method == 'GET'):
        res_dict["status"] = "NO_ERROR"
        res_dict["payload"] = {}
        res_dict["payload"]["display"] = "finance_summary"
        return render(request,'pgaccount/financeSummary.html',context=res_dict)

    if(request.method == "POST"):
        post_content = request.POST
        d_obj = validate_date(post_content["startDate"])
        if d_obj != None:
            startDate =  datetime.datetime(int(d_obj["year"]) ,int(d_obj["month"]) ,int(d_obj["day"]))
        else:
            result.append("End date should be of format mm/dd/yyyy")

        d_obj = validate_date(post_content["endDate"])
        if d_obj != None:
            endDate =  datetime.datetime(int(d_obj["year"]) ,int(d_obj["month"]) ,int(d_obj["day"]))
        else:
            result.append("End date should be of format mm/dd/yyyy")

        print(startDate , endDate)

        expense_list  =  ExpenseRecord.objects.filter(txn_info__endDate__range=[startDate,endDate])
#        expense_list  =  ExpenseRecord.objects.all()#(txn_info__endDate__range=[startDate,endDate])
        expense_sum  =  0
        mgmt_expense_sum = 0
        tenant_txn_sum = 0
        if (len(expense_list)>0):
            for e in expense_list:
                expense_sum +=e.txn_info.amount

        mgmt_expense_list  =  ManagementTransactionRecord.objects.filter(txn_info__endDate__range=[startDate,endDate])
        if (len(mgmt_expense_list)>0):
            for e in mgmt_expense_list:
                if (e.type == "withdrawl"):
                    mgmt_expense_sum -=e.txn_info.amount
                else:
                    mgmt_expense_sum +=e.txn_info.amount

        tenant_txn_list = TenantTransactionRecord.objects.filter(txn_info__endDate__range=[startDate,endDate])
        if (len(tenant_txn_list)>0):
            for e in tenant_txn_list:
                if (e.txn_type == "refund_deposit"):
                    tenant_txn_sum -=e.txn_info.amount
                else:
                    tenant_txn_sum +=e.txn_info.amount


        res_dict["status"] = "NO_ERROR"
        res_dict["payload"] = {}

        res_dict["payload"]["startDate"] = startDate.strftime("%m/%d/%Y")
        res_dict["payload"]["endDate"] = endDate.strftime("%m/%d/%Y")

        res_dict["payload"]["pg_expense_list"] = expense_list
        res_dict["payload"]["pg_expense_total"] = expense_sum
        res_dict["payload"]["mgmt_txn_list"] = mgmt_expense_list
        res_dict["payload"]["mgmt_txn_sum"] = mgmt_expense_sum
        res_dict["payload"]["tenant_txn_list"] = tenant_txn_list
        res_dict["payload"]["tenant_txn_sum"] = tenant_txn_sum

        return render(request,'pgaccount/financeSummary.html',context=res_dict)
