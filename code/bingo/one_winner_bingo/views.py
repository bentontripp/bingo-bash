from django.shortcuts import render
from django.http import HttpResponse
import io
from one_winner_bingo import models as app_models
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak

# Create your views here.
def index(request):
    return render(request, "one_winner_bingo/index.html")

def original_bingo(request):
    return render(request, "one_winner_bingo/pages/original_bingo.html")

def custom_bingo(request):
    return render(request, "one_winner_bingo/pages/custom_bingo.html")


# from django.http import FileResponse
# return FileResponse(buffer, as_attachment=True, filename='BINGO_CARDS.pdf')

def get_custom_bingo(request):
    a = request.POST.getlist('arr[]')
    arr_lis = app_models.custom_shuff(a, 15, True)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="BINGO_CARDS.pdf"'
    buffer = io.BytesIO() 
    doc = SimpleDocTemplate(buffer, pagesize = letter)
    # container for the 'Flowable' objects
    elements = []
    for arr in arr_lis:
        data = arr
        t = Table(data, 5 * [1.5 * inch], 6 * [1.4 * inch])
        # from (column, row) to (column, row)
        t.setStyle(TableStyle([('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                               ('FONTSIZE', (0,0), (-1,0), 15),
                               ('TEXTCOLOR', (0,1), (-1,-1), colors.black),
                               ('FONTSIZE', (0,1), (-1,-1), 14),
                               ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                               ('VALIGN', (0,0), (-1,-1),'MIDDLE'),
                               ('TEXTCOLOR', (0,0), (-1,0), colors.white),
                               ('BACKGROUND', (0,0), (-1,0), colors.black),
                               ('BACKGROUND', (0,1), (-1,-1), colors.Color(230/255, 220/255, 225/255)),
                               ('INNERGRID', (0,0), (-1,0), 0.7, colors.white),
                               ('INNERGRID', (0,1), (-1,-1), 0.7, colors.black),
                               ('BOX', (0,0), (-1,-1), 0.7, colors.black),
                               ]))
        elements.extend([t, PageBreak()])
    # write the document to disk
    doc.build(elements)
    response.write(buffer.getvalue())
    buffer.close()
    print(response)
    return response
    