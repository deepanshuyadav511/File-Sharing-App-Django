from django.shortcuts import render, redirect
from .models import File_info
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

mypost_btn = True
share_btn = True

# Create your views here.
def home(request):
    user = settings.AUTH_USER_MODEL
    current_user = request.user
    posts = File_info.objects.all()
    
    return render(request, 'fileshareapp/home.html', {'posts':posts,'mypost_btn':mypost_btn,'share_btn':share_btn, 'current_user':current_user})


@login_required
def share(request):
    share_btn = False
    user = settings.AUTH_USER_MODEL
    current_user = request.user
    if request.method == 'POST':
        user = settings.AUTH_USER_MODEL
        title = request.POST['title']
        file_in = request.FILES.get('file')
        description = request.POST['description']
        datetime = timezone.now()
        upload = File_info(username=request.user, title=title, file=file_in, description=description, datetime=datetime)
        upload.save()
        messages.success(request, ('Uploaded successfully'))
        return redirect('fileshareapp:Home')
    else:    
        return render(request, 'fileshareapp/share.html', {'share_btn': share_btn, 'current_user':current_user})


@login_required
def user_posts(request):
    share_btn = True
    mypost_btn = False
    user = settings.AUTH_USER_MODEL
    current_user = request.user
    posts = File_info.objects.all()

    return render(request, 'fileshareapp/myposts.html', {'posts':posts,'mypost_btn':mypost_btn,'share_btn':share_btn, 'current_user':current_user})


@login_required
def delete(request, pk):
    dest = File_info.objects.get(id = pk)
    dest.delete()
    return redirect('fileshareapp:Myposts')