from flask import Flask, request, jsonify
from Charity import Charity
import re
from person import Person

app = Flask(__name__, static_folder="static")

users = []

def is_valid_email(email):
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    hometown = data.get("hometown")

    if not name or not email or not hometown:
        return jsonify({"success": False, "message": "All fields are required."})

    if not is_valid_email(email):
        return jsonify({"success": False, "message": "Invalid email format."})

    if any(user.email == email for user in users):
        return jsonify({"success": False, "message": "Email already in use."})

    new_user = Person(name, email, "", hometown)
    users.append(new_user)
    return jsonify({"success": True, "message": "Account created successfully!"})

@app.route('/interest', methods=['POST'])
def interest():
    if not users:
        return jsonify({"success": False, "message": "No users available for matching."})

    first_user = users[0]
    if not isinstance(first_user, Person):
        return jsonify({"success": False, "message": "Invalid user data."})

    matches = first_user.return_matches()
    return jsonify({"success": True, "matches": [charity.to_json() for charity in matches]})

if __name__ == '__main__':
    person = Person("h", "h@gmail.com", "Supportive Health Care", "Calgary")
    users.append(person)
    app.run(debug=True, port=5000)
