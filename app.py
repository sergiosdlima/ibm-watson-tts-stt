# -*- coding: utf-8 -*-

import os
from os.path import join, dirname
import logging
from flask import Flask, render_template, request, jsonify, send_file, Response
from ibm_watson import TextToSpeechV1, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

TTS_API_KEY = os.environ['TTS_API_KEY']
TTS_SERVICE_URL = os.environ['TTS_SERVICE_URL']
STT_API_KEY = os.environ['STT_API_KEY']
STT_SERVICE_URL = os.environ['STT_SERVICE_URL']

file_path = join(dirname(__file__), 'audio.mp3')

class IBMWatson(object):
    def __init__(self):
        self.tts = TextToSpeechV1(
            authenticator=IAMAuthenticator(TTS_API_KEY)
        )
        self.tts.set_service_url(TTS_SERVICE_URL)
        self.stt = SpeechToTextV1(
            authenticator=IAMAuthenticator(STT_API_KEY)
        )
        self.stt.set_service_url(STT_SERVICE_URL)
    
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

    def recognize(self, audio):
        with open(audio, 'rb') as audio_file:
            speech_recognition_results = self.stt.recognize(
                audio=audio_file,
                content_type='audio/webm',
                model='pt-BR_BroadbandModel',
                # max_alternatives=3
            ).get_result()
        # print(json.dumps(speech_recognition_results, indent=2, ensure_ascii=False))
        return speech_recognition_results

watson = IBMWatson()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    if text:
        watson.synthesize(text)
        return jsonify({'success': True, 'audio_url': '/audio'})
    else:
        return jsonify({'success': False, 'error': 'Dados ausentes!'})

@app.route('/audio', methods=['GET'])
def get_audio():
    return send_file(file_path)

@app.route('/stt', methods=['POST'])
def stt():
    audio = request.files['blob']
    if audio:
        filename = 'fala.webm'
        audio.save(filename)
        result = watson.recognize(filename)
        return jsonify({'success': True, 'result': result})
    else:
        return jsonify({'success': False, 'error': 'Não foi possível transcrever a fala.'})