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
import csv

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/", methods=None)
def home_landing():    
    return render_template('home.html')

def compileGuests():
    directory = '/home/SpaceMeerkat/mysite/static/rsvp/'
    all_guests_file = '/home/SpaceMeerkat/mysite/static/rsvp/admin/allGuests.csv'
    data_list = []

    # Read all pickle files and collect data
    for filename in os.listdir(directory):
        if filename.endswith('.pkl'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'rb') as file:
                data = pickle.load(file)
                data_list.append(data)
                
    print("DATA: ", data_list)

    # Write data to CSV
    with open(all_guests_file, 'w', newline='') as csvfile:
        fieldnames = ['name', 'braai_response', 'wedding_day_response', 'dietary_requirements', 'song_requests']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in data_list:
            writer.writerow(data)

    return


@bp.route('/submit-rsvp', methods=['POST'])
def submit_rsvp():
    name = request.form['name']
    braai = request.form['braai']
    dietary_requirements = request.form['dietaryRequirements']
    song_requests = request.form['songRequests']
    response = request.form['response']  # 'going' or 'not going'
    responseDict = {'name':name,
                    'braai_response': braai,
                    'wedding_day_response':response,
                    'dietary_requirements':dietary_requirements,
                    'song_requests':song_requests}
    unique_id = str(int(time.time()))
    
    if name == 'UNIQUEKEY':
        compileGuests()
        return jsonify({'status': 'success', 'message': 'compiler request received'})
        
    with open('/home/SpaceMeerkat/mysite/static/rsvp/'+unique_id+'.pkl', 'wb') as file:
        pickle.dump(responseDict, file)
    
    # Handle the data as needed, maybe save to a database, etc.
    
    return jsonify({'status': 'success', 'message': 'RSVP received'})
