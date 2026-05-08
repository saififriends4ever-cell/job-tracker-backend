from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return {
        "message":"Backend Working Successfully"
    }

@app.route('/jobs')
def jobs():
    return {
        "jobs":[
            {
                "title":"Frontend Developer"
            },
            {
                "title":"Python Developer"
            }
        ]
    }

if __name__ == "__main__":
    app.run()
