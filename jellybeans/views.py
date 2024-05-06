from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AddFlavorForm
from .models import JellybeanFlavor

# Retrieve all objects from database in alphabetical order
def index(request):
    jellybeans = JellybeanFlavor.objects.all().order_by('flavor')

    return render(request, 'jellybeans/index.html', {'jellybeans': jellybeans})

# Either render add flavor page or save a new flavor on submission
def add_flavor(request):
    if request.method == 'POST':
        form = AddFlavorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddFlavorForm()
    return render(request, 'jellybeans/addflavor.html', {'form': form})

# Delete flavor from database and S3
def delete_flavor(request, pk):
    jellybean = get_object_or_404(JellybeanFlavor, pk=pk)
    jellybean.s3_image.delete()
    jellybean.delete()
    messages.success(request, 'Jellybean flavor deleted successfully!')
    return redirect('index')

# Either render edit flavor page or update flavor based on primary key (ID)
def edit_flavor(request, pk):
    jellybean = get_object_or_404(JellybeanFlavor, pk=pk)
    if request.method == 'POST':
        form = AddFlavorForm(request.POST, request.FILES, instance=jellybean)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddFlavorForm(instance=jellybean)
    return render(request, 'jellybeans/editflavor.html', {'form': form})
