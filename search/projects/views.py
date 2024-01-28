from django.shortcuts import render

projects_list = [{'id':'1', 'title':'finance model', 'description':'Model your personal finance'}
,{'id':'2', 'title':'Portfolio Website', 'description':'Just keep memorising frameworks'}
,{'id':'3', 'title':'ASL translator', 'description':'train a CNN to recognise the ASL'}
]

def projects(request):
    page = 'Projects'
    number = 10
    context = {'page':page, 'number':number, 'projects':projects_list}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projects_list:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
