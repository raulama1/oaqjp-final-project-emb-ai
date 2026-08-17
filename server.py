''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the scores or emotion
        and the dominant emotion.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the scores from the response
    anger_score = response.get('anger')
    disgust_score = response.get('disgust')
    fear_score = response.get('fear')
    joy_score = response.get('joy')
    sadness_score = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')    

    #Validate if dominant_emotion is None for blank entries
    if dominant_emotion is None:
        # Return text invalid entries
        return "Invalid text! Please try again!."

    # Return a formatted string with the scores or emotion and the dominant emotion
    return (
        f"For the given statement, the system response is 'anger': {anger_score},"
        f"'disgust': {disgust_score},'fear': {fear_score}, 'joy': {joy_score},"
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}.'"
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)