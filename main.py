from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('girl-power/index.html')
#    return render_template('index.html')

@app.route('/girl-power')
def girl_power_index():
    return render_template('Girl-Power/index.html')

@app.route('/girl-power/media')
def girl_power_media():
    return render_template('Girl-Power/gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
