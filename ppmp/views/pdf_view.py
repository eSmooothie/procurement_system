from ctypes import alignment
import logging
import io
import os
import theme
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Frame, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import reportlab.lib.colors as colors
from ..helper import *



logger = logging.getLogger("file_log")

def canvas_init(buffer):
    global page_height, page_width, font_size, font, margin_top, margin_right
    font = "Times-Roman"
    font_size = 12
    page_width, page_height = letter
    margin_top = page_width-inch
    margin_right = page_height-inch

    _canvas = canvas.Canvas(buffer, pagesize=landscape(letter))
    _canvas.setAuthor(author="Sherwin Sandoval")
    _canvas.setTitle(title="ppmp")
    _canvas.setFont(font, font_size)
    _canvas.translate(inch/2, inch/2) # set margin

    return _canvas

# drawString(x,y,text)
def canvas_header(canvas):
    story = []
    headerStyle = ParagraphStyle("myStyle", alignment=1)
    
    msu_iit_seal = os.path.dirname(theme.__file__) + "\\static\\images\\logo\\msu_iit_seal.png"
    qr_code = os.path.dirname(theme.__file__) + "\\static\\images\\logo\\sample_qr_code.png"
    canvas.drawInlineImage(msu_iit_seal, 0, margin_top-70, width=70, height=70)
    
    story.append(Paragraph("Mindanao State University", headerStyle))
    story.append(Paragraph("ILIGAN INSTITUTE OF TECHNOLOGY", headerStyle))

    f = Frame(70, margin_top-70, page_height - (70*2 + inch), 70, showBoundary=1)
    f.addFromList(story,canvas)

    canvas.drawInlineImage(qr_code, margin_right-70, margin_top-70, width=70, height=70)

   
def ppmp_detail(canvas):
    details = []
    style = ParagraphStyle("myStyle")
    details.append(Paragraph("PPMP DETAILS HERE", style))

    f = Frame(0, margin_top-140, page_height - inch, 70, showBoundary=1)
    f.addFromList(details,canvas)

def ppmp_table(canvas):
    table_header = []
    table_data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
    
    table_style = [
        ('GRID',(0,0),(-1,-1),1,colors.black),
    ]

    t = Table(table_data, style=table_style)
    
    t.wrapOn(canvas, page_height - inch, 250)
    t.drawOn(canvas, 0, margin_top - 210)
    

@login_required(login_url='login_user')
def pdf(request):
    # if request.method == "POST":
    cc_id = 1
    ppmp_year = 2022
    ppmp_id = 13
    cat_id = 912

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    canvas = canvas_init(buffer)
    
    canvas_header(canvas)
    ppmp_detail(canvas)
    ppmp_table(canvas)

    canvas.showPage()
    canvas.save()

    buffer.seek(0)

    filename = "test.pdf"

    return FileResponse(buffer, as_attachment=False, filename=filename)
        
    # return Response(None, status=status.HTTP_400_BAD_REQUEST)