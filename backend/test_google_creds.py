"""Test script to verify Google Cloud Speech-to-Text credentials."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=" * 60)
print("Google Cloud Credentials Test")
print("=" * 60)

# Check if environment variable is set
creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print(f"\n1. Environment Variable Check:")
print(f"   GOOGLE_APPLICATION_CREDENTIALS = {creds_path}")

if not creds_path:
    print("   ❌ NOT SET - Please add to .env file")
    exit(1)
else:
    print("   ✅ SET")

# Check if file exists
print(f"\n2. File Existence Check:")
if os.path.exists(creds_path):
    print(f"   ✅ File exists at: {creds_path}")
    file_size = os.path.getsize(creds_path)
    print(f"   File size: {file_size} bytes")
else:
    print(f"   ❌ File NOT found at: {creds_path}")
    exit(1)

# Try to load credentials
print(f"\n3. Credentials Loading Test:")
try:
    from google.oauth2 import service_account
    credentials = service_account.Credentials.from_service_account_file(creds_path)
    print("   ✅ Credentials loaded successfully")
    print(f"   Service account email: {credentials.service_account_email}")
except Exception as e:
    print(f"   ❌ Failed to load credentials: {str(e)}")
    exit(1)

# Try to create Speech client
print(f"\n4. Speech Client Test:")
try:
    from google.cloud import speech_v1p1beta1 as speech
    client = speech.SpeechClient(credentials=credentials)
    print("   ✅ Speech client created successfully")
except Exception as e:
    print(f"   ❌ Failed to create client: {str(e)}")
    exit(1)

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
print("\nYour Google Cloud credentials are configured correctly.")
print("The transcription should work now.")
