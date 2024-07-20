from .models import Conversation, Category


def seeder_func():
    categories = ['General', 'Family', 'Health', 'Veteran', 'Man/Father', 'Postpartum', 'Brain injury', 'Disabilities']
    conversations = ['Face to face', 'Online meeting']

    for category in categories:
        if not Category.objects.filter(heading=category):
            new_category = Category(heading=category)
            new_category.save()

    for conversation in conversations:
        if not Conversation.objects.filter(type=conversation):
            new_conversation = Conversation(type=conversation)
            new_conversation.save()



