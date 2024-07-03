from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload/upload.html", {"image_url": image_url})
    return render(request, "upload/upload.html")


def my_json_view(request):
    # Example data to return as JSON
    data = {"Status": "Live"}
    return JsonResponse(data)
