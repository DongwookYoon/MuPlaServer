import os
import shutil
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mupla_cython import mupla_cython
from PyPDF2 import PdfFileMerger

def upload(filepath):
    js = mupla_cython.PyMuPlaRun("../pdfs/"+filepath)
    if len(js) == 0:
        raise Exception("Invalid PDF file")
    f = open("../pdfs/"+filepath+".js",'w')
    f.write(json.dumps(js))
    f.close()
    return HttpResponse("succeed", content_type="application/json")

def merge(myuuid):
    path = "../pdfs/"+myuuid
    l = []
    for dir, dirs, files in os.walk(path):
        for file in files:
            fpath = os.path.join(dir, file)
            fn, fext = os.path.splitext(file)
            if fext == ".pdf":
                l.append(fpath)

    output_fname = path+"/merged.pdf"
    if len(l) == 1:
        shutil.copyfile(l[0], output_fname)
    else:
        merger = PdfFileMerger()
        for fpath in l:
            f = open(fpath, "rb")
            merger.append(f)
            f.close()
        output = open(output_fname, "wb")
        merger.write(output)
        output.close()
    return HttpResponse("succeed", content_type="application/json")

@csrf_exempt
def get_pdf_post(request):
    try:
        if request.POST["mode"] ==  "UploadFile":
            return upload(request.POST["filepath"])
        if request.POST["mode"] ==  "MergePdfs":
            return merge(request.POST["uuid"])

    except Exception as e:
        print "Exception"
        print e
        return HttpResponse(str(e), content_type="application/json")
