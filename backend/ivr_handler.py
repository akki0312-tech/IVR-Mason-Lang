from gtts import gTTS
import tempfile
import os
import re
from language_config import (
    QUESTIONS, CONFIRMATIONS, ERROR_MESSAGES,
    CONFIRMATION_WORDS, LANGUAGE_CODES, TTS_LANGUAGE_CODES
)

# In-memory session store
SESSIONS = {}

# Fields to collect from user
FIELDS = ["name", "age", "number", "address", "pay"]


def start_session(session_id: str, language: str = "en"):
    """Initialize a new IVR session with language preference."""
    SESSIONS[session_id] = {f: None for f in FIELDS}
    SESSIONS[session_id]["current_field"] = FIELDS[0]
    SESSIONS[session_id]["awaiting_confirmation"] = False
    SESSIONS[session_id]["language"] = language  # Store language preference


def reset_session(session_id: str):
    """Reset and clear a session."""
    if session_id in SESSIONS:
        del SESSIONS[session_id]


def get_initial_question(session_id: str, language: str = "en"):
    """Get the welcome message and first question without requiring audio input."""
    # Initialize session with language
    start_session(session_id, language)
    
    # Get first question in selected language
    assistant_text = QUESTIONS[language]["name"]
    
    # Generate TTS in selected language
    audio_file = synthesize_speech(assistant_text, language)
    
    return {
        "assistant_text": assistant_text,
        "finished": False,
        "fields": {f: None for f in FIELDS},
        "audio_file": audio_file
    }


def synthesize_speech(text: str, language: str = "en") -> str:
    """Generate TTS audio file using gTTS and return file path."""
    tts_lang = TTS_LANGUAGE_CODES.get(language, "en")
    tts = gTTS(text=text, lang=tts_lang, slow=False)
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp_file.name)
    return tmp_file.name


def process_turn(session_id: str, user_text: str):
    """Process a user turn with natural conversation flow."""
    if session_id not in SESSIONS:
        start_session(session_id)

    session = SESSIONS[session_id]
    current_field = session["current_field"]
    language = session.get("language", "en")  # Get language from session

    print(f"[IVR] User said: '{user_text}' (Language: {language})")
    
    # CASE 1: Waiting for CORRECT/INCORRECT confirmation
    if session["awaiting_confirmation"]:
        # Clean and normalize the user text
        cleaned_text = user_text.strip().lower()
        print(f"[IVR] Checking confirmation. Cleaned text: '{cleaned_text}'")
        
        # Handle empty or very short transcriptions
        if len(cleaned_text) < 2:
            print(f"[IVR] Transcription too short or empty. Asking to repeat.")
            assistant_text = ERROR_MESSAGES[language]["empty"]
            finished = False
        else:
            # Check for INCORRECT/NO - be very flexible
            is_no = False
            
            # Get language-specific no words
            no_words = CONFIRMATION_WORDS[language]["no"]
            
            # Check if any no word is in the cleaned text
            for word in no_words:
                if word in cleaned_text:
                    is_no = True
                    break
                
            print(f"[IVR] Detection result - is_no: {is_no}")
            
            # DEFAULT TO YES/CORRECT unless user clearly said NO/INCORRECT
            if not is_no:
                # User confirmed (or didn't clearly say no) - move to next field
                print(f"[IVR] User confirmed! Moving to next field.")
                session["awaiting_confirmation"] = False
                next_index = FIELDS.index(current_field) + 1

                if next_index < len(FIELDS):
                    session["current_field"] = FIELDS[next_index]
                    # Smooth transition to next question
                    next_question = QUESTIONS[language][session['current_field']]
                    
                    # Language-specific "Excellent!" prefix
                    excellent_prefix = {
                        "en": "Excellent!",
                        "hi": "बहुत बढ़िया!",
                        "ta": "அருமை!"
                    }
                    assistant_text = f"{excellent_prefix[language]} {next_question}"
                    finished = False
                else:
                    # All fields collected - warm completion message
                    name = session.get("name", "there")
                    
                    # Language-specific completion messages
                    completion_messages = {
                        "en": (
                            f"Perfect, {name}! We've got all your information. "
                            f"Thank you for applying with MASON! "
                            f"We'll review your application and get back to you soon at {session.get('number')}. "
                            f"Have a great day!"
                        ),
                        "hi": (
                            f"बिल्कुल सही, {name}! हमें आपकी सभी जानकारी मिल गई है। "
                            f"MASON के साथ आवेदन करने के लिए धन्यवाद! "
                            f"हम आपके आवेदन की समीक्षा करेंगे और जल्द ही {session.get('number')} पर संपर्क करेंगे। "
                            f"आपका दिन शुभ हो!"
                        ),
                        "ta": (
                            f"சரியானது, {name}! உங்கள் அனைத்து தகவல்களையும் பெற்றுவிட்டோம். "
                            f"MASON உடன் விண்ணப்பித்ததற்கு நன்றி! "
                            f"உங்கள் விண்ணப்பத்தை மதிப்பாய்வு செய்து விரைவில் {session.get('number')} இல் தொடர்பு கொள்வோம். "
                            f"நல்ல நாள்!"
                        )
                    }
                    assistant_text = completion_messages[language]
                    finished = True
                    reset_session(session_id)
            else:
                # User clearly said no - friendly retry
                print(f"[IVR] User said no. Asking again.")
                question = QUESTIONS[language][current_field]
                assistant_text = ERROR_MESSAGES[language]["retry"].format(question=question)
                session["awaiting_confirmation"] = False
                finished = False

    # CASE 2: Normal input - save value and ask for confirmation
    else:
        # Special validation for phone number
        if current_field == "number":
            digits = re.sub(r"\D", "", user_text)
            if len(digits) < 10:
                assistant_text = ERROR_MESSAGES[language]["number"]
                audio_file = synthesize_speech(assistant_text, language)
                return {
                    "assistant_text": assistant_text,
                    "finished": False,
                    "fields": {f: session.get(f) for f in FIELDS},
                    "audio_file": audio_file
                }
            # Format phone number nicely
            formatted_number = f"{digits[:3]} {digits[3:6]} {digits[6:10]}"
            session["number"] = digits
            confirmation_value = formatted_number

        # Special validation for age
        elif current_field == "age":
            digits = re.sub(r"\D", "", user_text)
            if not digits or not (18 <= int(digits) < 120):
                assistant_text = ERROR_MESSAGES[language]["age"]
                audio_file = synthesize_speech(assistant_text, language)
                return {
                    "assistant_text": assistant_text,
                    "finished": False,
                    "fields": {f: session.get(f) for f in FIELDS},
                    "audio_file": audio_file
                }
            session["age"] = digits
            confirmation_value = digits

        # Special validation for pay
        elif current_field == "pay":
            digits = re.sub(r"\D", "", user_text)
            if not digits:
                assistant_text = ERROR_MESSAGES[language]["pay"]
                audio_file = synthesize_speech(assistant_text, language)
                return {
                    "assistant_text": assistant_text,
                    "finished": False,
                    "fields": {f: session.get(f) for f in FIELDS},
                    "audio_file": audio_file
                }
            session["pay"] = digits
            confirmation_value = digits

        else:
            # For name and address, use as-is
            session[current_field] = user_text.strip()
            confirmation_value = user_text.strip()

        # Ask for confirmation with contextual message in selected language
        assistant_text = CONFIRMATIONS[language][current_field].format(value=confirmation_value)
        session["awaiting_confirmation"] = True
        finished = False

    # Generate TTS output in selected language
    audio_file = synthesize_speech(assistant_text, language)

    return {
        "assistant_text": assistant_text,
        "finished": finished,
        "fields": {f: session.get(f) for f in FIELDS},
        "audio_file": audio_file
    }
