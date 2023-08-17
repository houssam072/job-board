from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Jop
from django.core.paginator import Paginator
from .forms import ApplyForm, JopForm
from django.contrib.auth.decorators import login_required
from .filter import JobFilter

def job_list(request):
    job_list = Jop.objects.all()
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list = myfilter.qs


    paginator = Paginator(job_list,2)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    context = {'jobs' : page_obj, 'myfilter' : myfilter}
    return render(request, 'job/job_list.html' , context)

def job_detailes(request, slug):
    job_detailes = Jop.objects.get(slug=slug)

    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit = False)
            myform.job = job_detailes
            myform.save()
            
    else:
        form = ApplyForm()
    
    context = {
        "job_detailes" : job_detailes,
        "form" : form
    }
    return render(request, 'job/job_detailes.html', context)


@login_required
def add_jop(request):
    if request.method == "POST":
        form  = JopForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JopForm()
    context = {
        'form':form
    }
    return render(request, 'job/add_job.html', context)
