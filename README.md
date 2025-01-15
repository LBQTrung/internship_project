# Whisper Transcription Service

This project is a web-based transcription service using FastAPI, Faster-Whisper model, Gemini 1.5 Flash. It allows users to upload audio files and create report from this audio file.

## Project Structure

## Setup

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**
    ```sh
    pip install virtualenv
    virtualenv venv
    venv/Scripts/activate
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI server:**
    ```sh
    python app.py
    ```

2. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000`.

## Endpoints

- **GET `/`**: Serves the HTML interface from `templates/index.html`.
- **POST `/transcribe/`**: Accepts multiple audio files and returns their transcriptions.

## Example Usage

1. Open the application in your browser.
2. Upload audio files using the provided interface.
3. Click the "Generate" button to receive the report.

## Custom Report Format

You can access the `prompts` directory in `models` to customize the report format by describing the details of your report template.

## Dependencies

- FastAPI
- Faster-Whisper
- Torch
- Uvicorn
- Gemini-1.5-flash-002 (Google AI Studio)

## License

This project is licensed under the MIT License.