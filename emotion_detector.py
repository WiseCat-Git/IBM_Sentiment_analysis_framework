import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Check if request was successful
        
        # Parse JSON response
        result = response.json()
        
        # Extract the primary emotion and its score
        emotions = result["emotionPredictions"][0]["emotion"]
        primary_emotion = max(emotions, key=emotions.get)
        primary_score = emotions[primary_emotion]
        
        # Return the primary emotion and score in a structured response
        return {"label": primary_emotion, "score": primary_score}

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {"error": "Failed to analyze emotions"}



