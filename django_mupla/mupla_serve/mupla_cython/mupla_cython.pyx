
cdef extern from "<mupla.h>":
    ctypedef struct MuPlaRect:
        float l;
        float t;
        float r;
        float b;

    ctypedef struct MuPlaTextLine:
        MuPlaRect bbox;
        int len;
        int* text;

    ctypedef struct MuPlaTextBlock:
        MuPlaRect bbox;
        int len;
        MuPlaTextLine* lines;

    ctypedef struct MuPlaPage:
        MuPlaRect bbox;
        int len_t;
        MuPlaTextBlock* tblocks;

    ctypedef struct MuPlaDoc:
        int len;
        MuPlaPage* pages;

    MuPlaDoc MuPlaRun(char*)

cdef JSONIfy_Rect(MuPlaRect r):
    return [r.l, r.t, r.r, r.b]

cdef JSONify_Line(MuPlaTextLine line):
    text = u""
    for i in range(0, line.len):
        text += unichr(line.text[i])
    return {"bbox": JSONIfy_Rect(line.bbox), "text": text}

cdef JSONify_TextBlock(MuPlaTextBlock tblock):
    js_lines = []
    for i in range(0, tblock.len):
        js_lines.append(JSONify_Line(tblock.lines[i]))
    return {"bbox": JSONIfy_Rect(tblock.bbox), "lines": js_lines}

cdef JSONify_Page(MuPlaPage page):
    js_tblocks = []
    for i in range(0, page.len_t):
        js_tblocks.append(JSONify_TextBlock(page.tblocks[i]))

    return {"bbox": JSONIfy_Rect(page.bbox), "tblocks":js_tblocks}

cdef JSONify_Doc(MuPlaDoc doc):
    js_doc  = []
    for i in range(0, doc.len):
        js_doc.append(JSONify_Page(doc.pages[i]))
    return js_doc

def PyMuPlaRun(py_pdf_path): 
    cpdef char* c_pdf_path = py_pdf_path;
    cdef MuPlaDoc cmupladoc;
    try:
        cmupladoc = MuPlaRun(c_pdf_path)
        return JSONify_Doc(cmupladoc)
    except:
        return []
