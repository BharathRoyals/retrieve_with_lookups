from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    LOT=Topics.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpages.objects.all()
    LOW=Webpages.objects.filter(TName='Cricket')
    LOW=Webpages.objects.get(TName='Cricket')
    LOW=Webpages.objects.exclude(TName='Hockey')
    LOW=Webpages.objects.all()[1:3:]
    LOW=Webpages.objects.all().order_by(Length('Cricket'))
    LOW=Webpages.objects.all().order_by('-Name')
    LOW=Webpages.objects.all().order_by('Name')
    LOW=Webpages.objects.all().order_by(Length('Name').desc())
    LOW=Webpages.objects.all()
    LOW=Webpages.objects.filter(Name__startswith='B')
    LOW=Webpages.objects.filter(Name__startswith='H')
    LOW=Webpages.objects.filter(Name__endswith='h')
    LOW=Webpages.objects.filter(Email__endswith='.com')
    LOW=Webpages.objects.filter(Name__contains='B')
    LOW=Webpages.objects.filter(Name__in=('Bharath','Hemanth'))
    LOW=Webpages.objects.filter(Q(TName='Cricket')&Q(Name='Bharath'))
    LOW=Webpages.objects.filter(Q(TName='Cricket'))
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_accessrecord(request):
    LOA=AccessRecord.objects.all()
    
    LOA=AccessRecord.objects.filter(Date__gt='2023-10-10')
    LOA=AccessRecord.objects.filter(Date__lt='2023-09-05')
    LoA=AccessRecord.objects.filter(Date__gte='2023-09-25')
    LOA=AccessRecord.objects.filter(Date__lte='2023-06-24')
    LOA=AccessRecord.objects.filter(Date__year='2023')
    LOA=AccessRecord.objects.filter(Date__month='10')
    LOA=AccessRecord.objects.filter(Date__day='24')
    LOA=AccessRecord.objects.filter(Date__year__gt='2021')
    LOA=AccessRecord.objects.filter(Date__month__lte='07')
    LOA=AccessRecord.objects.filter(Date__month__lt='07')
    LOA=AccessRecord.objects.filter(Date__month__gte='07')
   
   
    
    d={'accessrecord':LOA}
    return render(request,'display_accessrecord.html',context=d)




   