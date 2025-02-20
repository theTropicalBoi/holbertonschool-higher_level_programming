#!/usr/bin/python3


import requests
import csv


"""
Function to interact with the request library
"""
def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceHolder
    print the status code of the response.
    If the request is successful, parse the fetched data into a JSON obj.
    Iterate through the parsed JSON data and print out the titles of all the posts.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceHolder
    If request if successful, instead of printing titles, structure the data
    into a list of dicts, where each dict represents a post with keys and values for id,
    title and body.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in structured_data:
                writer.writerow(post)