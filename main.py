# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:53:29 2024

@author: James
"""

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('templates/home.html')
