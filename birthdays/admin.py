from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birthday_display', 'level', 'phone_number', 'held_office', 'created_at']
    list_filter = ['birth_month', 'level', 'held_office', 'gender']
    search_fields = ['full_name', 'email', 'phone_number', 'alias']
    ordering = ['birth_month', 'birth_day']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone_number', 'gender', 'alias')
        }),
        ('Birthday Details', {
            'fields': ('birth_month', 'birth_day')
        }),
        ('Academic Information', {
            'fields': ('level', 'held_office', 'office_position')
        }),
        ('Profile', {
            'fields': ('profile_picture',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )