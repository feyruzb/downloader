from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/link')
def link():
    return render_template('link-shortener.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format = request.form['format']
    resolution = request.form['resolution']
    print(url, format, resolution)
    # yt = YouTube(url)


    video = YouTube(url)

    if format == 'MP3':
        audio = video.streams.get_audio_only()
        audio.download('downloads/')
        filename = audio.default_filename
        file_path = os.path.join('downloads', filename)
        return send_file(file_path, as_attachment=True)
    else:
        stream = video.streams.get_by_resolution(resolution)
        print(video.streams)
        stream.download('downloads/')
        filename = stream.default_filename
        file_path = os.path.join('downloads', filename)
        return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
