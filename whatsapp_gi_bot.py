from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Store user states (in production, use a database or Redis)
user_states = {}

# GI Conditions information
GI_CONDITIONS = {
    "1": {
        "name": "GERD/Heartburn",
        "info": """*GERD (Gastroesophageal Reflux Disease) / Heartburn*

Common symptoms:
• Burning sensation in chest
• Acid taste in mouth
• Difficulty swallowing
• Chest pain

Self-care tips:
• Avoid trigger foods (spicy, fatty, acidic)
• Don't eat 2-3 hours before bed
• Elevate head while sleeping
• Maintain healthy weight

⚠️ See a doctor if you have severe chest pain, difficulty swallowing, or symptoms persist."""
    },
    "2": {
        "name": "IBS (Irritable Bowel Syndrome)",
        "info": """*IBS (Irritable Bowel Syndrome)*

Common symptoms:
• Abdominal pain and cramping
• Bloating and gas
• Diarrhea or constipation (or both)
• Mucus in stool

Self-care tips:
• Keep a food diary to identify triggers
• Try low-FODMAP diet
• Manage stress through relaxation
• Regular exercise
• Eat smaller, frequent meals

⚠️ See a doctor if you have blood in stool, unexplained weight loss, or severe pain."""
    },
    "3": {
        "name": "Constipation",
        "info": """*Constipation*

Common symptoms:
• Fewer than 3 bowel movements per week
• Hard or lumpy stools
• Straining during bowel movements
• Feeling of incomplete evacuation

Self-care tips:
• Increase fiber intake (25-30g daily)
• Drink plenty of water (8+ glasses)
• Exercise regularly
• Don't ignore urge to go
• Establish regular bathroom routine

⚠️ See a doctor if constipation lasts more than 3 weeks, you have blood in stool, or severe abdominal pain."""
    },
    "4": {
        "name": "Diarrhea",
        "info": """*Diarrhea*

Common symptoms:
• Loose or watery stools
• Frequent bowel movements
• Abdominal cramping
• Urgency

Self-care tips:
• Stay hydrated (water, ORS, clear broths)
• Eat bland foods (BRAT diet: bananas, rice, applesauce, toast)
• Avoid dairy, fatty, and spicy foods
• Rest adequately

⚠️ See a doctor if diarrhea lasts more than 2 days, you have signs of dehydration, bloody stools, or high fever."""
    },
    "5": {
        "name": "Gastritis",
        "info": """*Gastritis (Stomach Inflammation)*

Common symptoms:
• Upper abdominal pain or discomfort
• Nausea and vomiting
• Feeling full after eating
• Loss of appetite

Self-care tips:
• Eat smaller, frequent meals
• Avoid irritants (alcohol, NSAIDs, spicy foods)
• Reduce stress
• Avoid smoking

⚠️ See a doctor if you vomit blood, have black stools, or severe persistent pain."""
    },
    "6": {
        "name": "Hemorrhoids",
        "info": """*Hemorrhoids (Piles)*

Common symptoms:
• Rectal bleeding during bowel movements
• Itching or irritation in anal area
• Pain or discomfort
• Swelling around anus

Self-care tips:
• Increase fiber and water intake
• Avoid straining during bowel movements
• Use warm sitz baths
• Apply over-the-counter creams
• Don't sit for long periods

⚠️ See a doctor if bleeding is heavy, you have severe pain, or symptoms don't improve in a week."""
    }
}

MAIN_MENU = """Welcome! 👋

I'm here to help with common GI conditions.

Please choose a condition:
1️⃣ GERD/Heartburn
2️⃣ IBS (Irritable Bowel Syndrome)
3️⃣ Constipation
4️⃣ Diarrhea
5️⃣ Gastritis
6️⃣ Hemorrhoids
7️⃣ My condition is not listed
8️⃣ Schedule an appointment

Reply with the number of your choice."""

APPOINTMENT_MESSAGE = """📅 *Schedule an Appointment*

To book an appointment with our GI specialist:

📞 Call: [YOUR PHONE NUMBER]
📧 Email: [YOUR EMAIL]
🌐 Website: [YOUR BOOKING URL]

Our team will get back to you within 24 hours.

Would you like to:
9️⃣ Return to main menu
0️⃣ End conversation"""


def get_user_state(phone_number):
    return user_states.get(phone_number, "main_menu")


def set_user_state(phone_number, state):
    user_states[phone_number] = state


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    from_number = request.values.get("From", "")
    
    resp = MessagingResponse()
    msg = resp.message()
    
    current_state = get_user_state(from_number)
    
    # Handle main menu state or welcome messages
    if incoming_msg.lower() in ["menu", "start", "hi", "hello"]:
        msg.body(MAIN_MENU)
        set_user_state(from_number, "main_menu")
    
    # Handle condition selection
    elif incoming_msg in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        if incoming_msg in GI_CONDITIONS:
            condition_info = GI_CONDITIONS[incoming_msg]
            response = f"{condition_info['info']}\n\n"
            response += "What would you like to do?\n"
            response += "8️⃣ Schedule an appointment\n"
            response += "9️⃣ Return to main menu\n"
            response += "0️⃣ End conversation"
            
            msg.body(response)
            set_user_state(from_number, "after_info")
        
        elif incoming_msg == "7":
            msg.body("I understand your condition isn't listed here.\n\n" + APPOINTMENT_MESSAGE)
            set_user_state(from_number, "appointment")
        
        elif incoming_msg == "8":
            msg.body(APPOINTMENT_MESSAGE)
            set_user_state(from_number, "appointment")
        
        else:
            msg.body("Please enter a valid option (1-8).\n\n" + MAIN_MENU)
    
    # Handle after viewing condition info
    elif current_state == "after_info":
        if incoming_msg == "8":
            msg.body(APPOINTMENT_MESSAGE)
            set_user_state(from_number, "appointment")
        
        elif incoming_msg == "9":
            msg.body(MAIN_MENU)
            set_user_state(from_number, "main_menu")
        
        elif incoming_msg == "0":
            msg.body("Thank you for using our GI Health Bot! Take care. 👋\n\nType 'menu' anytime to start again.")
            set_user_state(from_number, "ended")
        
        else:
            msg.body("Please choose a valid option:\n8️⃣ Schedule appointment\n9️⃣ Main menu\n0️⃣ End")
            set_user_state(from_number, "after_info")
    
    # Handle appointment state
    elif current_state == "appointment":
        if incoming_msg == "9":
            msg.body(MAIN_MENU)
            set_user_state(from_number, "main_menu")
        
        elif incoming_msg == "0":
            msg.body("Thank you! We look forward to seeing you. 👋\n\nType 'menu' anytime to start again.")
            set_user_state(from_number, "ended")
        
        else:
            msg.body("Our team will contact you soon!\n\n9️⃣ Main menu\n0️⃣ End conversation")
    
    # Handle ended state or any other input
    else:
        msg.body(MAIN_MENU)
        set_user_state(from_number, "main_menu")
    
    return str(resp)


@app.route("/", methods=["GET"])
def home():
    return """
    <h1>GI Chatbot is running!</h1>
    <p>Configure your Twilio webhook to point to /whatsapp</p>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5000)
