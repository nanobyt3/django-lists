from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

# import todo form and models

from .forms import ListsForm, ListForm
from .models import Lists, List

###############################################

@login_required
def showActiveLists(request):
    item_list = Lists.objects.filter(archive=False).order_by("-date")
    page = {
        "list": item_list,
        "title": "Lists: Active",
    }
    return render(request, 'lists/index.html', page)

def showArchivedLists(request):
    item_list = Lists.objects.filter(archive=True).order_by("-date")
    page = {
        "list": item_list,
        "title": "Lists: Archive",
    }
    return render(request, 'lists/index.html', page)

def addListForm(request):
    if request.method == "POST":
        form = ListsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"The list '{form.cleaned_data['title']}' has been created!")
            return redirect('lists')
        
    form = ListsForm()

    page = {
        "form": form,
        "title": "Create New List",
    }
    return render(request, 'lists/form.html', page)

def editListForm(request, item_id):
    list_obj = Lists.objects.get(id=item_id)
    if request.method == "GET":
        form = ListsForm(instance=list_obj)
    else:
        form = ListsForm(request.POST, instance=list_obj)
        if form.is_valid():
            form.save()
            messages.info(request, f"The list '{list_obj.title}' has been updated!")
            return redirect('lists')

    page = {
        "form": form,
        "title": "Edit list:" + list_obj.title,
    }
    return render(request, 'lists/form.html', page)

def showList(request, item_id):
    list_obj = Lists.objects.get(id=item_id)
    item_list = List.objects.filter(list=item_id).order_by("status", "-date")
    page = {
        "list_id": list_obj.id,
        "list": item_list,
        "title": "List:" + list_obj.title,
    }
    return render(request, 'lists/list-index.html', page)

def deleteList(request, item_id):
    item = Lists.objects.get(id=item_id)
    name = f"{item.title} [{item.id}]"
    item.delete()
    messages.info(request, f"The list '{name}' has been deleted!")
    return redirect('lists')

def addListItemForm(request, item_id):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"The item '{form.cleaned_data['title']}' has been created!")
            return redirect('create-list-item', item_id=item_id)
        
    form = ListForm(initial={'list': item_id})

    page = {
        "list_id": item_id,
        "form": form,
        "title": "Create new list item.",
    }
    return render(request, 'lists/form.html', page)

def editListItemForm(request, item_id):
    obj = List.objects.get(id=item_id)
    if request.method == "GET":
        form = ListForm(instance=obj)
    else:
        form = ListForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request, f"The item '{obj.title}' has been updated!")
            return redirect('view-list', item_id=obj.list.id)

    page = {
        "list_id": obj.list.id,
        "form": form,
        "title": "Edit list item:" + obj.title,
    }
    return render(request, 'lists/form.html', page)

def toggleStatusListItemForm(request, item_id):
    if request.method == "GET":
        obj = List.objects.get(id=item_id)
        obj.status = True if obj.status == False else False
        obj.save()
        return redirect('view-list', item_id=obj.list.id)

def deleteListItem(request, item_id):
    item = List.objects.get(id=item_id)
    list_id = item.list.id
    name = f"{item.title} [{item.id}]"
    item.delete()
    messages.info(request, f"The item '{name}' has been deleted!")
    return redirect('view-list', item_id=list_id)