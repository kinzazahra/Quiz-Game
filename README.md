Brainy Quiz – Interactive Knowledge Challenge
A dynamic and engaging web-based quiz application designed to test your knowledge across various topics. This application features a modern UI with real-time feedback, category selection, and a competitive scoring system to make learning fun and interactive.

Built with logic and fun by Kinza Zahra 🧠✨

Features
Category-Based Quizzes: Choose from a variety of topics including Science, History, Geography, and General Knowledge to tailor your challenge.

Interactive UI:

Progress Tracking: A visual progress bar that updates as you move through the questions.

Timed Questions: Challenge yourself with a countdown timer for each question to keep the game exciting.

Instant Feedback: Correct answers are highlighted in green, while incorrect choices are marked in red with the correct one revealed.

Dynamic Scoreboard:

Calculates your final score based on accuracy and speed.

Displays a summary card at the end of the session with performance insights.

Responsive Design: A clean, mobile-first interface featuring smooth transitions and glassmorphism effects for a premium look and feel.

Backend Powered: Uses a Python Flask backend to manage quiz data and ensure randomized question delivery for every session.

🛠 Tech Stack
Frontend: HTML5, CSS3 (Modern Flexbox/Grid), Vanilla JavaScript.

Backend: Python (Flask Framework).

Data Management: JSON-based question bank for easy content updates.

Styling: Custom CSS with animated backgrounds and interactive button effects.

📂 Project Structure
Plaintext
Quiz-Game/
│
├── app.py              # Main Flask server and quiz logic
│
├── static/             # Frontend assets
│   ├── styles.css      # Custom UI styling and animations
│   └── script.js       # Game logic, timers, and scoring
│
└── templates/          # HTML Views
    └── index.html      # The main quiz interface
⚙️ Installation & Setup
Clone the Repository:

Bash
git clone <your-repo-url>
cd Quiz-Game
Install Dependencies:
Ensure you have Python installed, then install Flask:

Bash
pip install Flask
Run the Application:

Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000 to start playing!

🚀 How to Play
Pick a Topic: Select your preferred category from the home screen.

Answer Questions: Read the question and click on the best option before the timer runs out.

Check Results: After the final question, review your total score and see if you reached the "High Score" status.

Play Again: Click the restart button to try a different category or beat your previous record!

🔮 Future Improvements
Leaderboard integration to compete with friends.

Support for image-based and audio-based questions.

Ability for users to create and share their own custom quiz sets.

Made with ❤️ by Kinza Zahra
