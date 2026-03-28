from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="api_key")

# Generate Questions
@app.route('/generate', methods=['POST'])
def generate_questions():
    topic = request.json['topic']

    prompt = f"""
    Generate 5 MCQ questions on {topic}.
    Include options and correct answer.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"questions": response.choices[0].message.content})


# Evaluate Answers
@app.route('/evaluate', methods=['POST'])
def evaluate_answers():
    data = request.json

    prompt = f"""
    Questions:
    {data['questions']}

    User Answers:
    {data['answers']}

    Give:
    - Score out of 100
    - Strengths
    - Weaknesses
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"result": response.choices[0].message.content})


if __name__ == "__main__":
    app.run(debug=True)