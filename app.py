from flask import Flask, render_template, request, redirect
import tkinter as tk
from tkinter.messagebox import showinfo
from main import Finding

app = Flask(__name__)
finder = Finding

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about-me/")
def about():
    return render_template("about.html")

@app.route("/attach-file-instruction/")
def attach():
    return render_template("attach.html")

@app.route("/finding-play-button/")
def play():

    return render_template("play.html")

