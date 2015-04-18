from django.contrib import admin
from myProfiles.models import UserProfile, UserImages, UserProject

class UserImageInline(admin.StackedInline):
    model = UserImages

class UserProjectInline(admin.StackedInline):
    model = UserProject
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    inlines = [ UserProjectInline, UserImageInline, ]

admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(UserImages)
admin.site.register(UserProject)

