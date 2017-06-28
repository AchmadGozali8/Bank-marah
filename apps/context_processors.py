from .models import Post

def count_level(request):
    user_id = request.user.id
    posts = Post.objects.get(id=user_id)

    HIGH = 1

    high = 0
    low = 0

    for p in posts:
        if p.anger_id == HIGH:
            high += 1
        low +=1

    context={
        'high':high,
        'low':low,
    }

    return context
