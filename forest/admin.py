from django.contrib import admin

# Register your models here.
from forest.models import Forest, Tree, Event

admin.site.register(Forest)
admin.site.register(Tree)
admin.site.register(Event)
