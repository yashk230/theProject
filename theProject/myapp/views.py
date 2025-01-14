import razorpay
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render

from .models import Cart, Money, ProjectImage, Projects, Services, Team


# Create your views here.
def index(request):
    context={}
    context['projects']=Projects.objects.all()
    context['services']=Services.objects.all()
    context['team']=Team.objects.all()
    return render(request,'index.html',context)


def content_details(request,cid):
    print("cid is ",cid)
    context = {}
    context["services"]=Services.objects.filter(id=cid)
    context["projects"]=Projects.objects.filter(id=cid)
    context['project_images'] = ProjectImage.objects.filter(project=cid)
    # order = Money.objects.filter(project_id=project.id).first()
    # context['order'] = order
    
    if Projects.objects.filter(id=cid).first():
        project=Projects.objects.filter(id=cid).first() # Check if the project exists
        print("project id",project)
        order = Money.objects.filter(project_id=project.id).first()
        context['order'] = order
    else:
        service = Services.objects.filter(id=cid).first()
        print("service id",service)
        order = Money.objects.filter(service_id=service.id).first()
        context['service_order'] = order
    return render(request,'content-details.html',context)

def about(request):
    context={}
    context['team']=Team.objects.all()
    return render(request,'about.html',context)

def contact(request):
    return render(request,'contact.html')

def project(request):
    context={}
    context['projects']=Projects.objects.all()
    return render(request,'project.html',context)


def project_folder(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    file_path = project.pfile.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{project.pfile.name}"'
    order = Money.objects.filter(project_id=project.id)
    order.delete()
    
    return response

def service(request):
    context={}
    context['services']=Services.objects.all()
    return render(request,'service.html',context)

def service_folder(request, service_id):
    service = get_object_or_404(Services, id=service_id)
    file_path = service.sfile.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{service.sfile.name}"'
    order = Money.objects.filter(service_id=service.id)
    order.delete()
    return response

def initiate_payment(request,pid):
    context={}
    context['projects']=Projects.objects.filter(id=int(pid))
    context['services']=Services.objects.filter(id=int(pid))
    if request.method == "POST":
        amount = float(request.POST['total_price']) * 100  # Convert to paise
        
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        if Projects.objects.filter(id=int(pid)):
            id_project=Projects.objects.get(id=int(pid))
            order = Money.objects.create(
            project_id=id_project,
            amount=amount / 100,
            razorpay_order_id=payment['id'],
        )
        else:
            id_services=Services.objects.get(id=int(pid))
            order = Money.objects.create(
            service_id=id_services,
            amount=amount / 100,
            razorpay_order_id=payment['id'],
        )
        
        context = {
            'order': order,
            'payment': payment,
            'razorpay_key_id': settings.RAZORPAY_KEY_ID
        }
        return render(request, 'payments.html', context)
    return render(request, 'initiate_payment.html',context)


def payment(request):
    if request.method == "POST":
        razorpay_order_id = request.POST.get('razorpay_order_id')
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_signature = request.POST.get('razorpay_signature')
        
        print(f'razorpay_order_id: {razorpay_order_id}')
        
        try:
            order = Money.objects.get(razorpay_order_id=razorpay_order_id)
            order.razorpay_payment_id = razorpay_payment_id
            order.razorpay_signature = razorpay_signature
            order.paid = True
            order.save()
            
            if order.project_id is not None:
                projects_id = order.project_id.id
                return redirect(f'/content_details/{projects_id}/') #it should redirect to the project_info page and the option to download the file sould appear
            else:
                projects_id = order.service_id.id
                return redirect(f'/content_details/{projects_id}/')
        except Money.DoesNotExist:
            return HttpResponse("Order not found", status=404)
    return redirect('initiate_payment')




def remove(request,rid):
    context={}
    c=Cart.objects.filter(id=rid)
    c.delete()
    context["msg"]="Item removed successfully"
    c=Cart.objects.filter(userid=request.user.id)
    context['cart']=c
    # print(c)
    return render(request,'cart.html',context)

def updateqty(request,x,uid):
    c=Cart.objects.filter(id=uid)
    p=Projects.objects.filter(id=x)
    # p=p.price
    q=c[0].quantity
    if x=="1":
        q=q+1
    elif q>1:
        q=q-1
    c.update(quantity=q)
    return render(request,'cart.html')


def view_cart(request):
    context={}
    if request.user.is_authenticated:
        c=Cart.objects.filter(userid=request.user.id)
        context['cart']=c
        totalqty=0
        totalprice=0
        for i in c:
            totalqty=totalqty+i.qty
            totalprice=totalprice+i.qty*i.pid.price
        print(totalqty)
        context["totalprice"]=totalprice
        context["items"]=totalqty
        return render(request,'view_cart.html',context)
    else:
        return redirect('/login')
    
def cart(request,pid):
    context={}
    context['projects']=Projects.objects.filter(id=int(pid))
    destionation=Cart.objects.create(project_id=int(pid),quantity=1,total=Projects.objects.get(id=int(pid)).price)
    destionation.save()
    context['cart']=Cart.objects.filter(project_id=int(pid))
    return render(request,'cart.html',context)


def feature(request):
    return render(request,'feature.html')

def team(request):
    context={}
    context['team']=Team.objects.all()
    return render(request,'team.html',context)

def quote(request):
    return render(request,'quote.html')

def testimonial(request):
    return render(request,'testimonial.html')