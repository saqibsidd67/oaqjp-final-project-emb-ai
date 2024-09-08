from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")

# defines function
def emotion_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    if anger_score is None or disgust_score is None or fear_score is None or joy_score is None or sadness_score is None:
        dominant_emotion = None
    else:
        score_dict = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}

        dominant_emotion = max(score_dict, key = score_dict.get)
    if dominant_emotion is None:

        return "Invalid text! Please try again!"
    # Return a formatted string with the sentiment label and score
    return (f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}.")

#next route to render index.html page
@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    