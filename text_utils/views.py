#I created this file
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def analyze(request):
    entered_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    removenumber = request.POST.get('removenumbers')
    removenewline = request.POST.get('removenewline')
    removespace = request.POST.get('removespace')
    capitalizeall = request.POST.get('capitalizeall', 'off')
    reversetext = request.POST.get('reversetext')
    countcharacter = request.POST.get('countchar')
    task = ''
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ''
        for char in entered_text:
         if char not in punctuations:
            analyzed_text += char
        entered_text = analyzed_text   
        task = 'removing punctuations' 
        context = {
            'task' : task,
            'alert_text' : 'success',
            'analyzed_prefix' : 'Success!',
            'analyzed_text' : analyzed_text
        }
    if capitalizeall == 'on':
        analyzed_text = ''
        analyzed_text = entered_text.upper()
        entered_text = analyzed_text
        task += '|| capitalizing all characters'
        context = {
        'task' : task,
        'alert_text' : 'success',
        'analyzed_prefix' : 'Success!',
        'analyzed_text' : analyzed_text
    }
    if removenewline == 'on':
        analyzed_text = ''
        # analyzed_text = entered_text.replace("\n","")
        for char in entered_text:
            if char != '\r' and char!= '\n':
                analyzed_text += char
        entered_text = analyzed_text
        task += '|| removing new line'
        context = {
            'task' : task,
            'alert_text' : 'success',
            'analyzed_prefix' : 'Success!',
            'analyzed_text' : analyzed_text
        }
    if removespace == 'on':
        analyzed_text = ''
        for index, char in enumerate(entered_text):
            if not(entered_text[index] == ' ' and entered_text[index+1] == ' '):
                analyzed_text += entered_text[index]
        entered_text = analyzed_text
        task += '|| removing extra spaces'   
        context = {
            'task' : task,
            'alert_text' : 'success',
            'analyzed_prefix' : 'Success!',
            'analyzed_text' : analyzed_text
        } 

    if removenumber == 'on':
        analyzed_text = ''
        number = '0123456789'
        for char in entered_text:
            if char not in number:
                analyzed_text += char
        entered_text = analyzed_text
        task += '|| removing numbers'
        context = {
            'task' : task,
            'alert_text' : 'success',
            'analyzed_prefix' : 'Success!',
            'analyzed_text': analyzed_text
        }    

    if reversetext == 'on':
        analyzed_text = ''
        analyzed_text = entered_text[::-1]
        task += '|| reversing characters'
        context = {
            'task' : task,
            'alert_text' : 'success',
            'analyzed_prefix' : 'Success!',
            'analyzed_text' : analyzed_text
        }

    if(not(removepunc=='on' or capitalizeall == 'on' or removenewline == 'on' or removespace == 'on' or removenumber == 'on' or reversetext == 'on')):
        context = {
            'task' : 'getting error',
            'alert_text' : 'danger',
            'analyzed_prefix' : 'Error!',
            'analyzed_text' : 'We are unable to process your request. Please select any one operation.'
        } 
    return render(request, 'analyze.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html') 