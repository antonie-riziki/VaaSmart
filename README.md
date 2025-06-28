# Vaa Smart 👕🔥

**The AI-Powered Outfit Generator, Style Roaster & Fashion Visionary built for the bold.**

## 🌟 Features

### 👗 1. Daily Outfit Generator
- Returns tailored outfit suggestions based on:
  - Gender
  - Body type
  - Race
  - Style preferences
  - Occasion
  - Additional personal inputs
- Uses Google Gemini and NVIDIA Flux APIs for image generation.

### 🧠 2. Persona-Based Outfit Roast
- Upload your outfit and get roasted with flair and Nairobi slang.
- Choose your roaster:
  - 👵 Grandma Rosie – old-school drip hater
  - 💅 Kathy the Instagram Influencer – dramatic fashion police
  - 👔 Kabogo the ICT CS – tech-savvy government drip analyst
- Adjustable roast intensity:
  - ☕ Light Roast (gentle & witty)
  - 🔥 Medium Roast (sassy & sarcastic)
  - 💀 Dark Roast (no chill, pure savagery)

### 🧥 3. AI Image Generation
- Converts outfit prompts into visual outfit renderings.
- NVIDIA API integration with simplified prompt extraction for best results.
- Output displayed directly via Streamlit.

### 🔊 4. Voice Generation
- Converts AI responses to audio using ElevenLabs API.
- Playback integrated with Streamlit.
- BytesIO handling for generator-based responses.

## 📦 Technologies Used
- 🧠 Google Gemini 2.0
- 🎨 NVIDIA AI Image Generator (Flux)
- 🔊 ElevenLabs Text-to-Speech API
- 🖼️ Streamlit (frontend)
- 🐍 Python 3.11+

## 🛠️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/vaa-smart.git
   cd vaa-smart
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API keys:
   - Google Gemini
   - NVIDIA AI
   - ElevenLabs

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## 🧠 Sample Prompts

### ✅ Outfit Input Prompt
```python
Generate a weekly outfit schedule for:
Gender: Male
Body Type: Slim
Race: African
Outfit Style: Streetwear
Occasion: Weekend Chill
```

### 🔥 Roast Prompt
```python
Style Persona: Kabogo the ICT CS
Roast Intensity: 🔥 Medium Roast
Analyze the outfit image and roast appropriately.
```

## 🔮 System Instructions

- **Outfit Generator Model**: Returns outfit text only, no explanations.
- **Roast Model**: Adjusts tone based on persona and roast level.
- **Voice Model**: Converts text into MP3 with ElevenLabs, handles generators.

## ⚠️ Common Errors & Fixes

- `TypeError: a bytes-like object is required`: Wrap ElevenLabs audio generator using `b''.join(...)`.
- `Unexpected keyword argument 'config'`: Use correct SDK method signature.
- `500 Internal Server Error (NVIDIA)`: Simplify image prompts to keywords only.

## 📌 Roadmap

- [ ] Upload outfit via webcam 📷
- [ ] Add wardrobe syncing feature
- [ ] Style improvement suggestions after roast
- [ ] Social sharing for roasts

---

## ✨ Made with ❤️ for Nairobi streetwear, techies, and anyone who dares to drip different.
