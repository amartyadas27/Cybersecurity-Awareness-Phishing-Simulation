from flask import Flask, render_template, request
from utils.checker import check_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        result = check_url(url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

