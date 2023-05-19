from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import mimetypes
from django.conf import settings
import os
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str

from .models import Profile, Resume, Education, Languages, Skills, Projects, Contact
# Create your views here.



def home(request):
    profile = Profile.objects.get(pk=1)
    context = {
        'profile': profile
    }
    return render(request, 'main/index.html',context)


def resume(request):
    education = Education.objects.all()
    languages = Languages.objects.all()
    skills = Skills.objects.all()
    
    context = {
        'education':education,
        'languages':languages,
        'skills':skills
    }
    
    return render(request, 'main/resume.html', context)

def projects(request):
    projects = Projects.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'main/projects.html', context)

    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(name=name, phone=phone, mail=email, message=message)
        contact.save()
        
        return redirect('home')      
        
        
    return render(request, 'main/contact.html')    


def download_resume(request): 
    # resume = Resume.objects.get(pk=1).resume
    # path = resume.path
    path = str(settings.MEDIA_ROOT) + '/resume'
    wrapper = FileWrapper( open( path, "rb" ) )
    content_type = mimetypes.guess_type( path )[0]
    response = HttpResponse(wrapper, content_type = content_type)
    response['Content-Length'] = os.path.getsize( path )
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str( os.path.basename( path ) )
    return response
    
    