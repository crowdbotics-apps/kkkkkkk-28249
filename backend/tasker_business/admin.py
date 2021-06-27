from django.contrib import admin
from .models import TaskerSkill, BusinessPhoto, Timeslot, TaskerAvailability

admin.site.register(Timeslot)
admin.site.register(TaskerSkill)
admin.site.register(BusinessPhoto)
admin.site.register(TaskerAvailability)

# Register your models here.
