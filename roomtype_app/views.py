from django.shortcuts import render, redirect
from datetime import datetime
from .models import RoomType, RoomTypeHistory
from django.db.models import Max

# Create Room Type

def roomtype_insert(request):
    if request.method == "POST":
        roomname = request.POST['roomname']
        roomshortname = request.POST['roomshortname']
        remarks = request.POST['remarks']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'

        #Getting the max value of product code, then computing for the next value in preparation for inserting a new record
        roomcode_max = RoomType.objects.all().aggregate(Max('roomcode'))
        roomcode_nextvalue = 0 if roomcode_max['roomcode__max'] == None else roomcode_max['roomcode__max'] + 1

        data = RoomType(roomcode=roomcode_nextvalue, roomname=roomname, roomshortname=roomshortname, remarks=remarks, transactby=transactby, transactdate=transactdate, transacttype=transacttype)
        data.save()

        #Call the function for keeping history
        roomtypehistory_save(data, transacttype)
  
        return redirect('/roomtype')
    else:
        return render(request, 'roomtype-insert.html')
    
# Retrive Room Type

def roomtype_show(request):
    roomtypes = RoomType.objects.exclude(transacttype = 'delete')
    return render(request,'roomtype-show.html',{'roomtypes':roomtypes})

# Update Room Type

def roomtype_edit(request,pk):
    roomtype = RoomType.objects.get(recordno=pk)
    transacttype = 'edit'

    if request.method == 'POST':
        print(request.POST)
        roomtype.roomname = request.POST['roomname']
        roomtype.roomshortname = request.POST['roomshortname']
        roomtype.remarks = request.POST['remarks']
        roomtype.transactby = 0
        roomtype.transactdate = datetime.now()
        roomtype.transacttype = transacttype
        roomtype.save()

        #Call the function for keeping history
        roomtypehistory_save(roomtype, transacttype)

        return redirect('/roomtype')
    context = {
        'roomtype': roomtype,
    }

    return render(request,'roomtype-edit.html',context)

# Delete Room Type

def roomtype_remove(request, pk):
    roomtype = RoomType.objects.get(recordno=pk)
    transacttype = 'delete'

    if request.method == 'POST':

        #Set values and update the record
        roomtype.transactby = 0
        roomtype.transactdate = datetime.now()
        roomtype.transacttype = transacttype
        roomtype.save()

        #Call the function for keeping history
        roomtypehistory_save(roomtype, transacttype)

        return redirect('/roomtype')

    context = {
        'roomtype': roomtype,
    }

    return render(request, 'roomtype-remove.html', context)

def roomtypehistory_save(obj, transacttype):
    roomtype = obj
    #Set values and insert the just updated record to history table that can be used for audit trail
    data = RoomTypeHistory(recordno = roomtype.recordno,
    roomcode = roomtype.roomcode,
    roomname = roomtype.roomname,
    roomshortname = roomtype.roomshortname,
    remarks = roomtype.remarks,
    transactby = 0,
    transactdate = datetime.now(),
    transacttype = transacttype)
    data.save()