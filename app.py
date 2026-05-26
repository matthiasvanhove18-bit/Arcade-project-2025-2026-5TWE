from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

highscores = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/highscores')
def highscores_page(): 
    return render_template('minesweeper.html', scores=highscores)

@app.route('/update_score', methods=['POST'])
def update_score():
    try:
        data = request.get_json()
        if not data or 'naam' not in data or 'score' not in data:
            return jsonify({"error": "Geen goede data ontvangen"}), 400
       
        nieuwe_entry = {
            "rang": 0, 
            "naam": str(data['naam']),
            "score": int(data['score'])
        }
        highscores.append(nieuwe_entry)
              
        highscores.sort(key=lambda x: x['score'], reverse=False)
                
        for i, entry in enumerate(highscores):
            entry['rang'] = i + 1
            
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
