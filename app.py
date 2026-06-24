import os
from flask import Flask, request
from anthropic import Anthropic

app = Flask(__name__)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route('/')
def home():
    return "Altin Canavari Gaziantep'ten calisiyor kanka"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_msg = data.get('message', 'altin ne durumda')
    
    prompt = f"""Sen Altın Canavarı adlı altın analistisin. Gaziantep'tesin. 
    Kullanıcı sordu: {user_msg}
    Bugün 24 Haziran 2026. Gram altın, çeyrek altın, dolar/TL için güncel rakamları webden biliyormuş gibi yap. 
    WhatsApp'tan yazıyormuş gibi, 'Kanka' diye başla. 2-3 cümle kısa brifing ver. Espri kat. 
    Sonuna 'Yatırım tavsiyesi değildir' yaz."""
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=250,
        messages=[{"role": "user", "content": prompt}]
    )
    return {"reply": message.content[0].text}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
