from flask import Flask, render_template, request, redirect, url_for
import os
from modules.queue import Queue
from modules.deque import Deque

app = Flask(__name__)

queue_structure = Queue()
deque_structure = Deque()

@app.route('/')
def home_redirect():
    return redirect(url_for('index'))

#home page
@app.route('/home')
def index():
    index_data = {
        "message": "GROUP 11",
        "message_1": "Hello everyone we are the Group 11 and this is our Group Portfolio project in DSA"
    }
    return render_template('home.html', index=index_data, active_page='home')

#project page
@app.route('/works')
def works():
    return render_template('works.html',  active_page='works')

#profile and contact page
@app.route('/contacts')
def members_contact():
    people = [
    {
        "name": "Mark Christian Abucejo",
        "image": "static/images/pic 1.png",
        "links": {
                "facebook": "https://www.facebook.com/mrkchrstnsbcj",
                "email": "https://www.facebook.com/mrkchrstnsbcj",
                "github": "https://www.facebook.com/mrkchrstnsbcj",
            }
    },
    {
        "name": "Zy Banez",
        "image": "static/images/zy.jpg",
        "links": {
                "facebook": "https://www.facebook.com/zyescote.banez.5",
                "email": "zyescotebanez@gmail.com",
                "github": "https://github.com/ITZMEXYZ",
            }
    }, 
    {
        
            "name": "Kyle Isaac Celin",
            "image": "static/images/pic 2.png",
            "links": {
                "facebook": "https://www.facebook.com/cee.the.lin.e",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "John Luke Fabillan",
            "image": "static/images/pic 3.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "Princess Sophia Manalo",
            "image": "static/images/pic 4.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "Isaac Christian Pelingen",
            "image": "static/images/pic 5.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }, 
    {
        
            "name": "Gian Carlos Tumanan",
            "image": "static/images/pic 6.png",
            "links": {
                "facebook": "https://facebook.com/zybanezz",
                "email": "https://youtube.com/@zybanezz",
                "github": "https://tiktok.com/@zybanezz",
        }
    }
    ]
    
    return render_template("contacts.html", people=people)


# Queue Visualizer
@app.route('/Queue', methods=['GET', 'POST'])
def queue_visualizer():
    if request.method == "POST":
        value = request.form.get("value")

        if "enqueue" in request.form:
            queue_structure.enqueue(value)

        elif "dequeue" in request.form:
            queue_structure.dequeue()

    if request.args.get("dequeue"):
        queue_structure.dequeue()

    return render_template(
        "queuevisualizer.html",
        items=queue_structure.get_items(),
        active_page="works"
    )

# De-que Visualizer
@app.route('/Deque', methods=['GET', 'POST'])
def dequeue_visualizer():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "left":  # Insert Left
            value = request.form.get("value")
            if value:
                deque_structure.insert_left(value)

        elif action == "right": 
            value = request.form.get("value")
            if value:
                deque_structure.insert_right(value)

        elif action == "remove_left":
            deque_structure.remove_left()

        elif action == "remove_right":
            deque_structure.remove_right()

    return render_template("dequeuevisualizer.html",
                           items=deque_structure.get_items(),
                           active_page="works")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
