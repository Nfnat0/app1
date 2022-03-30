from django.shortcuts import render
from game.models import Post
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

def post_list(request, posts=None):
    if not posts:
        posts = [Post(no=i, text='test') for i in range(1,10)]
        return render(request, 'game/post_list.html', {'posts': posts})


    posts = [Post(no=i, text='test') for i in range(1,10)]

    return render(request, 'game/post_list.html', {'posts': posts})
