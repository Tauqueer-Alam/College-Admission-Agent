
from flask import Flask, request, jsonify
from retriever import retrieve_context
from generator import generate_answer

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    
    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Step 1: Retrieve relevant context
    context_docs = retrieve_context(question)

    # Step 2: Generate answer using context
    answer = generate_answer(question, context_docs)

    return jsonify({
        "question": question,
        "answer": answer,
        "context": context_docs
    })

if __name__ == "__main__":
    app.run(debug=True)
