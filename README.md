# Telegram Bot on Firebase

A simple echo bot that runs 24/7 using Firebase Cloud Functions.

## Setup
1. **Get your Telegram token** from [@BotFather](https://t.me/BotFather).
2. **Deploy to Firebase**:
   ```bash
   firebase functions:config:set telegram.token="YOUR_BOT_TOKEN"
   firebase deploy --only functions
