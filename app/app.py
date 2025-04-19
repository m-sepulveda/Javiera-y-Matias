from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'titulo': '♥ Matias y Javiera ♥'
    }
    target_date = datetime(2025, 7, 5, 15, 00, 0)
    timestamp_ms = int(target_date.timestamp() * 1000)
    return render_template('index.html',data=data,target_date=timestamp_ms)

if __name__ == '__main__':
    app.run(debug =True, port=5000)