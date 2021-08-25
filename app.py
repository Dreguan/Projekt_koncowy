from flask import Flask, render_template, request, redirect
import tkinter as tk
from tkinter.messagebox import showinfo

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about-me/")
def about():
    return render_template("about.html")

@app.route("/attach-file-instruction/")
def attach():
    return render_template("attach.html")

