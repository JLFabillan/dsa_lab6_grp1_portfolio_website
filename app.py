from flask import Flask, render_template
from modules.queue import Queue
from modules.dequeue import DeQueue

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')

# PROFILES PAGE
@app.route('/profiles')
def profiles():
    return render_template('profiles.html')

# CONTACTS PAGE
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# WORKS PAGE
@app.route('/works')
def works():
    return render_template('works.html')

# "Queue Visualizer" PAGE
@app.route('/works/queue-visualizer', methods=['GET', 'POST'])
def queue_visualizer():
    return render_template('queuevisualizer.html')

# "DeQueue Visualizer" PAGE
@app.route('/works/dequeue-visualizer', methods=['GET', 'POST'])
def dequeue_visualizer():
    return render_template('dequeuevisualizer.html')

if __name__ == "__main__":
    app.run(debug=True)