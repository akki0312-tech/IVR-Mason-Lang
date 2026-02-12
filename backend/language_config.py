# Multi-language support for MASON IVR
# Contains all prompts, confirmations, and error messages in English, Hindi, and Tamil

# Multi-language prompts
QUESTIONS = {
    "en": {
        "name": "Hello! Welcome to MASON job application. Let's get started. What's your full name?",
        "age": "Great! And how old are you?",
        "number": "Perfect. What's the best phone number to reach you at?",
        "address": "Got it. Where do you currently live? Please tell me your full address.",
        "pay": "Almost done! What monthly salary are you looking for?"
    },
    "hi": {
        "name": "नमस्ते! MASON नौकरी आवेदन में आपका स्वागत है। चलिए शुरू करते हैं। आपका पूरा नाम क्या है?",
        "age": "बहुत अच्छा! और आपकी उम्र क्या है?",
        "number": "बढ़िया। आपसे संपर्क करने के लिए सबसे अच्छा फोन नंबर क्या है?",
        "address": "समझ गया। आप वर्तमान में कहाँ रहते हैं? कृपया अपना पूरा पता बताएं।",
        "pay": "लगभग हो गया! आप कितनी मासिक वेतन की उम्मीद कर रहे हैं?"
    },
    "ta": {
        "name": "வணக்கம்! MASON வேலை விண்ணப்பத்திற்கு வரவேற்கிறோம். தொடங்குவோம். உங்கள் முழு பெயர் என்ன?",
        "age": "நல்லது! உங்கள் வயது என்ன?",
        "number": "சரி. உங்களை தொடர்பு கொள்ள சிறந்த தொலைபேசி எண் என்ன?",
        "address": "புரிந்தது. நீங்கள் தற்போது எங்கு வசிக்கிறீர்கள்? உங்கள் முழு முகவரியை சொல்லுங்கள்.",
        "pay": "கிட்டத்தட்ட முடிந்தது! நீங்கள் எவ்வளவு மாதாந்திர சம்பளம் எதிர்பார்க்கிறீர்கள்?"
    }
}

CONFIRMATIONS = {
    "en": {
        "name": "I heard your name as {value}. Is that correct? Please say 'correct' or 'incorrect'.",
        "age": "So you're {value} years old, right? Please say 'correct' or 'incorrect'.",
        "number": "Let me confirm - your phone number is {value}. Is that right? Please say 'correct' or 'incorrect'.",
        "address": "Your address is {value}. Did I get that correctly? Please say 'correct' or 'incorrect'.",
        "pay": "You're looking for {value} rupees per month. Is that correct? Please say 'correct' or 'incorrect'."
    },
    "hi": {
        "name": "मैंने आपका नाम {value} सुना। क्या यह सही है? कृपया 'सही' या 'गलत' कहें।",
        "age": "तो आप {value} साल के हैं, है ना? कृपया 'सही' या 'गलत' कहें।",
        "number": "पुष्टि करता हूं - आपका फोन नंबर {value} है। क्या यह सही है? कृपया 'सही' या 'गलत' कहें।",
        "address": "आपका पता {value} है। क्या मैंने सही समझा? कृपया 'सही' या 'गलत' कहें।",
        "pay": "आप {value} रुपये प्रति माह की तलाश कर रहे हैं। क्या यह सही है? कृपया 'सही' या 'गलत' कहें।"
    },
    "ta": {
        "name": "உங்கள் பெயர் {value} என்று கேட்டேன். இது சரியா? 'சரி' அல்லது 'தவறு' என்று சொல்லுங்கள்.",
        "age": "நீங்கள் {value} வயது, இல்லையா? 'சரி' அல்லது 'தவறு' என்று சொல்லுங்கள்.",
        "number": "உறுதிப்படுத்துகிறேன் - உங்கள் தொலைபேசி எண் {value}. இது சரியா? 'சரி' அல்லது 'தவறு' என்று சொல்லுங்கள்.",
        "address": "உங்கள் முகவரி {value}. நான் சரியாகப் புரிந்துகொண்டேனா? 'சரி' அல்லது 'தவறு' என்று சொல்லுங்கள்.",
        "pay": "நீங்கள் மாதம் {value} ரூபாய் எதிர்பார்க்கிறீர்கள். இது சரியா? 'சரி' அல்லது 'தவறு' என்று சொல்லுங்கள்."
    }
}

ERROR_MESSAGES = {
    "en": {
        "number": "I didn't quite catch that. Could you please say your 10-digit phone number again? You can say it digit by digit if that helps.",
        "age": "Sorry, I couldn't understand your age. Could you please tell me how old you are? Just say the number.",
        "pay": "I couldn't catch the salary amount. Could you please tell me your expected monthly pay again?",
        "empty": "Sorry, I didn't catch that. Could you please say 'correct' or 'incorrect'?",
        "retry": "No problem! Let me ask again. {question}"
    },
    "hi": {
        "number": "मुझे वह समझ नहीं आया। क्या आप कृपया अपना 10 अंकों का फोन नंबर फिर से बता सकते हैं? आप इसे अंक दर अंक बोल सकते हैं।",
        "age": "क्षमा करें, मुझे आपकी उम्र समझ नहीं आई। कृपया बताएं कि आप कितने साल के हैं? बस संख्या बोलें।",
        "pay": "मुझे वेतन राशि समझ नहीं आई। कृपया अपनी अपेक्षित मासिक वेतन फिर से बताएं?",
        "empty": "क्षमा करें, मुझे वह समझ नहीं आया। कृपया 'सही' या 'गलत' कहें।",
        "retry": "कोई बात नहीं! मैं फिर से पूछता हूं। {question}"
    },
    "ta": {
        "number": "எனக்கு அது புரியவில்லை. உங்கள் 10 இலக்க தொலைபேசி எண்ணை மீண்டும் சொல்ல முடியுமா? நீங்கள் அதை இலக்கம் இலக்கமாக சொல்லலாம்.",
        "age": "மன்னிக்கவும், உங்கள் வயது புரியவில்லை. நீங்கள் எத்தனை வயது என்று சொல்ல முடியுமா? எண்ணை மட்டும் சொல்லுங்கள்.",
        "pay": "சம்பள தொகை புரியவில்லை. உங்கள் எதிர்பார்க்கும் மாதாந்திர சம்பளத்தை மீண்டும் சொல்ல முடியுமா?",
        "empty": "மன்னிக்கவும், எனக்கு அது புரியவில்லை. 'சரி' அல்லது 'தவறு' என்று சொல்லுங்கள்.",
        "retry": "பரவாயில்லை! நான் மீண்டும் கேட்கிறேன். {question}"
    }
}

# Language-specific confirmation words
CONFIRMATION_WORDS = {
    "en": {
        "yes": ["correct", "right", "yes", "yeah", "yep", "ok", "okay"],
        "no": ["incorrect", "wrong", "no", "nope", "nah"]
    },
    "hi": {
        "yes": ["सही", "ठीक", "हाँ", "जी", "बिल्कुल"],
        "no": ["गलत", "नहीं", "ना"]
    },
    "ta": {
        "yes": ["சரி", "ஆம்", "சரியானது", "நல்லது"],
        "no": ["தவறு", "இல்லை", "தவறானது"]
    }
}

# Google Cloud Speech-to-Text language codes
LANGUAGE_CODES = {
    "en": "en-IN",  # Indian English
    "hi": "hi-IN",  # Hindi
    "ta": "ta-IN"   # Tamil
}

# gTTS language codes
TTS_LANGUAGE_CODES = {
    "en": "en",
    "hi": "hi",
    "ta": "ta"
}
