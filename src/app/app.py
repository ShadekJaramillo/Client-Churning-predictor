from flask import Flask, request, render_template
from pickle import load
from pathlib import Path
from pandas import DataFrame
import os

app = Flask(__name__)
model_path = Path(__file__).parent.parent.parent/'models'/'AdaBoost_learning_rate_1.5_n_estimators_300_random_state_42.sav'
with open(str(model_path),'rb') as f:
    model = load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = DataFrame([request.form])
        prediction = model.predict(data)
        if prediction==1:
            message = 'The client is likely to churn'
        else:
            message = 'The client is likely not churning'
    else:
        message=None
    return render_template("index.html", prediction=message)

if __name__ == '__main__':
    if os.name == 'nt':
        from waitress import serve
        port = 5000
        host = '127.0.0.1'
        print(f'application running in {host}:{port}')
        serve(app, host=host, port=port)
    else:
        pass