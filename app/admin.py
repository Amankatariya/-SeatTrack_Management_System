from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Classroom)
admin.site.register(Seat)
admin.site.register(SeatAllocation)
# admin.site.register(Abstracttime)
# table+
# @admin.register(StudentModel)
# class Studentadmin(admin.ModelAdmin):
#     list_display=['id','name','email','classroom','seat_no']
#     search_fields=('name',)
#     ordering=('name',)

# @admin.register(BatchModel)
# class Batchadmin(admin.ModelAdmin):
#     list_display=['id','name','seat_no']
#     search_fields=('name',)
#     ordering=('name',)


# @admin.register(SeatModel)
# class Seatadmin(admin.ModelAdmin):
#     list_display=['id','name' ,'seat_no']


