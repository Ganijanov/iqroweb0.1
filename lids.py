from django.shortcuts import render, redirect
import telebot
import datetime


bot = telebot.TeleBot("7103426824:AAHYGRa3bfg3oID7mZVDW09ny_LaPo7Lszg", parse_mode=None)
def sender(text):
    bot.send_message('-1', text)


def botforlid(request, next_page=None):
    
    txt = f"Ism : {request.POST.get('name')}\nRaqam : {request.POST.get('email')}\n"
    template = 'index.html'  # Шаблон по умолчанию
    if next_page == 'index2':
        template = 'index2.html'
    # sender(txt)
    print(txt)
    return render( request, template)

