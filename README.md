# WhatsApp GI Health Chatbot 🏥💬

A free WhatsApp chatbot for helping patients learn about common gastrointestinal conditions and schedule appointments.

## 🎯 Features

- **6 Common GI Conditions Covered:**
  - GERD/Heartburn
  - IBS (Irritable Bowel Syndrome)
  - Constipation
  - Diarrhea
  - Gastritis
  - Hemorrhoids

- **Menu-Driven Flow:** Patients choose from options (no open-ended questions)
- **Appointment Scheduling:** Easy guidance to book appointments
- **Red Flag Warnings:** Important symptoms that require immediate medical attention
- **Self-Care Tips:** Practical advice for each condition

## 📦 What's Included

- `whatsapp_gi_bot.py` - Main chatbot application
- `requirements.txt` - Python dependencies
- `Procfile` - Railway deployment configuration
- `SETUP_GUIDE.md` - Complete step-by-step setup instructions
- `website_integration.html` - 5 different WhatsApp button examples for your website

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8+
- A Twilio account (free tier works!)
- A Railway account (free tier works!)

### 2. Test Locally (Optional)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the bot
python whatsapp_gi_bot.py

# In another terminal, expose to internet
ngrok http 5000
```

### 3. Deploy to Railway
```bash
# Install Railway CLI
curl -fsSL https://railway.app/install.sh | sh

# Login
railway login

# Deploy
railway init
railway up

# Get your URL
railway domain
```

### 4. Configure Twilio
1. Sign up at https://www.twilio.com/try-twilio
2. Go to Messaging → WhatsApp Sandbox
3. Set webhook URL to: `https://your-app.railway.app/whatsapp`
4. Save and test!

## 🌐 Add to Your Website

Choose from 5 integration examples in `website_integration.html`:
1. Simple button
2. Floating widget (most popular!)
3. Widget with tooltip
4. Call-to-action card
5. Mobile-only bottom bar

## 📝 Customization

### Update Your Contact Info
Edit these lines in `whatsapp_gi_bot.py`:
```python
📞 Call: [YOUR PHONE NUMBER]
📧 Email: [YOUR EMAIL]
🌐 Website: [YOUR BOOKING URL]
```

### Add More Conditions
Add to the `GI_CONDITIONS` dictionary:
```python
"7": {
    "name": "Your Condition",
    "info": """Your detailed information here..."""
}
```

### Change Welcome Message
Edit the `MAIN_MENU` variable.

## 💰 Cost

- **Development:** 100% FREE
- **Twilio Trial:** Free $15 credit
- **Railway:** Free tier (500 hours/month)
- **WhatsApp Business API:** First 1,000 conversations/month FREE

After free tier:
- Railway: ~$5/month
- WhatsApp: ~$0.005 per conversation

## 📖 Documentation

See `SETUP_GUIDE.md` for:
- Detailed setup instructions
- Troubleshooting tips
- Going to production
- Advanced features

## 🔒 Privacy & Compliance

**Note:** This bot is for informational purposes only and does not:
- Store personal health information
- Provide medical diagnosis
- Replace professional medical advice
- Require HIPAA compliance (no PHI collected)

Always encourage patients to consult healthcare professionals for medical concerns.

## 🐛 Troubleshooting

### Bot not responding?
1. Check Railway logs: `railway logs`
2. Verify webhook URL in Twilio
3. Ensure you joined the sandbox

### Local testing issues?
1. Make sure port 5000 is available
2. Check firewall settings
3. Verify ngrok is running

## 📞 Support

For setup help or customization questions, refer to:
1. `SETUP_GUIDE.md` - Comprehensive setup guide
2. Twilio Docs - https://www.twilio.com/docs/whatsapp
3. Railway Docs - https://docs.railway.app

## ⚖️ License

Free to use and modify for your medical practice.

## 🎓 Learn More

- Twilio WhatsApp API: https://www.twilio.com/docs/whatsapp
- Flask Documentation: https://flask.palletsprojects.com/
- Railway Platform: https://railway.app

---

**Made with ❤️ for healthcare providers**

Questions? Check the SETUP_GUIDE.md or feel free to customize the code to fit your needs!
