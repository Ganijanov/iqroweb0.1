from django.shortcuts import render, redirect
import telebot
import datetime


bot = telebot.TeleBot("7103426824:AAHYGRa3bfg3oID7mZVDW09ny_LaPo7Lszg", parse_mode=None)
print(bot.message_handler)
def sender(text):
    bot.send_message('-4599062176', text)


def botforlid(request, next_page=None):
    template = 'index.html'  # Шаблон по умолчанию  
    if next_page == 'index2':
        template = 'index2.html'
        if request.POST.get('name')  and request.POST.get('email')  : 
            txt = f"Ism : {request.POST.get('name')}\nRaqam : {request.POST.get('email')}\n"
            sender(txt)
    return render( request, template)

