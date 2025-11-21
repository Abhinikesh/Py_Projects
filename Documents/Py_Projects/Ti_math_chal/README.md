# Math Challenge Web Application

A Flask-based web application that converts your Python math challenge program into a REST API.

## Features

- **GET /problems**: Generates 10 random math problems and returns them as JSON
- **POST /check**: Validates user answers against expressions
- **GET /health**: Health check endpoint

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 3. Access the Web Application

Open your web browser and go to:
- **Main Web App**: `http://localhost:5000` (or `http://127.0.0.1:5000`)
- **API Health Check**: `http://localhost:5000/health`

## Web Application Features

The web application includes:
- **Modern, responsive UI** with beautiful gradients and animations
- **Real-time timer** to track your solving speed
- **Progress bar** showing completion status
- **Instant feedback** for correct/incorrect answers
- **Results screen** with detailed statistics
- **Share results** functionality
- **Mobile-friendly** responsive design

## API Endpoints

#### GET /problems
Generates 10 random math problems.

**Response:**
```json
{
  "problems": [
    {
      "id": 1,
      "expression": "45 + 23",
      "answer": 68
    },
    {
      "id": 2,
      "expression": "87 - 34",
      "answer": 53
    }
    // ... 8 more problems
  ],
  "total_problems": 10
}
```

#### POST /check
Validates a user's answer for a given expression.

**Request Body:**
```json
{
  "expression": "45 + 23",
  "user_answer": "68"
}
```

**Response:**
```json
{
  "expression": "45 + 23",
  "user_answer": "68",
  "correct_answer": 68,
  "is_correct": true
}
```

#### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Frontend Integration

### Example Frontend Code (JavaScript)

```javascript
// Fetch problems
async function getProblems() {
  const response = await fetch('http://localhost:5000/problems');
  const data = await response.json();
  return data.problems;
}

// Check an answer
async function checkAnswer(expression, userAnswer) {
  const response = await fetch('http://localhost:5000/check', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      expression: expression,
      user_answer: userAnswer
    })
  });
  return await response.json();
}

// Example usage
async function runMathChallenge() {
  const problems = await getProblems();
  
  for (const problem of problems) {
    const userAnswer = prompt(`Problem #${problem.id}: ${problem.expression} = `);
    const result = await checkAnswer(problem.expression, userAnswer);
    
    if (result.is_correct) {
      console.log('Correct!');
    } else {
      console.log(`Wrong! The correct answer is ${result.correct_answer}`);
    }
  }
}
```

### Example Frontend Code (Python with requests)

```python
import requests

# Fetch problems
def get_problems():
    response = requests.get('http://localhost:5000/problems')
    return response.json()['problems']

# Check an answer
def check_answer(expression, user_answer):
    response = requests.post('http://localhost:5000/check', 
                           json={'expression': expression, 'user_answer': user_answer})
    return response.json()

# Example usage
problems = get_problems()
for problem in problems:
    user_answer = input(f"Problem #{problem['id']}: {problem['expression']} = ")
    result = check_answer(problem['expression'], user_answer)
    
    if result['is_correct']:
        print('Correct!')
    else:
        print(f"Wrong! The correct answer is {result['correct_answer']}")
```

## Original Program Logic Preserved

The core logic from your original program has been preserved:
- `generate_problem()` function remains unchanged
- Same operators: `+`, `-`, `*`
- Same operand range: 2-100
- Same total problems: 10
- Same evaluation logic using `eval()`

## Development Notes

- The Flask app runs in debug mode by default
- CORS is not configured - you may need to add Flask-CORS for cross-origin requests
- Error handling is included for invalid expressions and malformed requests
- The application handles floating-point precision in answer checking
