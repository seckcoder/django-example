import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.db import models
from blog.models import *
author = Author.objects.all()
print author
