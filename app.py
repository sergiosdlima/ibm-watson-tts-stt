# -*- coding: utf-8 -*-

import os
from os.path import join, dirname
import logging
from flask import Flask, render_template, request, jsonify, send_file
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

API_KEY = os.environ['API_KEY']
TTS_SERVICE_URL = os.environ['TTS_SERVICE_URL']

file_path = join(dirname(__file__), 'audio.mp3')

class IBMWatson(object):
    def __init__(self):
        authenticator = IAMAuthenticator(API_KEY)
        self.tts = TextToSpeechV1(
            authenticator=authenticator
        )
        self.tts.set_service_url(TTS_SERVICE_URL)
    
    def synthesize(self, text):
        if (os.path.exists(file_path)):
            os.remove(file_path)

        with open('audio.mp3', 'wb') as audio_file:
            content = self.tts.synthesize(
                text,
                voice='pt-BR_IsabelaVoice',
                accept='audio/mp3'
            ).get_result().content
            audio_file.write(content)

watson = IBMWatson()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    if text:
        watson.synthesize(text)
        return jsonify({'output': text, 'audio_url': '/audio'})
    else:
        return jsonify({'error': 'Missing data!'})

@app.route('/audio', methods=['GET'])
def get_audio():
    return send_file(file_path)