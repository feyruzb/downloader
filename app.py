from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format = request.form['format']
    resolution = request.form['resolution']

    video = YouTube(url)
    if format == 'mp3':
        audio = video.streams.get_audio_only()
        audio.download('downloads/')
        filename = audio.default_filename
        file_path = os.path.join('downloads', filename)
        return send_file(file_path, as_attachment=True)
    else:
        if resolution == '720p':
            stream = video.streams.get_by_resolution('720p')
        else:
            stream = video.streams.get_highest_resolution()
        stream.download('downloads/')
        filename = stream.default_filename
        file_path = os.path.join('downloads', filename)
        return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
