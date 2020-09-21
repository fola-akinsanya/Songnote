from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm

# Create your views here.
#def upload_song_view(request, *args, **kwargs):
	#if request.method == 'POST':
		#uploaded_song = request.FILES['song']
		#fs=FileSystemStorage()
		#fs.save(uploaded_song.name, uploaded_song)
	#return render(request,"upload_song.html", {})


def upload_song_view(request):
	if request.method == "POST":
		upload_form = UploadForm(request.POST,request.FILES)
		if upload_form.is_valid():
			upload_form.save()
			return redirect("upload success")
	else:
		upload_form =UploadForm()
	return render(request, "upload_song.html", {'upload_form': upload_form})