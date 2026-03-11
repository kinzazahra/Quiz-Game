async function loadGeminiQuiz() {
    try {
        const res = await fetch('/generate-questions', { method: 'POST' });
        const data = await res.json();

        const quizDiv = document.getElementById('quiz-container');
        quizDiv.innerHTML = '';
        if (Array.isArray(data)) {
            data.forEach((q, i) => {
                const qEl = document.createElement('div');
                qEl.innerHTML = `
                    <h3>Q${i + 1}: ${q.question}</h3>
                    <ul>
                        ${q.options.map((opt, idx) => `<li>${String.fromCharCode(65 + idx)}. ${opt}</li>`).join('')}
                    </ul>
                `;
                quizDiv.appendChild(qEl);
            });
        } else {
            document.getElementById("error-message").innerText = "⚠️ Could not load quiz.";
        }
    } catch (e) {
        document.getElementById("error-message").innerText = "⚠️ Error fetching questions.";
        console.error("❌ Fetch error:", e);
    }
}



