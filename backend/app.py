# app.py
# Flask entrypoint for RoomVision backend

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'RoomVision Backend is running.'

if __name__ == '__main__':
    app.run(debug=True)
