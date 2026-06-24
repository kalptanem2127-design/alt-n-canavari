from flask import Flask, request, render_template_string
import anthropic
import os

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

HTML = """
<!DOCTYPE html>
<html>
<head><title>Altın Canavarı</title></head>
<body style="font-family:sans-serif; max-width:600px; margin:50px auto; padding:20px;">
    <h1>Altın Canavarı - Gaziantep</h1>
    <form method="post">
        <button type="submit" style="padding:15px 30px; font-size:18px;">Altın Analizi Getir</button>
    </form>
    {% if analiz %}
        <h3>Bugünün Analizi:</h3>
        <pre style="background:#f4f4f4; padding:15px; white-space:pre-wrap;">{{ analiz }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    analiz = None
    if request.method == "POST":
        msg = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[{"role": "user", "content": "Gaziantep'li bir kuyumcuya kısa, net altın analizi yap. Bugün gram altın al-sat tavsiyesi ver. 3 madde."}]
        )
        analiz = msg.content[0].text
    return render_template_string(HTML, analiz=analiz)

if __name__ == "__main__":
    app.run()
