# When did the Rocket Launch Telegram Bot

## Overview

This project is a Telegram bot developed using **python-telegram-bot** that assists users in pinpointing the exact frame of a rocket launch from a video. The bot employs a bisection algorithm to interactively narrow down the launch frame based on user feedback about the rocket's launch status.

### Key Features
- **Interactive Frame Querying**: Displays video frames to the user, asking if the rocket has launched yet.
- **Bisection Algorithm**: Efficiently narrows down the exact launch frame within 16 steps.

### Limitations
- **Frame Count**: The bot is designed for videos with a maximum of 61,696 frames.
- **User Feedback Dependence**: The accuracy of the frame identification depends on user responses.
- **Single Video Source**: Currently set to work with a single video; multi-video support is not implemented.

### Future Enhancements
- **Multi-Video Support**: Enable functionality to handle multiple videos for frame analysis.
- **Dockerized and CI/CD**: Create Docker image and add CI/CD
---

## Requirements

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- A Telegram account (to create a bot)
- (Optional) Docker for containerized deployment

### Python Dependencies

Install the necessary Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```
---

## Running Unit Tests

Tests use **unittest** and mock AWS interactions. Ensure that tests are run in an isolated environment without
interacting with real AWS resources.

1. **Install Testing Dependencies**:

Make sure you have installed `unittest` for testing:

2. **Run Tests**:

Run tests using the following command:

```bash
python -m unittest discover
```
Tests are located in the `tests/` folder. These will mock S3 services to avoid actual AWS calls during testing.
---
