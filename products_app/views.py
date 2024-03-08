from django.shortcuts import render, redirect
from datetime import datetime
from .models import Products, ProductsHistory
from django.db.models import Max

# Create Product

def products_insert(request):
    if request.method == "POST":
        productname = request.POST['productname']
        productshortname = request.POST['productshortname']
        productdescription = request.POST['productdescription']
        remarks = request.POST['remarks']
        transactby = 0
        transactdate = datetime.now()
        transacttype = 'add'

        #Getting the max value of product code, then computing for the next value in preparation for inserting a new record
        productcode_max = Products.objects.all().aggregate(Max('productcode'))
        productcode_nextvalue = 0 if productcode_max['productcode__max'] == None else productcode_max['productcode__max'] + 1

        data = Products(productcode=productcode_nextvalue, productname=productname, productshortname=productshortname, productdescription=productdescription, remarks=remarks, transactby=transactby, transactdate=transactdate, transacttype=transacttype)
        data.save()

        #Call the function for keeping history
        producthistory_save(data, transacttype)
  
        return redirect('/product')
    else:
        return render(request, 'products-insert.html')
    
# Retrive Products

def products_show(request):
    products = Products.objects.exclude(transacttype = 'delete')
    return render(request,'products-show.html',{'products':products})

# Update Products

def products_edit(request,pk):
    product = Products.objects.get(recordno=pk)
    transacttype = 'edit'

    if request.method == 'POST':
        print(request.POST)
        product.productname = request.POST['productname']
        product.productshortname = request.POST['productshortname']
        product.productdescription = request.POST['productdescription']
        product.remarks = request.POST['remarks']
        product.transactby = 0
        product.transactdate = datetime.now()
        product.transacttype = transacttype
        product.save()

        #Call the function for keeping history
        producthistory_save(product, transacttype)

        return redirect('/product')
    context = {
        'product': product,
    }

    return render(request,'products-edit.html',context)

# Delete Products

def products_remove(request, pk):
    product = Products.objects.get(recordno=pk)
    transacttype = 'delete'

    if request.method == 'POST':

        #Set values and update the record
        product.transactby = 0
        product.transactdate = datetime.now()
        product.transacttype = transacttype
        product.save()

        #Call the function for keeping history
        producthistory_save(product, transacttype)

        return redirect('/product')

    context = {
        'product': product,
    }

    return render(request, 'products-remove.html', context)

def producthistory_save(obj, transacttype):
    product = obj
    #Set values and insert the just updated record to history table that can be used for audit trail
    data = ProductsHistory(recordno = product.recordno,
    productcode = product.productcode,
    productname = product.productname,
    productshortname = product.productshortname,
    productdescription = product.productdescription,
    remarks = product.remarks,
    transactby = 0,
    transactdate = datetime.now(),
    transacttype = transacttype)
    data.save()