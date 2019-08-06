from django.shortcuts import render, redirect
from . models import *
from . avitomp4 import *
from django.conf import settings

# Create your views here.
def index(request):
	device_name = request.environ['GNOME_SHELL_SESSION_MODE']
	language = request.environ['LANGUAGE']
	server_name = request.environ['SERVER_NAME']
	Port = request.environ['SERVER_PORT']
	var = request.headers['User-Agent']
	var1 = var.split()
	if "Chrome" in var:
		print(var1[-2])
	else:
		print(var1[-1])
	return render(request, "myapp/index.html", {'device_name' : device_name,
		'language' : language, 
		'server_name' : server_name, 
		'Port' : Port})


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


def showmedia(request):
	return render(request, 'myapp/all_media_file.html')


def allmedia(request):
	if request.method == "POST":
		name = request.POST.get("name")
		media = request.FILES.getlist("mediafile")
		for i in media:
			if i.name.lower().endswith(('.png', '.jpg', '.jpeg')):
				obj = AllMedia(name=name, media_file=i, file_types='I')
			elif i.name.lower().endswith(('.mp4', '.avi')):
				obj = AllMedia(name=name, media_file=i, file_types='V')
			elif i.name.lower().endswith(('.mp3')):
				obj = AllMedia(name=name, media_file=i, file_types='A')
			obj.save()
	return redirect(allmedia_success)


def allmedia_success(request):
	if request.method == "GET":
		obj = AllMedia.objects.all()
		return render(request, "myapp/allmedia.html", {"AllMedia": obj})


def success(request):
	if request.method == "GET":
		obj = Video.objects.all()
		return render(request, "myapp/video_show.html", {"data": obj})	
