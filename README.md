# Guess The Number Game

Welcome to the **Guess The Number** game! This fun and interactive Python application challenges you to guess a randomly generated number between 1 and 10. Test your luck and see if you can guess the number within three attempts!

## Table of Contents

- [Game Overview](#game-overview)
- [Getting Started](#getting-started)
- [How to Play](#how-to-play)
- [Dockerization](#dockerization)
- [GitHub Actions Workflows](#github-actions-workflows)

## Game Overview

In this simple game, the computer generates a random number between 1 and 10. You have three attempts to guess the correct number. After each guess, you will receive feedback on whether your guess was too high, too low, or correct. Can you guess the number before you run out of attempts?

## Getting Started

To run the Guess The Number game on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/attilaxban/guess-the-number.git
   cd guess-the-number
   ```

2. Make sure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

3. Run the game:
   ```bash
   python3 script.py
   ```

## How to Play

1. Launch the game by running `python3 script.py`.
2. When prompted, enter your guess (a number between 1 and 10).
3. You will receive feedback on your guess.
4. You have three attempts to guess the correct number. Good luck!

## Dockerization

This application is also dockerized for easy deployment. To run the application in a Docker container, follow these steps:

1. Run the Docker container:
   ```bash
   docker run -it attilaxban/python-app
   ```

## GitHub Actions Workflows

This project is integrated with GitHub Actions to automate testing and deployment. The workflow is triggered on every push request to the repository. It will:

1. Run the tests to ensure everything is working correctly.
2. If the tests pass, it will automatically push the updated image to Docker Hub.

### Workflow Configuration

Make sure to check the `.github/workflows/` directory for the configuration files that set up the CI/CD pipelines.