from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

def index(request):
    context = {
        "message":"Bonjour et bienvenue dans ma bibliothèque de Manga et animés",
        "numberNews" : 15,
        "userList" : ["Tata","Titi","Toto"],
        "publication" : datetime.datetime.now(),
        "d1" : datetime.datetime.now(),
        "d2" : datetime.datetime.now(),
        "username":"Jack Sparrow",
        "numberOfNews":12,
        "link":"https://www.youtube.com/watch?v=xNPiqBCftc8&list=PLrSOXFDHBtfED_VFTa6labxAOPh29RYiO&index=6",
        "lk":"N'oubliez pas ma recette originale sur http://mescrepes.fr et abonnez-vous !"
        }
    template = loader.get_template("mangalib/index.html")
    return HttpResponse(template.render(context, request))
