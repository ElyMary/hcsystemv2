from datetime import datetime
from django.shortcuts import render, redirect
from .models import Adjudication 


# Create your views here.
def adju_show(request):
    adjudications = Adjudication.objects.all()
    return render(request, 'adju-show.html', {'adjudications':adjudications})

def adju_insert(request):
    if request.method == "POST":
        adjudicationcode = request.POST['adjudicationcode']
        providercode = request.POST['providercode']
        soanumber = request.POST['soanumber']
        soadate = request.POST['soadate']
        duedate = request.POST['duedate']
        claimsstatus = request.POST['claimsstatus']
        remarks = request.POST['remarks']
        transactby = request.POST['transactby']
        transactdate = datetime.now()
        transactype =request.POST['transactype']

        data = Adjudication(adjudicationcode=adjudicationcode, providercode=providercode, 
                            soanumber=soanumber, soadate=soadate, duedate=duedate,
                            claimsstatus=claimsstatus, remarks=remarks, transactby=transactby,
                            transactdate=transactdate, transactype=transactype)
        data.save()
        
        return redirect('adju-list')
    else:
        return render(request, 'adju-insert.html')


def adju_list(request):
    adjudications = Adjudication.objects.all()
    return render(request, 'adju-list.html', {'adjudications':adjudications})