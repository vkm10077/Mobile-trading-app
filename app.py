from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>📱 Mobile Trading App</h1>
    <p>Version 1.0</p>
    <p>Server is Running Successfully ✅</p>
    """

@app.route("/health")
def health():
    return {
        "status": "ok",
        "message": "Mobile Trading App Running"
    }

if __name__ == "__main__":
    app.run(debug=True)
