![Baymax Waving](./baymax.jpg)

# Baymax Bot

> _"Hello! I am Baymax. Your personal healthcare companion"_

This project brings **Baymax**, the beloved robotic healthcare assistant from *Big Hero 6*, into the real world through a Telegram bot. It uses conversational AI, image understanding, and AI voice synthesis to provide simple, supportive health guidance — just like the original Baymax would.

Built using Google’s Gemini API, Resemble AI, and Telegram’s Bot API, the bot can chat, interpret images, and even speak in a voice that closely mimics Baymax’s warm, robotic tone.

---

## What This Bot Can Do

### 1. Conversational Health Support
- The bot begins every session with Baymax’s classic prompt:  
  _"Hello! I am Baymax, your personal healthcare companion. On a scale of 1 to 10, how would you rate your pain?"_
- Users can describe their symptoms, ask health questions, or just talk casually.
- Responses are short, empathetic, and medically grounded.

### 2. AI-Generated Baymax Voice
- Using **Resemble AI**, each text response is converted into speech.
- The voice is an AI-generated replica that closely resembles Baymax’s tone.
- Voice replies are sent to the user in `.ogg` format (Telegram-compatible).

### 3. Image-Based Health Understanding
- Users can send health-related images (e.g., prescriptions, lab reports).
- The bot uses **Google Gemini 1.5 Flash** to interpret and respond to the contents of the image in a helpful way.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| **Google Gemini 1.5 Flash** | Fast, free LLM for generating chat and image-based responses |
| **Resemble AI** | Converts text responses to AI-generated speech using a Baymax-like voice |
| **Telegram Bot API** | Frontend messaging interface |
| **Python** | Orchestrates backend logic |
| **Pillow (PIL)** | Image handling and processing |
| **Pydub** | Converts audio formats for Telegram compatibility |

---

## Try It Out

You can interact with the bot on Telegram at:  
**[@baymaxhealthcarecompanionbot](https://t.me/baymaxhealthcarecompanionbot)**

> **Note:** The bot is not currently deployed on a server. It only functions when the backend code is actively running by the developer.

---

## Beyond Telegram: Where This Could Go

- Can be adapted for **WhatsApp** using Twilio or Gupshup APIs to maintain the same conversational experience.  
- Easily integrated into **web applications** like health portals or student wellness sites with voice support via WebRTC and Gemini APIs.  
- Can be packaged as a lightweight, **voice-first mobile app** with offline or cloud interaction options.  
- Suitable for integration into **healthcare kiosks or low-power wearable devices** for clinics, elder care, or remote health setups.

---

## From Fun Idea to Functional AI

This project started off as a fun idea — just trying to bring a fictional character to life. But while building it, it became clear how much is possible today with the tools already out there. With the pace at which AI is evolving and how easy it is to plug into powerful APIs, you don’t need a massive teams or years of work to build something useful. Whether it’s a personal tutor, a mental health companion, a tool to help the elderly stay connected, or something that makes education or healthcare more accessible — the possibilities are huge. We’re at a point where if you can imagine it, you can probably build it. This bot is an example, but it shows how far a simple idea can go.

Whether you're here to relive a bit of animated nostalgia or explore the future of assistive technology, this bot proves how quickly meaningful, character-driven interfaces can be built using the tools now available.

> _"I will now deactivate. Are you satisfied with your care?"_
