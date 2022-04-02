from django.shortcuts import render
from game.models import Post
import requests
import os
from django.http import JsonResponse

def top(request):
    posts = [Post(word=f'test{i}', src='') for i in range(1,10)]
    print('top called')
    return render(request, 'game/post_list.html', {'posts': posts})


def search(request):
    print('search called')
    print(request.POST)
    text = request.POST['choice']
    print(text)
    url = 'https://www.google.co.jp/search'

    # グーグルへ接続
    req = requests.get(url, params={'q': 'パイソン'})

    # アドレス取得
    print(req.url)
    # 検索結果取得
    print(req.text)

def ajax_post_search(request):
    word = request.POST.get('word')
    print(word)
    d = {
        'src': f'test_src_{word}',
    }
    return JsonResponse(d)
