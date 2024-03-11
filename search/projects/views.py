from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags':tags})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    # submit query
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid(): # django can check against our models.Project
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    #prefill the project form with the project's data
    form = ProjectForm(instance=project)

    # submit query
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid(): # django can check against our models.Project
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}

    if request.method == 'POST':
        if 'delete' in request.POST:
            project.delete()
        return redirect('account')
    if 'cancel' in request.POST:
            return redirect(request.GET.get('next', '/'))

    return render(request, 'delete_template.html',context)