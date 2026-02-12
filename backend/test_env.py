"""Simple test to check if .env file is being loaded."""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Try to load .env
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ dotenv loaded")
except Exception as e:
    print(f"❌ dotenv failed: {e}")

# Check environment variable
google_creds = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print(f"\nGOOGLE_APPLICATION_CREDENTIALS = {google_creds}")

if google_creds:
    print(f"✅ Environment variable is set")
    if os.path.exists(google_creds):
        print(f"✅ File exists at path")
    else:
        print(f"❌ File NOT found at path")
else:
    print("❌ Environment variable NOT set")
    print("\nChecking .env file contents:")
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            for line in f:
                if "GOOGLE" in line:
                    print(f"  {line.strip()}")
    else:
        print("  .env file not found!")
