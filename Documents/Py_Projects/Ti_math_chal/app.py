from flask import Flask, request, jsonify, send_from_directory
import random
import time
import os

app = Flask(__name__, static_folder='static')

# Constants from your original program
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 100
TOTAL_PROBLEMS = 10


def generate_problem():
    """
    Generate a random math problem and return the expression and answer.
    This function is kept exactly as in your original program.
    """
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


@app.route('/problems', methods=['GET'])
def get_problems():
    """
    Generate 10 random math problems and return them as JSON.
    Each problem includes the expression and the correct answer.
    """
    problems = []
    
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        problems.append({
            'id': i + 1,
            'expression': expr,
            'answer': answer
        })
    
    return jsonify({
        'problems': problems,
        'total_problems': TOTAL_PROBLEMS
    })


@app.route('/check', methods=['POST'])
def check_answer():
    """
    Check if a user's answer is correct for a given expression.
    Expects JSON with 'expression' and 'user_answer' fields.
    """
    try:
        data = request.get_json()
        
        if not data or 'expression' not in data or 'user_answer' not in data:
            return jsonify({
                'error': 'Missing required fields: expression and user_answer'
            }), 400
        
        expression = data['expression']
        user_answer = data['user_answer']
        
        # Calculate the correct answer
        try:
            correct_answer = eval(expression)
        except:
            return jsonify({
                'error': 'Invalid expression'
            }), 400
        
        # Check if the answer is correct
        try:
            user_answer_num = float(user_answer)
            is_correct = abs(user_answer_num - correct_answer) < 0.001  # Handle floating point precision
        except ValueError:
            return jsonify({
                'error': 'Invalid user answer format'
            }), 400
        
        return jsonify({
            'expression': expression,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'is_correct': is_correct
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500


@app.route('/')
def index():
    """
    Serve the main web application page.
    """
    return send_from_directory('static', 'index.html')


@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint.
    """
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
