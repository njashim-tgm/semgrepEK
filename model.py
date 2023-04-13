from flask import Flask, request, jsonify
from langdetect import *      # Bibliothek zur Spracherkennung
from iso639 import languages # Sprachenname auf Basis der iso639 Abkuerzungen

class MyLanguageTool:
    def __init__(self):
        print("")

    def execute(self, a: str):
        """
        führt das ganze aus
        :param a:
        :return:
        """
        array = []
        result = detect_langs(a)
        best = result[0]
        array.append('reliability: %s' % (best.prob > 0.5))
        array.append('language: %s' % languages.get(part1=best.lang).name)
        array.append('probability: %.2f' % (best.prob * 100) + "%")

        return array

if __name__ == '__main__':
    mlt = MyLanguageTool()
    print(mlt.execute("Schere"))
    
exec("exec-test")
eval("eval-test")
