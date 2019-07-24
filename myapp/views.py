from django.shortcuts import render, redirect
from . models import *
from . avitomp4 import *
from django.conf import settings

# Create your views here.
def index(request):
	print(settings.BASE_DIR)
	return render(request, "myapp/index.html")


def getvideo(request):
	if request.method == "POST":
		name = request.POST.get("name")
		file = request.FILES["video_file"]
		obj = Video(name=name, videofile=file)
		obj.save()
		file_path = "/home/user/newproject/video/media/videos/"+ str(file)
		mp4_file = convert_avi_to_mp4(file_path, name)
		mp4file = 'videos/'+ name + ".mp4"
		# obj2 = Video.objects.filter(video=file)
		obj.mp4file = mp4file
		obj.save()
		mp4_file.close()
		return redirect(success)
	else:
		return redirect(index)
	

def success(request):
	if request.method == "GET":
		obj = Video.objects.all()
		return render(request, "myapp/video_show.html", {"data": obj})	
