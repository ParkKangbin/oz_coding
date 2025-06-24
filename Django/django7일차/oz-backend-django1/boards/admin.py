from django.contrib import admin
from .models import Board
# Register your models here.
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display =  ('title','writer','date','likes','content','updated_at','created_at')
    list_filter = ('date','writer')
    search_fields = ('title','content')
    ordering = ('-date',)
    readonly_fields = ('writer',)
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('추가 옵션', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    )
    list_per_page = 10
    

    actions = ('increment_likes',)

    def increment_likes(self, request, quertset):
        
        for board in quertset:
            board.likes += 1
            board.save()

    increment_likes.short_description = "선택된 게시글 좋아용 증가?"