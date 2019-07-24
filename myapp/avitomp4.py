from subprocess import check_output, STDOUT, CalledProcessError
import os

def convert_avi_to_mp4(avi_file_path, output_name):
	print("avi_file_path", avi_file_path, output_name)
	video_file = os.popen("ffmpeg -i '{input}' \
	 -c:v libx264 -crf 23 -profile:v baseline -level 3.0 -pix_fmt yuv420p \
	  -c:a aac -ac 2 -b:a 128k \
	   /home/user/newproject/video/media/videos/'{output}.mp4'".format(input = avi_file_path, output = output_name))
	
	return video_file
