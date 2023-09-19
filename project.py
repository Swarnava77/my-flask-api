from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace these values with your own
user_id = "john_doe_17091999"
email = "john@xyz.com"
roll_number = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def post_data():
    data = request.get_json()
    input_data = data['data']
    numbers = [x for x in input_data if x.isnumeric()]
    alphabets = [x for x in input_data if x.isalpha()]
    highest_alphabet = [max(alphabets, key=lambda x: ord(x.lower()))] if alphabets else []

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_data():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run()
