from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suggest-medicine', methods=['POST'])
def suggest_medicine():
    data = request.json
    message = data.get('message', '')
    available_medicines = data.get('available_medicines', [])

    suggestion = None
    for med in available_medicines:
        if med.lower() in message.lower():
            suggestion = med
            break

    if not suggestion and available_medicines:
        import random
        suggestion = random.choice(available_medicines)

    return jsonify({
        'suggestion': suggestion,
        'from_available': True,
        'all_options': available_medicines
    })

if __name__ == '__main__':
    app.run(port=8000)