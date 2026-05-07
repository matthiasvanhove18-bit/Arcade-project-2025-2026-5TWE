from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Een tijdelijke lijst om scores in op te slaan (verwijnt als de server herstart)
# Voor een echt project gebruik je later een database, maar dit is prima voor nu.
highscores = [
    {"rang": 1, "naam": "Matthias", "score": 950},
    {"rang": 2, "naam": "Kasper", "score": 880}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/highscores')
def highscores_page():
    # We sturen de lijst met scores mee naar de HTML
    return render_template('minesweeper.html', scores=highscores)

# DIT IS DE NIEUWE CODE VOOR NODE-RED
@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.json
    if data:
        # We voegen de nieuwe score toe aan de lijst
        nieuwe_score = {
            "rang": len(highscores) + 1,
            "naam": data.get("naam", "Onbekend"),
            "score": data.get("score", 0)
        }
        highscores.append(nieuwe_score)
        # Sorteer op score (hoogste eerst)
        highscores.sort(key=lambda x: x['score'], reverse=True)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
