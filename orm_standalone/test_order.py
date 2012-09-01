import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.db import models
from django.db.models import Q
from blog.models import *

#case = StudyOrder.objects.all()
case1 = StudyOrder.objects.filter(author__name="liwei").latest('update_date')
#print case1.update_date
case2 = StudyOrder.objects.filter(Q(author__name="liwei") & ~Q(update_date__exact=case1.update_date)).latest('update_date')
print case1
print case2
