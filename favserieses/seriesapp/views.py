from django.shortcuts import render, redirect
from .models import watched_series, watched_later_series
from .forms import watch_form,later_form

def home(request):
    return render(request,'index.html')

def watched(request):
    obj = watched_series.objects.all()
    return render(request,'watched.html',{'series_key':obj})

def watchlater(request):
    later = watched_later_series.objects.all()
    return render(request,'watchlater.html',{'later_key':later})

def addwatch(request):
   try:
       if request.method == 'POST':
           name = request.POST['name']
           image = request.FILES['image']

           watched = watched_series(name=name, image=image)
           watched.save()
           return redirect('watched')


   except:
       return redirect('addwatch')
   return render(request, 'addwatched.html')


def addwatchlater(request):
    try:
        if request.method == 'POST':
            name=request.POST['name']
            image=request.FILES['image']

            later=watched_later_series(name=name,image=image)
            later.save()
            return redirect('watchlater')
    except:
        return redirect('addwatchlater')
    return render(request,'addlater.html')

def update(request,series_id):
    series =watched_series.objects.get(id=series_id)
    form = watch_form(request.POST or None,request.FILES,instance=series)

    if form.is_valid():
       form.save()
       return redirect('watched')



    return render(request,'update.html',{'series':series,'form':form})

def update1(request,series_id):
    series = watched_later_series.objects.get(id=series_id)
    form = later_form(request.POST or None, request.FILES, instance=series)
    if form.is_valid():
        form.save()
        return redirect('watchlater')
    return render(request, 'update.html', {'series': series, 'form': form})

def delete(request,series_id):
    series = watched_series.objects.get(id=series_id)
    series.delete()
    return redirect('watched')
def delete1(request,series_id):
    series = watched_later_series.objects.get(id=series_id)
    series.delete()
    return redirect('watchlater')
