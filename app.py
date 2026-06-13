from flask import Flask, render_template_string, request
import os, datetime

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
<title>Automation Tool</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#0a0c0f;color:#00ff41;font-family:monospace;padding:16px}
h1{text-align:center;text-shadow:0 0 10px #00ff41}
.card{border:1px solid #1a2a1a;padding:12px;margin:10px 0;background:#0f1318}
input,select,textarea{background:#111;color:#00ff41;border:1px solid #00ff41;padding:8px;width:100%;margin:6px 0;font-family:monospace}
button{background:#00ff41;color:#000;padding:8px;border:none;width:100%;font-weight:bold;cursor:pointer}
.result{background:#060809;border:1px solid #00ff41;padding:12px;margin-top:12px;white-space:pre-wrap;font-size:0.78rem}
</style>
</head>
<body>
<h1>Python Automation Tool</h1>
<p style="text-align:center;color:#4a7a55">by Mohammed Ayaan</p>
<div class="card">
<h3>Select Task</h3>
<form method="POST">
<select name="task">
<option value="rename">Bulk File Rename</option>
<option value="password">Password Generator</option>
<option value="counter">Word Counter</option>
<option value="date">Date Calculator</option>
</select>
Input: <textarea name="input" rows="3" placeholder="Enter your input here"></textarea>
<button type="submit">Run Task</button>
</form>
</div>
{% if result %}
<div class="result">{{ result }}</div>
{% endif %}
</body></html>"""

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    if request.method == "POST":
        task = request.form.get("task","")
        inp = request.form.get("input","")
        
        if task == "password":
            import random, string
            chars = string.ascii_letters + string.digits + "!@#$"
            result = "Generated Passwords:\n"
            for i in range(5):
                result += ''.join(random.choices(chars, k=12)) + "\n"
        
        elif task == "counter":
            words = len(inp.split())
            chars = len(inp)
            lines = len(inp.splitlines())
            result = f"Words: {words}\nCharacters: {chars}\nLines: {lines}"
        
        elif task == "date":
            result = f"Current Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\nCurrent Time: {datetime.datetime.now().strftime('%H:%M:%S')}"
        
        elif task == "rename":
            files = inp.strip().splitlines()
            result = "Renamed files:\n"
            for i, f in enumerate(files):
                result += f"{f} → file_{i+1}.txt\n"
    
    from flask import render_template_string
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    print("[*] Automation Tool: http://127.0.0.1:5002")
    app.run(host="127.0.0.1", port=5002, debug=False)
