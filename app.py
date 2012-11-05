import os
from flask import render_template
from flask import Flask
from headliner import headline

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    message = headline()
    return render_template('layout.html', suggestion=message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
