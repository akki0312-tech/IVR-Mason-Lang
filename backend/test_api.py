"""Test actual Google Cloud Speech-to-Text API call."""

import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 70)
print("Google Cloud Speech-to-Text API Test")
print("=" * 70)

# Step 1: Load credentials
print("\n[1/4] Loading credentials...")
try:
    from google.oauth2 import service_account
    from google.cloud import speech_v1p1beta1 as speech
    
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    print(f"  Credentials path: {creds_path}")
    
    credentials = service_account.Credentials.from_service_account_file(creds_path)
    print(f"  ✅ Loaded credentials for: {credentials.service_account_email}")
except Exception as e:
    print(f"  ❌ Failed: {e}")
    exit(1)

# Step 2: Create client
print("\n[2/4] Creating Speech client...")
try:
    client = speech.SpeechClient(credentials=credentials)
    print("  ✅ Client created")
except Exception as e:
    print(f"  ❌ Failed: {e}")
    exit(1)

# Step 3: Create a simple test audio (silence)
print("\n[3/4] Creating test audio...")
try:
    # Create 1 second of silence as test audio (WAV format)
    import wave
    import struct
    
    test_audio_path = "test_audio.wav"
    with wave.open(test_audio_path, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(16000)  # 16kHz
        # Write 1 second of silence
        for _ in range(16000):
            wav_file.writeframes(struct.pack('h', 0))
    
    print(f"  ✅ Created test audio: {test_audio_path}")
except Exception as e:
    print(f"  ❌ Failed: {e}")
    exit(1)

# Step 4: Try actual API call
print("\n[4/4] Testing API call...")
try:
    with open(test_audio_path, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-IN",
    )
    
    print("  Sending request to Google Cloud...")
    response = client.recognize(config=config, audio=audio)
    print("  ✅ API call successful!")
    print(f"  Response: {response}")
    
except Exception as e:
    print(f"  ❌ API call failed!")
    print(f"  Error type: {type(e).__name__}")
    print(f"  Error message: {str(e)}")
    print("\n" + "=" * 70)
    print("POSSIBLE CAUSES:")
    print("=" * 70)
    print("1. Speech-to-Text API not enabled in Google Cloud Console")
    print("   → Go to: https://console.cloud.google.com/apis/library/speech.googleapis.com")
    print("   → Click 'ENABLE'")
    print("\n2. Service account lacks permissions")
    print("   → Service account needs 'Cloud Speech Client' role")
    print("\n3. Billing not enabled")
    print("   → Google Cloud requires billing account (even for free tier)")
    print("\n4. API quota exceeded")
    print("   → Check quota in Google Cloud Console")
    print("=" * 70)
    exit(1)

# Cleanup
os.remove(test_audio_path)

print("\n" + "=" * 70)
print("✅ ALL TESTS PASSED! Google Cloud Speech-to-Text is working!")
print("=" * 70)
