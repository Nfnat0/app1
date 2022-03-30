from django.shortcuts import render

def post_list(request):
    posts = [1, 2, 3]

    return render(request, 'game/post_list.html', {'posts': posts})
