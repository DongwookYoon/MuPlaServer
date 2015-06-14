import os
import shutil
import json
from django.http import HttpResponse
if __name__ != "__main__":
    from django.views.decorators.csrf import csrf_exempt
from mupla_cython import mupla_cython
from PyPDF2 import PdfFileMerger, PdfFileReader

def run_mupla(dir_path):
    pdfs = []
    filen = 0

    while(True):
        pdf_path = dir_path+"/"+str(filen)+".pdf"
        if os.path.isfile(pdf_path):
            pdfs.append(pdf_path)
            filen += 1
        else:
            break

    merged_pdf_path = dir_path+"/merged.pdf"
    if len(pdfs) == 0:
        raise Exception("No PDF file available")
    elif len(pdfs) == 1:
        shutil.copyfile(pdfs[0], merged_pdf_path)
    else:
        merger = PdfFileMerger()
        for pdf in pdfs:
            with open(pdf, "rb") as f:
                merger.append(PdfFileReader(f))
                f.close()
        with open(merged_pdf_path, "wb") as output:
            merger.write(output)
            output.close()

    js = mupla_cython.PyMuPlaRun(merged_pdf_path)
    if len(js) == 0:
        raise Exception("Invalid PDF file")
    with open(dir_path+"/merged.js", 'w') as f:
        f.write(json.dumps(js))
        f.close()

@csrf_exempt
def get_pdf_post(request):
    try:
        if request.POST["mode"] ==  "MergePdfs":
            run_mupla("../pdfs/"+request.POST["uuid"])
            return HttpResponse("succeed", content_type="application/json")
        else:
            raise Exception("Invalid request to the MuPla server")

    except Exception as e:
        print "Exception"
        print e
        return HttpResponse(str(e), content_type="application/json")

if __name__ == "__main__":
    run_mupla("./pdfs/a2d0ce10-12d7-11e5-abf8-d7cd6cb0153a")