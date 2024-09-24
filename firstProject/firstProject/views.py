# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text' , 'defult')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    
    if removepunc == 'on':
        punctution = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctution:
                analyzed = analyzed + char
        params = {'Purpose' : 'Removed Punctutions' , 'analyzed_text' : analyzed }
        return render(request , 'analyze.html' , params)

    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'Purpose' : 'Change To Uppercase' , 'analyzed_text' : analyzed }
        return render(request , 'analyze.html' , params)
    
            
            
        
        
    