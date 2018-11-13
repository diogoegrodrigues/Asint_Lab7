from flask import Flask
from flask import render_template, jsonify
from flask import request
import requests
import bookDB


def get_func():
	l=input("mete o id: ")
	r = requests.get("http://127.0.0.1:5000/Books/"+l)
	print(r.status_code)
	data = r.json()
	print(data)

def post_func():
	payload = {"author":"Joao","title":"Titulo 1","year":2021}
	r = requests.post("http://127.0.0.1:5000/Books", json=payload)
	print(r.text)

get_func();
post_func();