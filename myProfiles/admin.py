from django.contrib import admin
from myProfiles.models import UserProfile, UserImages, UserProject, UserSupport, UserFiles

class UserFileInline(admin.StackedInline):
    model = UserFiles
    extra = 1

class UserImageInline(admin.StackedInline):
    model = UserImages
    extra = 1

class UserProjectInline(admin.StackedInline):
    model = UserProject
    extra = 1

class UserSupportInline(admin.StackedInline):
    model = UserSupport
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [ UserProjectInline, UserSupportInline, UserImageInline, UserFileInline]

admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(UserImages)
admin.site.register(UserFiles)
admin.site.register(UserProject)
admin.site.register(UserSupport)

