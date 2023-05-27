from django.contrib import admin

from .models import *

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Timetable)
admin.site.register(Day)
admin.site.register(TimeSlot)
admin.site.register(Attendance)
admin.site.register(Status)
