from django.contrib import admin

# Register your models here.
from .models import Contact, Academic, Studentdata,Parentdata, Teacherdata,BCAAttendance,BBAAttendance, AttendanceClass,Examresult, Class, AssignTime, Dept, Course, Assign

admin.site.register(Contact)
admin.site.register(Studentdata)
admin.site.register(Teacherdata)
admin.site.register(Parentdata)
admin.site.register(Examresult)
admin.site.register(Dept)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Assign)
admin.site.register(AssignTime)
admin.site.register(AttendanceClass)
admin.site.register(BCAAttendance)
admin.site.register(BBAAttendance)


@admin.register(Academic)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)