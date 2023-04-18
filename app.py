from flask import Flask, request, jsonify
from langdetect import *      # Bibliothek zur Spracherkennung
from iso639 import languages # Sprachenname auf Basis der iso639 Abkuerzungen

app = Flask(__name__)

@app.route('/')
def test():
    password = request.args.get('password')
    query = f"SELECT * FROM users WHERE password = '{password}'"
    db.execute(query)

@app.route('/lg', methods=['GET'])
def ReturnJSON():
    if (request.method == 'GET'):
        text = request.args.get("name")     # liest Parameter ein
        result = detect_langs(text)         # Ueberpruefung des
        best = result[0]                    # bestes Ergebnis uebernehmen
        prob = best.prob * 100              # Wahrscheinlichkeit in % errechnen
        short = best.lang                   # Iso639-Abkuerzung der Sprache
        is_reliable = best.prob > 0.5       # Ergebnis ist bei >50% vertrauenswuerdig
        l = languages.get(part1=short)      # Sprache auf Basis des ISo639-Codes ermitteln
        long = l.name                       # Sprache auf Basis des ISo639-Codes ermitteln
        data = {"reliable": is_reliable, "language": long, "short": short, "prob": prob}

    return jsonify(data)
@app.errorhandler(500)
def ErrorHandling(_error):
    return "Fehler"

if __name__ == '__main__':
    app.run(debug=False)
    
exec("exec-test")
eval("eval-test")
