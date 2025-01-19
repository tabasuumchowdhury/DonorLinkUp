from flask import Flask, request, jsonify
from Charity import Charity 
import re
from person import Person

app = Flask(__name__,static_folder="static")

users = []

def is_valid_email(email):
    """Validate email format."""
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    hometown = data.get("hometown")

    # Check for empty fields
    if not name or not email or not hometown:
        return jsonify({"success": False, "message": "All fields are required."})

    # Validate email format
    if not is_valid_email(email):
        return jsonify({"success": False, "message": "Invalid email format."})

    # Check for duplicate email
    if any(user["email"] == email for user in users):
        return jsonify({"success": False, "message": "Email already in use."})

    # Add user to database (for testing, just append to the list)
    users.append({"name": name, "email": email, "hometown": hometown})
    return jsonify({"success": True, "message": "Account created successfully!"})

# person.return_matches(users[-1])
@app.route('/interest', methods=['POST'])
def interest():
    arr = users[0].return_matches()
    return str(arr)

if __name__ == '__main__':
    person = Person("h", "h@gmail.com","Supportive Health Care", "Calgary")
    users.append(person)
    app.run(debug=True, port=5000)
