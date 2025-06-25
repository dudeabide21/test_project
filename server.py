from flask import Flask, request, send_from_directory, render_template_string
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Upload endpoint
@app.route("/upload", methods=["POST"])
def upload_image():
    if request.data:
        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, "wb") as f:
            f.write(request.data)
        return "Image received", 200
    return "No data", 400


# Route to serve uploaded images
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# Dashboard page
@app.route("/")
def dashboard():
    files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)
    html = """
    <html>
    <head>
        <title>Chicken Farm Feed</title>
        <meta http-equiv="refresh" content="5"> <!-- auto-refresh every 5 seconds -->
        <style>
            body { font-family: Arial; background: #f4f4f4; padding: 20px; }
            h1 { text-align: center; }
            .gallery { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
            .gallery img { border: 2px solid #ddd; border-radius: 8px; width: 240px; }
        </style>
    </head>
    <body>
        <h1>🐔 Chicken Farm Live Feed</h1>
        <div class="gallery">
        {% for file in files %}
            <img src="/uploads/{{ file }}" alt="{{ file }}">
        {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, files=files)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
