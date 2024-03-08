from django.shortcuts import render, redirect
from datetime import datetime
from .models import LimitType, LimitTypeHistory
from django.db.models import Max

# Create Limit Type

def limittype_insert(request):
    if request.method == "POST":
        limittypename = request.POST['limittypename']
        limittypeshortname = request.POST['limittypeshortname']
        limittypeunit = request.POST['limittypeunit']
        remarks = request.POST['remarks']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'

        #Getting the max value of limit code, then computing for the next value in preparation for inserting a new record
        limittypecode_max = LimitType.objects.all().aggregate(Max('limittypecode'))
        limittypecode_nextvalue = 0 if limittypecode_max['limittypecode__max'] == None else limittypecode_max['limittypecode__max'] + 1

        data = LimitType(limittypecode=limittypecode_nextvalue, limittypename=limittypename, limittypeshortname=limittypeshortname, limittypeunit=limittypeunit, remarks=remarks, transactby=transactby, transactdate=transactdate, transacttype=transacttype)
        data.save()

        #Call the function for keeping history
        limittypehistory_save(data, transacttype)
  
        return redirect('/limittype')
    else:
        return render(request, 'limittype-insert.html')
    
# Retrive Limit Type

def limittype_show(request):
    limittypes = LimitType.objects.exclude(transacttype = 'delete')
    return render(request,'limittype-show.html',{'limittypes':limittypes})

# Update Limit Type

def limittype_edit(request,pk):
    limittype = LimitType.objects.get(recordno=pk)
    transacttype = 'edit'

    if request.method == 'POST':
        print(request.POST)
        limittype.limittypename = request.POST['limittypename']
        limittype.limittypeshortname = request.POST['limittypeshortname']
        limittype.limittypeunit = request.POST['limittypeunit']
        limittype.remarks = request.POST['remarks']
        limittype.transactby = 0
        limittype.transactdate = datetime.now()
        limittype.transacttype = transacttype
        limittype.save()

        #Call the function for keeping history
        limittypehistory_save(limittype, transacttype)

        return redirect('/limittype')
    context = {
        'limittype': limittype,
    }

    return render(request,'limittype-edit.html',context)

# Delete Limit Type

def limittype_remove(request, pk):
    limittype = LimitType.objects.get(recordno=pk)
    transacttype = 'delete'

    if request.method == 'POST':

        #Set values and update the record
        limittype.transactby = 0
        limittype.transactdate = datetime.now()
        limittype.transacttype = transacttype
        limittype.save()

        #Call the function for keeping history
        limittypehistory_save(limittype, transacttype)

        return redirect('/limittype')

    context = {
        'limittype': limittype,
    }

    return render(request, 'limittype-remove.html', context)

def limittypehistory_save(obj, transacttype):
    limittype = obj
    #Set values and insert the just updated record to history table that can be used for audit trail
    data = LimitTypeHistory(recordno = limittype.recordno,
    limittypecode = limittype.limittypecode,
    limittypename = limittype.limittypename,
    limittypeshortname = limittype.limittypeshortname,
    limittypeunit = limittype.limittypeunit,
    remarks = limittype.remarks,
    transactby = 0,
    transactdate = datetime.now(),
    transacttype = transacttype)
    data.save()