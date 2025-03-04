from flask import Flask, request, jsonify
import whisper
import tempfile
import os
import torch
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Check for CUDA availability
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Using device: {device}")

# Load model with CUDA support
try:
    model = whisper.load_model("small.en").to(device)  # Move model to GPU
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    raise

@app.route('/audio/transcriptions', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        logger.error("No file provided in request")
        return jsonify({"error": "No file provided"}), 400

    audio_file = request.files['file']
    logger.info(f"Received file: {audio_file.filename}")

    try:
        # Create a temporary file and ensure it's closed before transcription
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp_path = tmp.name
            audio_file.save(tmp_path)
            logger.info(f"Saved file to temporary location: {tmp_path}")

        # Run transcription (no need to pass 'device' here)
        result = model.transcribe(tmp_path, fp16=torch.cuda.is_available())
        logger.info("Transcription completed successfully")

        # Delete the temporary file after transcription
        try:
            os.remove(tmp_path)
            logger.info(f"Temporary file {tmp_path} deleted")
        except Exception as e:
            logger.error(f"Failed to delete temporary file: {e}")

        return jsonify({
            "text": result["text"],
            "language": result["language"],
            "device": device
        })
        
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='******THIS_MACHINES_IP_ADDRESS******', port=5000)