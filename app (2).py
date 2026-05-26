from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

easy = []
normal = []
hard = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/highscores')
def highscores_page():
    return render_template('minesweeper.html')

@app.route('/get_scores')
def get_scores():
    all_scores = easy + normal + hard

    all_scores.sort(key=lambda x: x['score'])

    for i, s in enumerate(all_scores):
        s["rang"] = i + 1

    return jsonify({
        "all": all_scores,
        "easy": easy,
        "normal": normal,
        "hard": hard
    })

@app.route('/update_score', methods=['POST'])
def update_score():
    try:
        data = request.get_json()

        if not data or 'naam' not in data or 'score' not in data or 'level' not in data:
            return jsonify({"error": "Geen goede data ontvangen"}), 400

        score = int(data['score'])

        # filter
        if score < 20:
            return jsonify({"status": "ignored"}), 200

        entry = {
            "rang": 0,
            "naam": str(data['naam']),
            "score": score,
            "level": int(data['level'])
        }

        level = entry["level"]

        if level == 1:
            easy.append(entry)
            easy.sort(key=lambda x: x['score'])
            lijst = easy

        elif level == 2:
            normal.append(entry)
            normal.sort(key=lambda x: x['score'])
            lijst = normal

        elif level == 3:
            hard.append(entry)
            hard.sort(key=lambda x: x['score'])
            lijst = hard

        else:
            return jsonify({"error": "invalid level"}), 400

        for i, e in enumerate(lijst):
            e["rang"] = i + 1

        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)