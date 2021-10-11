from django.contrib import admin

from librarybooks.models import library, book, library_user, library_activity, library_book

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('library_name',
                    'city',)
    list_filter = ['library_name', 'city' ]

class BookAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author_name',)
    list_filter = ['title', 'author_name' ]

class LibraryUserAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name' ]

class LibraryActivityAdmin(admin.ModelAdmin):
    list_display = ('library_user',
                    'activity_type',)
    list_filter = ['library_user', 'activity_type' ]

class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ('library',
                    'book',)
    list_filter = ['library', 'book' ]

admin.site.register(library, LibraryAdmin)
admin.site.register(book, BookAdmin)
admin.site.register(library_user, LibraryUserAdmin)
admin.site.register(library_activity, LibraryActivityAdmin)
admin.site.register(library_book, LibraryBookAdmin)