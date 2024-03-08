from django.shortcuts import render, redirect
from datetime import datetime
from .models import ProviderCategory
from django.db.models import Max
from django.contrib import messages

# Create your views here.
# Create Providers Category

def prvdrcateg_insert(request):
    
    if request.method == "POST":
        providercategoryname = request.POST['providercategoryname']
        providercategoryshortname = request.POST['providercategoryshortname']
        remarks = request.POST['remarks']
        ordernumber = request.POST['ordernumber']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'
        
        #Validation: Checking if the category name already exists
        try:
            ProviderCategory.objects.get(providercategoryname=providercategoryname)
            isexist = True
        except ProviderCategory.DoesNotExist:
            isexist = False
        
        #If record exists, render the add form again or add the record and render the list of categories
        if isexist:
            messages.success(request, f"The Category { providercategoryname } Already Exists!")
            return render(request, 'prvdrcateg-insert.html', {'ordernumber_nextvalue': ordernumber})
        else:
            #Getting the max value of category code, then computing for the next value in preparation for inserting a new record
            categorycode_max = ProviderCategory.objects.all().aggregate(Max('categorycode'))
            categorycode_nextvalue = 1 if categorycode_max['categorycode__max'] == None else categorycode_max['categorycode__max'] + 1

            data = ProviderCategory(categorycode=categorycode_nextvalue, providercategoryname=providercategoryname, providercategoryshortname=providercategoryshortname, remarks=remarks, ordernumber=ordernumber, transactby=transactby, transactdate=transactdate, transacttype=transacttype)
            data.save()

            return redirect('/prvdrcateg')
    else:
        #Getting the max value of order number for category code, then computing for the next value as initial assumption of the value.
        ordernumber_max = ProviderCategory.objects.all().aggregate(Max('ordernumber'))
        ordernumber_nextvalue = 0 if ordernumber_max['ordernumber__max'] == None else ordernumber_max['ordernumber__max'] + 1
        

        return render(request, 'prvdrcateg-insert.html', {'ordernumber_nextvalue': ordernumber_nextvalue})


# Retrive Providers Category
def prvdrcateg_show(request):
    prvdrcateg = ProviderCategory.objects.all()
    return render(request,'prvdrcateg-show.html',{'prvdrcateg':prvdrcateg})


# Update Providers Category
def prvdrcateg_edit(request,pk):
    prvdrcateg = ProviderCategory.objects.get(recordno=pk)
    if request.method == 'POST':
        print(request.POST)
        prvdrcateg.categorycode = request.POST['categorycode']
        prvdrcateg.providercategoryname = request.POST['providercategoryname']
        prvdrcateg.providercategoryshortname = request.POST['providercategoryshortname']
        prvdrcateg.remarks = request.POST['remarks']
        prvdrcateg.ordernumber = request.POST['ordernumber']
        prvdrcateg.transactby = 0
        prvdrcateg.transactdate = datetime.now()
        prvdrcateg.transacttype = 'edit'
            
        #Validation: Checking if the category name already exists
        try:
            ProviderCategory.objects.get(providercategoryname=prvdrcateg.providercategoryname)
            isexist = True
        except ProviderCategory.DoesNotExist:
            isexist = False
        
        #If record exists, render the edit form again or update the record and render the list of categories
        if isexist:
            messages.success(request, f"The Category { prvdrcateg.providercategoryname } Already Exists!")
            return render(request, 'prvdrcateg-edit.html')
        else:
            prvdrcateg.save()
            
            return redirect('/prvdrcateg')

    context = {
        'prvdrcateg': prvdrcateg,
    }

    return render(request,'prvdrcateg-edit.html',context)


# Delete Providers Category

def prvdrcateg_remove(request, pk):
    prvdrcateg = ProviderCategory.objects.get(recordno=pk)

    if request.method == 'POST':
        prvdrcateg.delete()
        return redirect('/prvdrcateg')

    context = {
        'prvdrcateg': prvdrcateg,
    }

    return render(request, 'prvdrcateg-remove.html', context)