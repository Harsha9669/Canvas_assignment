
from flask import Flask, request

app = Flask(__name__)

@app.route('/lti', methods=['POST'])
def launch():
    course_title = request.form.get('context_title')
    user_id = request.form.get('user_id')
    
    if course_title and user_id:
        return f"Course Title: {course_title}, User ID: {user_id}"
    else:
        return "Required fields (context_title or user_id) are missing", 400

if __name__ == '__main__':
    app.run(debug=True)





