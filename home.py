# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:52:45 2024

@author: James
"""

from flask import (Blueprint, flash, g, redirect, render_template, request,
                   session, url_for, make_response, jsonify)
import time 
import pickle
import os

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/", methods=None)
def home_landing():    
    return render_template('home.html')

def compileGuests():
    print("triggered!!")
    return

@bp.route('/submit-rsvp', methods=['POST'])
def submit_rsvp():
    name = request.form['name']
    dietary_requirements = request.form['dietaryRequirements']
    song_requests = request.form['songRequests']
    response = request.form['response']  # 'going' or 'not going'
    responseDict = {'name':name,
                    'response':response,
                    'dietary_requirements':dietary_requirements,
                    'song_requests':song_requests}
    unique_id = str(int(time.time()))
    
    if name == 'UNIQUEKEY':
        compileGuests()
        return jsonify({'status': 'success', 'message': 'compiler request received'})
        
    with open('/home/jdawson/repos/weddingapp/static/rsvp/'+unique_id+'.pkl', 'wb') as file:
        pickle.dump(responseDict, file)
    
    # Handle the data as needed, maybe save to a database, etc.
    
    return jsonify({'status': 'success', 'message': 'RSVP received'})
