from django.shortcuts import render,redirect
from .models import HirePost, Professional,BidForJob
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


def deal(request, workId):
    user_id = Professional.objects.get(ProfessionID='2')
    if request.method == 'POST':
        job_post = HirePost.objects.get(hireID=workId)
        bid_money = request.POST.get('bid_money')
        offering = request.POST.get('description')
        applyJob = BidForJob(pID=user_id,jobID=job_post, offer=offering, bidPrice=bid_money)
        applyJob.save()

        return redirect(f'/hire/deals/{workId}')
    
    hireOne = HirePost.objects.get(hireID=workId)
    applied_Post = BidForJob.objects.filter(jobID__hireID=workId).order_by('-created_at')

    return render(request, 'deals.html', {'hireOne': hireOne, 'applidPost':applied_Post})


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
    for e in exparts:
        print(e.ProfessionID)
    return render(request,'professionals.html',{'exparts': exparts})

