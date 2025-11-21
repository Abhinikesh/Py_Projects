class MathChallenge {
    constructor() {
        this.problems = [];
        this.currentProblemIndex = 0;
        this.startTime = null;
        this.wrongAnswers = 0;
        this.correctAnswers = 0;
        
        this.initializeElements();
        this.bindEvents();
    }

    initializeElements() {
        // Screens
        this.startScreen = document.getElementById('startScreen');
        this.gameScreen = document.getElementById('gameScreen');
        this.resultsScreen = document.getElementById('resultsScreen');
        this.loadingOverlay = document.getElementById('loadingOverlay');

        // Game elements
        this.progressFill = document.getElementById('progressFill');
        this.problemCounter = document.getElementById('problemCounter');
        this.timer = document.getElementById('timer');
        this.problemNumber = document.getElementById('problemNumber');
        this.problemExpression = document.getElementById('problemExpression');
        this.answerInput = document.getElementById('answerInput');
        this.feedback = document.getElementById('feedback');
        this.feedbackIcon = document.getElementById('feedbackIcon');
        this.feedbackText = document.getElementById('feedbackText');

        // Results elements
        this.finalTime = document.getElementById('finalTime');
        this.correctAnswersEl = document.getElementById('correctAnswers');
        this.wrongAnswersEl = document.getElementById('wrongAnswers');
        this.accuracy = document.getElementById('accuracy');

        // Buttons
        this.startBtn = document.getElementById('startBtn');
        this.submitBtn = document.getElementById('submitBtn');
        this.playAgainBtn = document.getElementById('playAgainBtn');
        this.shareBtn = document.getElementById('shareBtn');
    }

    bindEvents() {
        this.startBtn.addEventListener('click', () => this.startGame());
        this.submitBtn.addEventListener('click', () => this.submitAnswer());
        this.playAgainBtn.addEventListener('click', () => this.resetGame());
        this.shareBtn.addEventListener('click', () => this.shareResults());

        // Enter key support
        this.answerInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.submitAnswer();
            }
        });

        // Auto-focus on answer input when game starts
        this.answerInput.addEventListener('input', () => {
            this.hideFeedback();
        });
    }

    async startGame() {
        this.showLoading();
        
        try {
            const response = await fetch('/problems');
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'Failed to fetch problems');
            }
            
            this.problems = data.problems;
            this.currentProblemIndex = 0;
            this.wrongAnswers = 0;
            this.correctAnswers = 0;
            this.startTime = Date.now();
            
            this.hideLoading();
            this.showGameScreen();
            this.displayCurrentProblem();
            this.startTimer();
            
        } catch (error) {
            console.error('Error starting game:', error);
            this.hideLoading();
            alert('Failed to load problems. Please try again.');
        }
    }

    showGameScreen() {
        this.startScreen.classList.add('hidden');
        this.resultsScreen.classList.add('hidden');
        this.gameScreen.classList.remove('hidden');
        this.answerInput.focus();
    }

    displayCurrentProblem() {
        const problem = this.problems[this.currentProblemIndex];
        
        this.problemNumber.textContent = problem.id;
        this.problemExpression.textContent = problem.expression;
        this.problemCounter.textContent = `Problem ${problem.id} of ${this.problems.length}`;
        
        // Update progress bar
        const progress = (this.currentProblemIndex / this.problems.length) * 100;
        this.progressFill.style.width = `${progress}%`;
        
        // Clear input and focus
        this.answerInput.value = '';
        this.answerInput.focus();
        this.hideFeedback();
    }

    async submitAnswer() {
        const userAnswer = this.answerInput.value.trim();
        
        if (!userAnswer) {
            return;
        }

        const problem = this.problems[this.currentProblemIndex];
        
        try {
            const response = await fetch('/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    expression: problem.expression,
                    user_answer: userAnswer
                })
            });

            const result = await response.json();
            
            if (!response.ok) {
                throw new Error(result.error || 'Failed to check answer');
            }

            this.showFeedback(result.is_correct, result.correct_answer);
            
            if (result.is_correct) {
                this.correctAnswers++;
            } else {
                this.wrongAnswers++;
            }

            // Move to next problem after a short delay
            setTimeout(() => {
                this.nextProblem();
            }, 1500);

        } catch (error) {
            console.error('Error checking answer:', error);
            alert('Failed to check answer. Please try again.');
        }
    }

    showFeedback(isCorrect, correctAnswer) {
        this.feedback.classList.remove('hidden');
        
        if (isCorrect) {
            this.feedback.classList.remove('incorrect');
            this.feedback.classList.add('correct');
            this.feedbackIcon.textContent = '✓';
            this.feedbackText.textContent = 'Correct!';
        } else {
            this.feedback.classList.remove('correct');
            this.feedback.classList.add('incorrect');
            this.feedbackIcon.textContent = '✗';
            this.feedbackText.textContent = `Wrong! The answer is ${correctAnswer}`;
        }
    }

    hideFeedback() {
        this.feedback.classList.add('hidden');
    }

    nextProblem() {
        this.currentProblemIndex++;
        
        if (this.currentProblemIndex >= this.problems.length) {
            this.endGame();
        } else {
            this.displayCurrentProblem();
        }
    }

    endGame() {
        this.stopTimer();
        this.showResults();
    }

    showResults() {
        this.gameScreen.classList.add('hidden');
        this.resultsScreen.classList.remove('hidden');
        
        const totalTime = Date.now() - this.startTime;
        const minutes = Math.floor(totalTime / 60000);
        const seconds = Math.floor((totalTime % 60000) / 1000);
        const timeString = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        
        const accuracy = Math.round((this.correctAnswers / this.problems.length) * 100);
        
        this.finalTime.textContent = timeString;
        this.correctAnswersEl.textContent = this.correctAnswers;
        this.wrongAnswersEl.textContent = this.wrongAnswers;
        this.accuracy.textContent = `${accuracy}%`;
    }

    resetGame() {
        this.startScreen.classList.remove('hidden');
        this.gameScreen.classList.add('hidden');
        this.resultsScreen.classList.add('hidden');
        this.hideFeedback();
    }

    startTimer() {
        this.timerInterval = setInterval(() => {
            const elapsed = Date.now() - this.startTime;
            const minutes = Math.floor(elapsed / 60000);
            const seconds = Math.floor((elapsed % 60000) / 1000);
            this.timer.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }, 1000);
    }

    stopTimer() {
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
    }

    showLoading() {
        this.loadingOverlay.classList.remove('hidden');
    }

    hideLoading() {
        this.loadingOverlay.classList.add('hidden');
    }

    shareResults() {
        const totalTime = Date.now() - this.startTime;
        const minutes = Math.floor(totalTime / 60000);
        const seconds = Math.floor((totalTime % 60000) / 1000);
        const timeString = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        const accuracy = Math.round((this.correctAnswers / this.problems.length) * 100);
        
        const shareText = `🧮 Math Challenge Results:
⏱️ Time: ${timeString}
✅ Correct: ${this.correctAnswers}/10
❌ Wrong: ${this.wrongAnswers}
📊 Accuracy: ${accuracy}%

Try the challenge yourself!`;

        if (navigator.share) {
            navigator.share({
                title: 'Math Challenge Results',
                text: shareText,
                url: window.location.href
            });
        } else {
            // Fallback: copy to clipboard
            navigator.clipboard.writeText(shareText).then(() => {
                alert('Results copied to clipboard!');
            }).catch(() => {
                // Fallback: show in prompt
                prompt('Copy these results:', shareText);
            });
        }
    }
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new MathChallenge();
});
