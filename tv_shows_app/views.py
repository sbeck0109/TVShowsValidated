from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show



def index(request):
    return render(request, "index.html")

def add_a_new_show(request):
    return render(request, "add_a_new_show.html")

def create(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new")
        else:
        # print(request.POST)
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']
            this_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
            this_show_id = this_show.id
            messages.success(request, "TV show succesfully created")
            return redirect (f'/shows/{this_show.id}')
def view_this_show(request):
    request.POST
    context = {
    "all_shows" : Show.objects.all()
    }
    return redirect(request, '/shows')
def display_show(request, this_show_id):
    context = {
    "this_show" : Show.objects.get(id=this_show_id)
    }
    return render(request, 'display_one_show.html', context)
def view_all_shows(request):
    context = {
    "all_shows" : Show.objects.all()
    }
    return render(request, 'all_shows.html', context)
def edit(request, this_show_id):
    print(this_show_id)
    context = {
    "all_shows" : Show.objects.all(),
    "this_show" : this_show_id
    }
    return render(request, "edit_show.html", context)
def update(request, this_show_id):
    edit_this_show = Show.objects.get(id=this_show_id)
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{this_show_id}/edit')
        else:
            edit_this_show = Show.objects.get(id = this_show_id)
            edit_this_show.title = request.POST['title']
            edit_this_show.network = request.POST['network']
            edit_this_show.release_date = request.POST['release_date']
            edit_this_show.description = request.POST['description']
            edit_this_show.save()
            messages.success(request, "Show succcessfully updated")
            return redirect(f'/shows/{edit_this_show.id}')


def destroy(request, this_show_id):
    this_show = Show.objects.get(id=this_show_id)
    this_show.delete()
    return redirect ('/shows')
