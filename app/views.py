from django.shortcuts import render

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings

from datetime import datetime
from app.models import Persona, Skills, SocialNetwork, TextDescript, Services, Sumary, Project, ProectTech, Experience, \
    ExperienceDetails, EducationsDetails, Education, Awards, Portafolio, Categories


def index(request):
    persona = Persona.objects.all()
    skills = Skills.objects.all().values()
    networks = SocialNetwork.objects.all().values()
    textDescript = TextDescript.objects.all().values()
    services = Services.objects.all().values()
    sumary = Sumary.objects.all().values()
    project = Project.objects.all().values()
    projectTech = ProectTech.objects.all().values()
    experience = Experience.objects.all().values()
    experienceDetails = ExperienceDetails.objects.all().values()
    education = Education.objects.all().values()
    educationsDetails = EducationsDetails.objects.all().values()
    awards = Awards.objects.all().values()
    categories = Categories.objects.all().values()
    portafolio = Portafolio.objects.all()

    print(persona)
    print(portafolio)

    context = {
        'persona': persona[0],
        'skills': skills,
        'linkdin': networks[0],
        'github': networks[1],
        'twitter': networks[2],
        'instagram': networks[3],
        'facebook': networks[4],
        'email': networks[5],
        'textDescript': textDescript[0],
        'services': services,
        'sumary': sumary[0],
        'project': project,
        'projectTech': projectTech,
        'experience': experience,
        'experienceDetails': experienceDetails,
        'education': education,
        'educationsDetails': educationsDetails,
        'awards': awards,
        'sizeAward': len(awards),
        'categories': categories,
        'portafolio': portafolio
    }
    return render(request,'index.html', context)

def detailPortfolio(request, id):
    return render(request, 'portfolio-details.html')


def send_email(email, texto):
    try:
        mailServer = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(settings.EMAIL_HOST_USER)
        mailServer.starttls()
        print(mailServer.ehlo())
        mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado...')

        email_to='sheilafundora04gmail.com'

        #construir el mensaje
        mensaje= MIMEText("""Alguien ha hecho contacto contigo a trves de myPortafolio. 
        Entre al siguiente link para revisarlo: http://yandivd.pythonanywhere.com/listar/contactos/ """+
                          "Correo: "+email+' '+texto)
        mensaje['From'] = settings.EMAIL_HOST_USER
        mensaje['To'] = email_to

        mensaje['Subject'] = 'Te han dejado un mensaje'

        mailServer.sendmail(settings.EMAIL_HOST_USER,email_to, mensaje.as_string())
        print("Correo enviado")

    except Exception as e:
        print(e)