from django.shortcuts import render, redirect
from datetime import datetime
from .models import MemberType, MemberTypeHistory
from django.db.models import Max

# Create Member Type

def membertype_insert(request):
    if request.method == "POST":
        membertypename = request.POST['membertypename']
        membertypeshortname = request.POST['membertypeshortname']
        remarks = request.POST['remarks']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'

        #Getting the max value of product code, then computing for the next value in preparation for inserting a new record
        membertypecode_max = MemberType.objects.all().aggregate(Max('membertypecode'))
        membertypecode_nextvalue = 0 if membertypecode_max['membertypecode__max'] == None else membertypecode_max['membertypecode__max'] + 1

        data = MemberType(membertypecode=membertypecode_nextvalue, membertypename=membertypename, membertypeshortname=membertypeshortname, remarks=remarks, transactby=transactby, transactdate=transactdate, transacttype=transacttype)
        data.save()

        #Call the function for keeping history
        membertypehistory_save(data, transacttype)
  
        return redirect('/membertype')
    else:
        return render(request, 'membertype-insert.html')
    
# Retrive Member Type

def membertype_show(request):
    membertypes = MemberType.objects.exclude(transacttype = 'delete')
    return render(request,'membertype-show.html',{'membertypes':membertypes})

# Update Member Type

def membertype_edit(request,pk):
    membertype = MemberType.objects.get(recordno=pk)
    transacttype = 'edit'

    if request.method == 'POST':
        print(request.POST)
        membertype.membertypename = request.POST['membertypename']
        membertype.membertypeshortname = request.POST['membertypeshortname']
        membertype.remarks = request.POST['remarks']
        membertype.transactby = 0
        membertype.transactdate = datetime.now()
        membertype.transacttype = transacttype
        membertype.save()

        #Call the function for keeping history
        membertypehistory_save(membertype, transacttype)

        return redirect('/membertype')
    context = {
        'membertype': membertype,
    }

    return render(request,'membertype-edit.html',context)

# Delete Member Type

def membertype_remove(request, pk):
    membertype = MemberType.objects.get(recordno=pk)
    transacttype = 'delete'

    if request.method == 'POST':

        #Set values and update the record
        membertype.transactby = 0
        membertype.transactdate = datetime.now()
        membertype.transacttype = transacttype
        membertype.save()

        #Call the function for keeping history
        membertypehistory_save(membertype, transacttype)

        return redirect('/membertype')

    context = {
        'membertype': membertype,
    }

    return render(request, 'membertype-remove.html', context)

def membertypehistory_save(obj, transacttype):
    membertype = obj
    #Set values and insert the just updated record to history table that can be used for audit trail
    data = MemberTypeHistory(recordno = membertype.recordno,
    membertypecode = membertype.membertypecode,
    membertypename = membertype.membertypename,
    membertypeshortname = membertype.membertypeshortname,
    remarks = membertype.remarks,
    transactby = 0,
    transactdate = datetime.now(),
    transacttype = transacttype)
    data.save()