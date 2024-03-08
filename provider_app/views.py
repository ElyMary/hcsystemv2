from django.shortcuts import render, redirect
from datetime import datetime
from .models import Providers
from providercategory_app.models import ProviderCategory
from django.db.models import Max

# Create your views here.
# Create Providers

def provider_insert(request):
    #Get categories for dropdown
    categories = ProviderCategory.objects.all()
    if request.method == "POST":

        categorycode = request.POST['categorycode']
        providername = request.POST['providername']
        tin = request.POST['tin']
        address = request.POST['address']
        locationcode = request.POST['locationcode']
        emailaddress = request.POST['emailaddress']
        contactperson = request.POST['contactperson']
        landline = request.POST['landline']
        mobilenumber = request.POST['mobilenumber']
        remarks = request.POST['remarks']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'

        #Getting the max value of provider code, then computing for the next value in preparation for inserting a new record
        providercode_max = Providers.objects.all().aggregate(Max('providercode'))
        providercode_nextvalue = 0 if providercode_max['providercode__max'] == None else providercode_max['providercode__max'] + 1
        
        data = Providers(providercode=providercode_nextvalue, categorycode=categorycode, providername=providername, tin=tin, address=address, locationcode=locationcode, emailaddress=emailaddress, contactperson=contactperson, landline=landline, mobilenumber=mobilenumber, remarks=remarks, transactby=transactby, transactdate=transactdate, transacttype=transacttype)
        data.save()
  
        return redirect('/provider')
    else:
        return render(request, 'provider-insert.html', {'categories': categories})


# Retrive Providers

def provider_show(request):
    providers = Providers.objects.all()
    return render(request,'provider-show.html',{'providers':providers})


# Update Providers

def provider_edit(request,pk):
    providers = Providers.objects.get(recordno=pk)
    if request.method == 'POST':
            print(request.POST)
            providers.categorycode = request.POST['categorycode']
            providers.providername = request.POST['providername']
            providers.tin = request.POST['tin']
            providers.address = request.POST['address']
            providers.locationcode = request.POST['locationcode']
            providers.emailaddress = request.POST['emailaddress']
            providers.contactperson = request.POST['contactperson']
            providers.landline = request.POST['landline']
            providers.mobilenumber = request.POST['mobilenumber']
            providers.remarks = request.POST['remarks']
            providers.transactby = 0
            providers.transactdate = datetime.now()
            providers.transacttype = 'edit'
            providers.save()
            return redirect('/provider')
    context = {
        'providers': providers,
    }

    return render(request,'provider-edit.html',context)


# Delete Providers

def provider_remove(request, pk):
    providers = Providers.objects.get(recordno=pk)

    if request.method == 'POST':
        providers.delete()
        return redirect('/provider')

    context = {
        'providers': providers,
    }

    return render(request, 'provider-remove.html', context)