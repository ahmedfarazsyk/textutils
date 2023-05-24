from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    text_rec = request.POST.get('text', 'default')
    rempunc = request.POST.get('rempunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    remline = request.POST.get('remline', 'off')
    remspace = request.POST.get('remspace', 'off')
    charcount = request.POST.get('charcount', 'off')
    if rempunc == 'on':
        analyzed = ""
        punctuations = '''!@#$%^&*()~}{][":';?><,./\|+_=-'''
        for char in text_rec:
            if char not in punctuations:
                analyzed = analyzed + char
        dict = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        text_rec = analyzed

    if capitalize == 'on':
        analyzed = ''
        for char in text_rec:
            analyzed = analyzed + char.upper()
        dict = {'purpose': 'Capitalize text', 'analyzed_text': analyzed}
        text_rec = analyzed

    if remline == 'on':
        analyzed = ''
        for char in text_rec:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        dict = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        text_rec = analyzed

    if remspace == 'on':
        analyzed = ''
        list = text_rec.split(' ')
        for item in list:
            if item != '':
                analyzed+=item+' '
        dict = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        text_rec = analyzed

    if charcount == 'on':
        count = 0
        analyzed = text_rec
        for char in text_rec:
            count += 1

        dict = {'purpose': 'Counting Characters', 'analyzed_text': f'{analyzed}\n'
                                                                   f'The number of Characters in string = {count}'}
        return render(request, 'analyze_text.html', dict)
    if rempunc != 'on' and remline != 'on' and remspace != 'on' and capitalize != 'on' and charcount != 'on':
        return HttpResponse("<h1>Error</h1>")
    return render(request, 'analyze_text.html', dict)
