from django.shortcuts import render, redirect
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

def createProject(request):
    form = ProjectForm()

    # submit query
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid(): # django can check against our models.Project
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    #prefill the project form with the project's data
    form = ProjectForm(instance=project)

    # submit query
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid(): # django can check against our models.Project
            form.save()
            return redirect('projects')
    
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object':project}

    if request.method == 'POST':
        if 'delete' in request.POST:
            project.delete()
        return redirect('projects')

    return render(request, 'projects/delete_template.html',context)