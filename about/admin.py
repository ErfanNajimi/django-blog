from django.contrib import admin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    summernote_fields = ('content',)

# Register your models here.
