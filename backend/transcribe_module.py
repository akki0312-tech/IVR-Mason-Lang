"""Audio transcription using Google Cloud Speech-to-Text API."""

import os
import base64
import json
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()


def transcribe_audio(file_path: str, language_code: str = "en-IN") -> str:
    """
    Transcribe audio file using Google Cloud Speech-to-Text API.
    Optimized for IVR systems with telephony model and multi-language support.
    
    Args:
        file_path: Path to audio file (webm, wav, mp3, etc.)
        language_code: Language code for transcription (en-IN, hi-IN, ta-IN, etc.)
        
    Returns:
        Transcribed text
        
    Raises:
        FileNotFoundError: If audio file doesn't exist
        RuntimeError: If transcription fails
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Load Google Cloud credentials
        # PRIORITY 1: Base64 string (for Production/Railway)
        credentials_base64 = os.getenv("GOOGLE_CREDENTIALS_BASE64")
        
        if credentials_base64:
            try:
                # Decode base64 to JSON string
                credentials_json = base64.b64decode(credentials_base64).decode("utf-8")
                # Parse JSON string to dict
                credentials_dict = json.loads(credentials_json)
                # Create credentials object
                credentials = service_account.Credentials.from_service_account_info(credentials_dict)
                print("[TRANSCRIBE] Using Base64 credentials")
            except Exception as e:
                print(f"[TRANSCRIBE ERROR] Failed to decode base64 credentials: {str(e)}")
                return "[Transcription unavailable - Invalid Base64 credentials]"
        else:
            # PRIORITY 2: File path (for Local Development)
            credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            if not credentials_path:
                print("[TRANSCRIBE WARNING] GOOGLE_APPLICATION_CREDENTIALS not set")
                return "[Transcription unavailable - Please configure Google Cloud credentials]"
            
            if not os.path.exists(credentials_path):
                print(f"[TRANSCRIBE WARNING] Credentials file not found: {credentials_path}")
                return "[Transcription unavailable - Google Cloud credentials file not found]"
            
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
            print(f"[TRANSCRIBE] Using credentials file: {credentials_path}")

        client = speech.SpeechClient(credentials=credentials)
        
        # Read audio file
        with open(file_path, "rb") as audio_file:
            content = audio_file.read()
        
        audio = speech.RecognitionAudio(content=content)
        
        # Detect audio format from file extension
        file_ext = os.path.splitext(file_path)[1].lower()
        
        # Map file extensions to Google Cloud audio encodings
        encoding_map = {
            ".webm": speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
            ".wav": speech.RecognitionConfig.AudioEncoding.LINEAR16,
            ".mp3": speech.RecognitionConfig.AudioEncoding.MP3,
            ".ogg": speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        }
        
        encoding = encoding_map.get(file_ext, speech.RecognitionConfig.AudioEncoding.WEBM_OPUS)
        
        # Configure recognition with specified language
        config = speech.RecognitionConfig(
            encoding=encoding,
            sample_rate_hertz=48000,  # Common sample rate for web audio
            language_code=language_code,  # Use specified language
            use_enhanced=True,  # Enhanced model for better accuracy
            enable_automatic_punctuation=True,
            # Alternative candidates for better accuracy
            max_alternatives=1,
        )
        
        print(f"[TRANSCRIBE] Processing {file_path} with language: {language_code}")
        
        # Perform transcription
        response = client.recognize(config=config, audio=audio)
        
        # Extract text from response
        if response.results and len(response.results) > 0:
            transcript = response.results[0].alternatives[0].transcript.strip()
            print(f"[TRANSCRIBE] Result: '{transcript}'")
            return transcript
        else:
            print("[TRANSCRIBE] No transcription results returned")
            return ""
            
    except FileNotFoundError as e:
        print(f"[TRANSCRIBE ERROR] {str(e)}")
        return "[Transcription unavailable - File error]"
    except Exception as e:
        print(f"[TRANSCRIBE ERROR] {str(e)}")
        # Return a helpful fallback message instead of crashing
        return f"[Transcription error: {str(e)[:100]}]"
