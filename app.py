@app.route('/update_score', methods=['POST'])
def update_score():
    try:
        data = request.get_json()
        if not data or 'naam' not in data or 'score' not in data:
            return jsonify({"error": "Ongeldige data"}), 400

        nieuwe_score = {
            "rang": 0, # Wordt hieronder berekend
            "naam": str(data['naam']),
            "score": int(data['score'])
        }
        
        highscores.append(nieuwe_score)
        # Sorteer op hoogste score
        highscores.sort(key=lambda x: x['score'], reverse=True)
        
        # Rangnummers updaten na sorteren
        for i, score in enumerate(highscores):
            score['rang'] = i + 1
            
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
