# When did the Rocket Launch Telegram Bot

## Overview

This project is a Telegram bot developed using **python-telegram-bot** that assists users in pinpointing the exact frame of a rocket launch from a video. The bot employs a bisection algorithm to interactively narrow down the launch frame based on user feedback about the rocket's launch status.

### Bot Name
**ste_rocket_launch_bot**

### Key Features
- **Interactive Frame Querying**: Displays video frames to the user, asking if the rocket has launched yet.
- **Bisection Algorithm**: Efficiently narrows down the exact launch frame within 16 steps.

### Limitations
- **Frame Count**: The bot is designed for videos with a maximum of 61,696 frames.
- **User Feedback Dependence**: The accuracy of the frame identification depends on user responses.
- **Single Video Source**: Currently set to work with a single video; multi-video support is not implemented.

### Future Enhancements
- **Multi-Video Support**: Enable functionality to handle multiple videos for frame analysis.
- **Dockerized and CI/CD**: Create a Docker image and add CI/CD pipeline.

---

## Requirements

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- A Telegram account (to create and interact with a bot)
- (Optional) Docker for containerized deployment | Not implemented yet...

### Python Dependencies

Install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

---

## Running Unit Tests

Tests use **unittest** and mock AWS interactions. Ensure that tests are run in an isolated environment without interacting with real AWS resources.

1. **Install Testing Dependencies**:

Make sure you have installed `unittest` for testing:

```bash
pip install unittest
```

2. **Run Tests**:

Run tests using the following command:

```bash
python -m unittest discover
```

Tests are located in the `tests/` folder. These will mock S3 services to avoid actual AWS calls during testing.

---

## How to Use the Bot

1. **Run the Code**:
   - Make sure the bot is running locally by executing the main script. The bot will start and begin listening for commands.

```bash
python -m app.main 
```

2. **Open Telegram**:
   - You can use either the Telegram web client or the mobile app. 

3. **Search for the Bot**:
   - In the search bar, type `@ste_rocket_launch_bot` to find the bot.

4. **Start the Bot**:
   - Run the command `/start` to initiate the bot's functionality.

5. **Follow Instructions**:
   - Follow the prompts provided by the bot to complete the game and help identify the rocket launch frame.
![img.png](img.png)

## Code Maintainability

To ensure the code is maintainable and scalable, the following practices were implemented:

- **Modular Design**: The code is divided into clear modules and classes, each handling a specific part of the bot's functionality. This separation allows for easier testing and modification of individual components.

- **Use of Dependency Injection**: The `BisectionAlgorithm` class takes an API interface as a parameter. This allows for easier testing with mocks and promotes the single responsibility principle.

- **Consistent Naming Conventions**: Variables, functions, and classes are named descriptively, making the code easier to read and understand.

- **Unit Testing**: Creating unit tests with mocking indicates a commitment to code quality and reliability. It shows an understanding of TDD (Test-Driven Development) principles, which is crucial for maintaining large codebases.