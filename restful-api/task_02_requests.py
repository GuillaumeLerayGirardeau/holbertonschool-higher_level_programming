#!/usr/bin/python3
"""
Functions to fetch, print and save posts
"""
import requests
import csv


def fetch_and_print_posts():
    """
    fetch postst from jsonplaceholder, and print them
    """
    post = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {post.status_code}")
    if post.status_code == 200:
        data = post.json()
        for i in data:
            print(i["title"])


def fetch_and_save_posts():
    """
    fetch posts from jsonplaceholder, and save them
    """
    post = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = post.json()
    post_dict = []
    new_post = {}

    for i in data:
        new_post["id"] = i["id"]
        new_post["title"] = i["title"]
        new_post["body"] = i["body"]
        post_dict.append(new_post.copy())

    with open("posts.csv", "w") as file:
        fields = ["id", "title", "body"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(post_dict)
