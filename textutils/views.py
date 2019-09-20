# this file is not auto generated.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','Default')
    if len(text.strip()) == 0:
        return HttpResponse("Error Please Enter Text.")
    rmvpunc = request.POST.get('removepunc',"off")
    rmvwhitespace = request.POST.get('whitespace','off')
    rmvnewline= request.POST.get('newlineremover', 'off')
    cnvrtUppercase= request.POST.get('Uppercase', 'off')
    letterwordcount = request.POST.get('letterwordcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    before = 'Before Processing data word count - '+str(len(text.split(' ')))+' and total letter count - '+str(len(text))
    temp = ''
    if rmvpunc == 'on':
        for char in text:
            if char not in punctuations:
                temp = temp + char
        text = temp

    if cnvrtUppercase == 'on':
        print('inside converter')
        temp = ''
        for char in text:
            temp = temp + char.upper()
        text = temp

    if rmvnewline == 'on':
        temp = ''
        for char in text:
            if char != '\n' and char !='\r':
                temp = temp + char
        text = temp

    if rmvwhitespace == 'on':
        temp = ''
        for indx,char in enumerate(text):
            if not(text[indx]==' ' and text[indx+1]==' '):
                temp = temp + char
        text = temp

    after = 'After Processing data word count - '+str(len(text.split()))+' and total letter count - '+str(len(text))

    if letterwordcount == 'on':
        text = text + '\n' + before + '\n' + after

    if rmvwhitespace != 'on' and rmvnewline != 'on' and rmvpunc != 'on' and cnvrtUppercase != 'on' and letterwordcount != 'on':
        return HttpResponse("Error.! choose atleast one Option")

    analyzed = text
    params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html',params)