from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from django.template import loader

def image_view(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ImageForm()
    # template = loader.get_template('simple_image/upload_image.html')
    # return HttpResponse(template.render(request))
    return render(request, 'upload_image.html', {'form': form})
def success(request):
    return HttpResponse("Success Uploaded")