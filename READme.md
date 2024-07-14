# Electrical & Electronics Engineering Chatbot

This repository contains the implementation of an AI-powered chatbot designed to answer questions related to Electrical and Electronics Engineering. The chatbot is built using Streamlit for the web interface and Google's Generative AI (Gemini) for generating responses.

![Chatbot Interface](Images\page1.png)

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Dependencies](#dependencies)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Introduction

The Electrical & Electronics Engineering Chatbot is designed to assist students, professionals, and enthusiasts by answering their questions related to the field of Electrical and Electronics Engineering. The chatbot provides responses at different expertise levels, including Beginner, Intermediate, and Professional.

## Features

- **User Authentication:** Users can log in using their company name and email.
- **Multi-level Explanations:** Responses are tailored based on the selected expertise level (Beginner, Intermediate, Professional).
- **Chat History:** Users can view and manage their chat history.
- **Feedback Submission:** Users can provide feedback on the responses received.
- **Customizable Avatars:** Users and bot avatars can be customized for a personalized experience.
- **Instant Response Display:** User queries and AI responses are displayed instantly.

## Installation

To run the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/electrical-engineering-chatbot.git
    cd electrical-engineering-chatbot
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

5. **Ensure you have an image named `pic1.jpg` in the `Images` directory for branding.**

## Usage

To run the Streamlit application:

1. **Run the application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your browser and navigate to http://localhost:8501.**

3. **Enter your company name and email to continue.**

4. **Select your expertise level from the sidebar.**

5. **Interact with the AI assistant by typing questions in the input box.**

6. **View chat history and submit feedback via the sidebar.**

## Dependencies

The project requires the following libraries:

- `streamlit`
- `Pillow`
- `python-dotenv`
- `google-generativeai`
- `base64`
- `io`
- `datetime`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

# 

LicenseContributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.


# Contact

For any questions or suggestions, please contact olamidehassan007@gmail.com.


### Additional Notes

1. **Images Directory:** Ensure that you have an `images` directory with the relevant images (`chatbot_interface.png` and `pic1.jpg`) for the avatars and branding.

2. **Environment Variables:** The `.env` file should be set up properly with the correct API key.

3. **Dependencies:** Ensure all dependencies are listed in the `requirements.txt` file. If there are any missing, add them.

4. **Testing:** Test the instructions to ensure that they are accurate and everything works as expected.

5. **Customization:** Customize the README and other files as necessary to fit your project specifics.

Feel free to adjust the content to better suit your project's needs and context.
