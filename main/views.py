from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
def home(request):
    return render(request,'index.html')


def contact(request):
 if request.method == 'POST':
    email_id= 'fsdpython@gmail.com'
    subject = 'New contact'
    name=request.POST.get('name')
    number=request.POST.get('number')
    message = request.POST.get('msg')
    send_mail(
       subject,
       f'name- {name}\nmessage- {message}\nnumber-{number} ',
       'fsdpython@gmail.com',
       [email_id],
       fail_silently=False
    )
 return redirect('home')
    
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['admin@example.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('home')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')


 return render(request,'index.html')