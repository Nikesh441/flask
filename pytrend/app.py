from flask import Flask, render_template, request
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trends', methods=['POST'])
def trends():
    keyword = request.form.get('keyword')
    pytrends = TrendReq(hl='en-IN', tz=330)
    tf = request.form.get('timeframe')
    pytrends.build_payload([keyword], timeframe=str(tf))
    interest_over_time_df = pytrends.interest_over_time()

    return render_template('index.html', data=interest_over_time_df.to_html())

if __name__ == '__main__':
    app.run(debug=True)
