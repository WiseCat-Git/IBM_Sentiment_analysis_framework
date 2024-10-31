from flask import Flask, render_template, request, jsonify
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    # Render a basic HTML template with a form to accept text input
    return render_template("index.html")  # Ensure there's an index.html file in a 'templates' folder

@app.route("/analyze_emotion", methods=["GET"])
def analyze_emotion():
    # Get text from the query parameters
    text_to_analyze = request.args.get("textToAnalyze", default="", type=str)
    if not text_to_analyze:
        return jsonify({"error": "No text provided for analysis"}), 400

    try:
        # Run the emotion detection function
        result = emotion_detector(text_to_analyze)

        # If there's an error in the API response, handle it
        if result is None or "error" in result:
            return jsonify({"error": result.get("error", "Failed to analyze emotions")}), 500

        # If no emotion label is detected, treat it as an invalid input
        if not result.get("label"):
            return jsonify({"error": "Unable to detect emotion in the provided text."}), 400

        # Return the detected emotions as a JSON response
        return jsonify(result)  # result is expected to contain 'label' and 'score'

    except Exception as e:
        # Log the exact error and return a generic error message
        print(f"Error in emotion detection: {e}")
        return jsonify({"error": "Internal server error occurred"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

