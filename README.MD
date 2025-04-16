# Groq Customer Support Assistant

This project demonstrates a basic customer support assistant powered by the Groq Cloud language model. It uses Python and the `groq` library to interact with the model and provides a simple example of how to get started.

## Setup Instructions

1.  **Clone the repository** (if you have one):
    ```bash
    git clone your_repository_url
    cd your_project_directory
    ```
    (If you're not using Git, just navigate to your project folder in your terminal.)

2.  **Install the required Python libraries:**
    ```bash
    pip install groq python-dotenv
    ```

3.  **Create a `.env` file** in the root directory of your project.

4.  **Add your Groq Cloud API key to the `.env` file:**
    ```
    GROQ_API_KEY=your_actual_groq_cloud_api_key_here
    ```
    **Important:** Replace `your_actual_groq_cloud_api_key_here` with your actual API key from the Groq Cloud platform. **Do not commit this file to version control for security reasons.**

## How to Run the Assistant

1.  **Navigate to the project directory** in your terminal:
    ```bash
    cd your_project_directory
    ```

2.  **Run the main Python script** (e.g., if your script is named `groq_assistant.py`):
    ```bash
    python groq_assistant.py
    ```

    This will execute the script, which in the example provided, sends a query to the Groq model and prints the response to your terminal.

## Example Usage

The current example in `groq_assistant.py` sends the following prompt to the Groq model: