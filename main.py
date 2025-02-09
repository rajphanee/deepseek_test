   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route('/predict', methods=['POST'])
   def predict():
       data = request.json
       question = data.get('question', '').lower()

       if "who is the president of america" in question:
           answer = "The current president of America is Joe Biden."
       else:
           answer = "I'm sorry, I can't answer that question."

       return jsonify({"answer": answer})

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=8080)
   
