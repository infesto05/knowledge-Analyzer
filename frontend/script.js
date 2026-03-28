async function getQuestions() {
    const topic = document.getElementById("topic").value;

    console.log("Sending request...");

    const res = await fetch("http://127.0.0.1:5000/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    });

    const data = await res.json();

    console.log("Response received:", data);
    
    <button onclick="getQuestions()">Generate Questions</button>

    document.getElementById("questions").innerText = data.questions;
}

async function submitAnswers() {
    const questions = document.getElementById("questions").innerText;
    const answers = document.getElementById("answers").value;

    const res = await fetch("http://127.0.0.1:5000/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ questions, answers })
    });

    const data = await res.json();
    document.getElementById("result").innerText = data.result;
}