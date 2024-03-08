from django.shortcuts import render, redirect
from datetime import datetime
from .models import Plan, PlanHistory
from products_app.models import Products
from roomtype_app.models import RoomType
from membertype_app.models import MemberType
from limittype_app.models import LimitType
from django.db.models import Max
import decimal

# Create Plan

def plan_insert(request):
    #Get data from various models to be used for respective dropdown items
    products = Products.objects.exclude(transacttype = 'delete')
    rooms = RoomType.objects.exclude(transacttype = 'delete')
    membertypes = MemberType.objects.exclude(transacttype = 'delete')
    limittypes = LimitType.objects.exclude(transacttype = 'delete')
    
    if request.method == "POST":
        plantype = request.POST['plantype']
        
        # Fetch the Products instance with the provided productcode
        #productcode_qs = Products.objects.exclude(transacttype = 'delete')
        productcode = Products.objects.get(productcode=request.POST['productcode'])
        
        # Fetch the RoomType instance with the provided roomcode
        #roomcode_qs = RoomType.objects.exclude(transacttype = 'delete')
        roomcode = RoomType.objects.get(roomcode=request.POST['roomcode'])
        
        # Fetch the MemberType instance with the provided membertypecode
        #membertypecode_qs = MemberType.objects.exclude(transacttype = 'delete')
        membertypecode = MemberType.objects.get(membertypecode=request.POST['membertypecode'])

        agefrom = decimal.Decimal(request.POST['agefrom'])
        ageto = decimal.Decimal(request.POST['ageto'])
        premiumamount = decimal.Decimal(request.POST['premiumamount'])
        benefitlimit = decimal.Decimal(request.POST['benefitlimit'])

        # Fetch the LimitType instance with the provided limittypecode
        #limittypecode_qs = LimitType.objects.exclude(transacttype = 'delete')
        limittypecode = LimitType.objects.get(limittypecode=request.POST['limittypecode'])

        withaccesstotophospital = request.POST['withaccesstotophospital']
        remarks = request.POST['remarks']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'

        #Getting the max value of plan code, then computing for the next value in preparation for inserting a new record
        plancode_max = Plan.objects.all().aggregate(Max('plancode'))
        plancode_nextvalue = 0 if plancode_max['plancode__max'] == None else plancode_max['plancode__max'] + 1

        data = Plan(plancode=plancode_nextvalue,
                    plantype=plantype,
                    productcode=productcode,
                    roomcode=roomcode,
                    membertypecode=membertypecode,
                    agefrom=agefrom,
                    ageto=ageto,
                    premiumamount=premiumamount,
                    benefitlimit=benefitlimit,
                    limittypecode=limittypecode,
                    withaccesstotophospital=withaccesstotophospital,
                    remarks=remarks,
                    transactby=transactby,
                    transactdate=transactdate,
                    transacttype=transacttype
                    )
        data.save()

        #Call the function for keeping history
        planhistory_save(data, transacttype)
  
        return redirect('/plan')
    else:
        return render(request, 'plan-insert.html', {'products':products, 'rooms':rooms, 'membertypes':membertypes, 'limittypes':limittypes})
    
# Retrive Plan

def plan_show(request):
    
    #Get data from joined models to be used for showing plans and its related fields
    plans = Plan.objects.select_related('productcode','roomcode','membertypecode','limittypecode').exclude(transacttype = 'delete')
    return render(request,'plan-show.html',{'plans':plans})

# Update Plan
def plan_edit(request,pk):
    plan = Plan.objects.get(recordno=pk)
    transacttype = 'edit'

    if request.method == 'POST':
        print(request.POST)
        plan.plantype = request.POST['plantype']
        plan.productcode = request.POST['productcode']
        plan.roomcode = request.POST['roomcode']
        plan.membertypecode = request.POST['membertypecode']
        plan.agefrom = request.POST['agefrom']
        plan.ageto = request.POST['ageto']
        plan.premiumamount = request.POST['premiumamount']
        plan.benefitlimit = request.POST['benefitlimit']
        plan.limittypecode = request.POST['limittypecode']
        plan.withaccesstotophospital = request.POST['withaccesstotophospital']
        plan.remarks = request.POST['remarks']
        plan.transactby = 0
        plan.transactdate = datetime.now()
        plan.transacttype = transacttype
        plan.save()

        #Call the function for keeping history
        planhistory_save(plan, transacttype)

        return redirect('/plan')
    context = {
        'plan': plan,
    }

    return render(request,'plan-edit.html',context)

# Delete Member Type

def plan_remove(request, pk):
    plan = Plan.objects.get(recordno=pk)
    transacttype = 'delete'

    if request.method == 'POST':

        #Set values and update the record
        plan.transactby = 0
        plan.transactdate = datetime.now()
        plan.transacttype = transacttype
        plan.save()

        #Call the function for keeping history
        planhistory_save(plan, transacttype)

        return redirect('/plan')

    context = {
        'plan': plan,
    }

    return render(request, 'plan-remove.html', context)

def planhistory_save(obj, transacttype):
    plan = obj
    #Set values and insert the just updated record to history table that can be used for audit trail
    data = PlanHistory(recordno = plan.recordno,
    plancode = plan.plancode,
    plantype = plan.plantype,
    productcode = plan.productcode,
    roomcode = plan.roomcode,
    membertypecode = plan.membertypecode,
    agefrom = plan.agefrom,
    ageto = plan.ageto,
    premiumamount = plan.premiumamount,
    benefitlimit = plan.benefitlimit,
    limittypecode = plan.limittypecode,
    withaccesstotophospital = plan.withaccesstotophospital,
    remarks = plan.remarks,
    transactby = 0,
    transactdate = datetime.now(),
    transacttype = transacttype)
    data.save()