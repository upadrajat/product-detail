from django.shortcuts import render,HttpResponse
from .forms import ProductForm,uppdateForm,DeleteForm
from .models import Product
from django.template import loader


def home(request):
    return render(request,'home.html')
def insert(request):
    if request.method=='POST':
        form=ProductForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            data="<h1>Insertion is successfully done</h1>"\
            "<a href='./'>Goto home</a>"
            return HttpResponse(data)
        else:
            print(form.errors)

    else:
        form=ProductForm()
        return render(request,'insert.html',{'form':form})

def display(request):
    det=Product.objects.all()
    if len(det)==0:
        data="<h1>no data found</h1>"\
              "<a href='./'>Goto home</a>"
        return HttpResponse(data)
    else:
        template=loader.get_template('details.html')
        context={'det':det}
        r=template.render(context,request)
        return HttpResponse(r)

def update(request):
    if request.method=='POST':
        form=uppdateForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data['pid']
            id1=int(id)
            cost=form.cleaned_data['pcost']
            cost1=int(cost)
            dbuser=Product.objects.filter(pid=id1)
            if not dbuser:
                data="<h1>Invalid product id</h1>"\
                     "<a href='./'>Goto Home</a>"
                return HttpResponse(data)
            else:
                dbuser.update(pcost=cost)
                data="<h1> product updated successfully</h1>"\
                      "<a href='./'>Goto home</a>"
                return HttpResponse(data)
        else:
            print(form.errors)
    else:
        form=uppdateForm()
        return render(request,'update.html',{'form':form})

def delete(request):
    if request.method=='POST':
        form=DeleteForm(request.POST)
        if form.is_valid():
            pid1=int(form.cleaned_data['pid'])
            dbuser=Product.objects.get(pid=pid1)
            print(dbuser,"test")
            if not dbuser:
                return HttpResponse('The given id is not available')
            else:
                dbuser.delete()
                data="<h1>Product was deleted successfully</h1>"\
                    "<a href='./'>Goto home</a>"
                return HttpResponse(data)
        else:
            print(form.errors)
    else:
        form=DeleteForm()
        return render(request,'delete.html',{'form':form})


