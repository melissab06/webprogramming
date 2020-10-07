from django.shortcuts import render, redirect
from django.conf import settings
import os
from django.http import HttpResponse
from django.utils.encoding import force_text
import re

# Create your views here.

def index(request):
    dirList = os.listdir(settings.MEDIA_ROOT)
    context = {"dir":dirList}
    return render(request, "updown/index.html", context)

def get_valid_filename(s):
    """
    Returns the given string converted to a string that can be used for a clean
    filename. Specifically, leading and trailing spaces are removed; other
    spaces are converted to underscores; and anything that is not a unicode
    alphanumeric, dash, underscore, or dot, is removed.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = force_text(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

def upload(request):
    if request.method == "POST":
        for x in request.FILES.getlist("files"):
            y = get_valid_filename(x)
            upLoadFile = open(settings.MEDIA_ROOT + "\\" + str(y), "wb")
            print(upLoadFile)
            for chunk in x.chunks():
                #print("chunk: ", chunk)
                upLoadFile.write(chunk)
        return redirect("updown:index")
    else: 
        return render(request, "updown/upload.html")

def download(request, test):
    #path = "test.txt"
    #path = "test.xlsx"
    #path="test.png"
    file_path = os.path.join(settings.MEDIA_ROOT, test)
    print("file_path: ", file_path)
    test = urllib.parse.quote(test)
    if os.path.exists(file_path): #해당 파일 존재시 true
        readFile = open(file_path, "rb")
        response = HttpResponse(readFile.read())
        response['Content-Disposition'] = 'attachment; filename=' +test
        response['Content-type'] = mimetypes.guess_type(test)[0]

        #response['Content-type'] = 'image/png' #이미지
        #response['Content-type'] = 'text/plain' #텍스트
        #response['Content-type'] = 'application/vnd.ms-excel' #엑셀
        
        return response
