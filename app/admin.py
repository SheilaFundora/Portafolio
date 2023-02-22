from django.contrib import admin

# Register your models here.
from app.models import Persona, TextDescript, SocialNetwork, Sumary, Project, ExperienceDetails, \
    ProectTech, Skills, Experience, Education, EducationsDetails, Portafolio, PortafolioIMG, Services, Awards, \
    Categories

admin.site.register(Persona)
admin.site.register(TextDescript)
admin.site.register(SocialNetwork)
admin.site.register(Skills)
admin.site.register(Sumary)
admin.site.register(Project)
admin.site.register(ProectTech)
admin.site.register(Experience)
admin.site.register(ExperienceDetails)
admin.site.register(Education)
admin.site.register(EducationsDetails)
admin.site.register(Portafolio)
admin.site.register(PortafolioIMG)
admin.site.register(Services)
admin.site.register(Awards)
admin.site.register(Categories)

