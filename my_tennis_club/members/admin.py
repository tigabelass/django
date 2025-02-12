from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ("id","firstname", "lastname","phone","joined_date",)
    prepopulated_fields = {"slug" :("firstname","lastname")}

admin.site.register(Member, MemberAdmin)
