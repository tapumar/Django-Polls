from django.contrib import admin
from .models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information',
            {
                'fields': ['pub_date'],
                'classes':['collapse']
            }
         ),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    list_display = ('question', 'pub_date')


admin.site.register(Poll, PollAdmin)
