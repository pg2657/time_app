from datetime import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/time')
def time():
    time_display= datetime.now()
    return 'The current time is: {}'.format(time_display)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
