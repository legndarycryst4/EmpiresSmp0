from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/girl-power')
def girl_power_index():
    return render_template('Girl-Power/index.html')
@app.route('/girl-power/media')
def girl_power_media():
    return render_template('Girl-Power/gallery.html')
@app.route('/girl-power/<path:filename>')
def serve_girl_power_files(filename):
    return send_from_directory('Girl-Power', filename)
