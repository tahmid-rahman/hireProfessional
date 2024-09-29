from django.shortcuts import render,redirect
from .models import HirePost, Professional
# Create your views here.


def hire(request):

    if request.method == 'POST':
        expart_type = request.POST.get('expart_type')
        description = request.POST.get('description')
        offered_money = request.POST.get('offered_money')

        createHirePost = HirePost(username='tahmid', expart_type=expart_type, description=description, offered_money=offered_money)
        createHirePost.save()
        print('hello')
        return redirect('/hire')
    
    hires = HirePost.objects.order_by('-created_at')
    return render(request,'main.html',{'hires': hires})


def try_view(request):
    return render(request,'try_view.html')




def professional(request):

    if request.method == 'POST':
        # Get data from the form
        username = 'tahmid_rahman'
        fullname = request.POST.get('fullname')
        profession = request.POST.get('profession')
        description = request.POST.get('description')

        Professional.objects.create(
            username = username,
            fullname=fullname,
            profession=profession,
            description=description
        )

        return redirect('/hire/professionals')

    exparts = Professional.objects.all()
    return render(request,'professionals.html',{'exparts': exparts})

