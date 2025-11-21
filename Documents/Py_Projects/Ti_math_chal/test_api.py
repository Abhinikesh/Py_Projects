#!/usr/bin/env python3
"""
Test script for the Math Challenge Flask API
Run this after starting the Flask server with: python app.py
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f'{BASE_URL}/health')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_problems():
    """Test the problems endpoint"""
    print("Testing problems endpoint...")
    response = requests.get(f'{BASE_URL}/problems')
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Total problems: {data['total_problems']}")
    print("First 3 problems:")
    for problem in data['problems'][:3]:
        print(f"  Problem #{problem['id']}: {problem['expression']} = {problem['answer']}")
    print()
    return data['problems'][0]  # Return first problem for testing

def test_check(problem):
    """Test the check endpoint with a sample problem"""
    print("Testing check endpoint...")
    
    # Test correct answer
    correct_data = {
        'expression': problem['expression'],
        'user_answer': str(problem['answer'])
    }
    response = requests.post(f'{BASE_URL}/check', json=correct_data)
    print(f"Correct answer test - Status: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test wrong answer
    wrong_data = {
        'expression': problem['expression'],
        'user_answer': str(problem['answer'] + 1)
    }
    response = requests.post(f'{BASE_URL}/check', json=wrong_data)
    print(f"Wrong answer test - Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == '__main__':
    try:
        test_health()
        problem = test_problems()
        test_check(problem)
        print("All tests completed successfully!")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Flask server.")
        print("Make sure to start the server first with: python app.py")
    except Exception as e:
        print(f"Error: {e}")
