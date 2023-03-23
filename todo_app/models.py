from django.db import models

from universaldjango.models import Universal

class Todo(Universal):
    attributes = ["title", "content"]


