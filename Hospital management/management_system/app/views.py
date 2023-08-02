
from django.shortcuts import render, redirect
from .forms import AdminCreationForm
from .models import Admin
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request,'base.html')


def create_admin(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return admin_list(request)
    else:
        form = AdminCreationForm()
    return render(request, 'create_admin.html', {'form': form})
@login_required
def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'admin_list.html', {'admins': admins})

def admin_edit(request, pk):
    admin = Admin.objects.get(pk=pk)
    if request.method == 'POST':
        form = AdminCreationForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('admin_list')
    else:
        form = AdminCreationForm(instance=admin)
    return render(request, 'admin_edit.html', {'form': form})

def admin_delete(request, pk):
    admin = Admin.objects.get(pk=pk)
    if request.method == 'POST':
        admin.delete()
        return admin_list(request)
    return render(request, 'admin_delete.html', {'admin': admin})








