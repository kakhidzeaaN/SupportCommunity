from django.contrib import admin
from .models import Topic, Category, User, Meeting, Conversation, Comment

admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Meeting)
admin.site.register(Conversation)
admin.site.register(Comment)
