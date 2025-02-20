#!/usr/bin/python3

import requests
import csv

"""
Use requests library to request and process http responses,
Parses and manipulate JSON data using Python.
"""


def fetch_and_print_posts():
    """
    Fetch all posts from JSON Placeholder
    Print Status Code if 200 and parse it to JSON Object
    Print out the file title.
    """
    response = requests.get(url="https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch all post from JSON PlaceHolder
    If request is successful, structure the data into a list of dicts
    where each dict represents a post with keys and values for id,
    title and body.
    """
    response = requests.get(url="https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        structured = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])

            writer.writeheader()
            writer.writerows(structured)
