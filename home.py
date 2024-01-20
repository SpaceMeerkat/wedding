# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:52:45 2024

@author: James
"""

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for, make_response, jsonify)
from os import listdir

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/", methods=None)
def home_landing():
    # cards_path = "/home/jdawson/repos/sharkweb/static/cards/"
    # #shark_cards = ["cards/"+f for f in listdir(cards_path)]
    # shark_cards = listdir(cards_path)
    # print(shark_cards)
    # #shark_card_names = [shark_cards[k].split("/")[1].split(".")[0] for k in range(len((shark_cards)))]
    # shark_card_names = [shark_cards[k].split(".")[0] for k in range(len((shark_cards)))]
    # #shark_card_urls = [url_for("static", filename=i) for i in shark_cards]
    # shark_card_urls = shark_cards
    # shark_card_status = ["unobserved"] * len(shark_card_names)
    
    # shark_cards_dict = {"names":shark_card_names,
    #                     "urls":shark_card_urls,
    #                     "status":shark_card_status,
    #                     "species":[],
    #                     "location":[],
    #                     "operator":[],
    #                     "depth":[],
    #                     "about":[]}
    
    return render_template('home.html')


