''' Module Emotion detector.
'''
# Import the json and requests library to handle HTTP requests
import json
import requests

# Function Emotion detector
def emotion_detector(text_to_analyze):
    ''' Define a function named emotion_detector that takes a string input (text_to_analyze)
    Arguments: text_to_analyze: Text to analyze
    '''
    # URL of the emotion detector service
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
    'watson.runtime.nlp.v1/NlpService/EmotionPredict')

    # Custom header for the API request specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = input_json, headers=header, timeout=5)

    # Check if response status code is 400 for blank entries
    if response.status_code == 400:
        # Return the same dictionary, but with values for all keys being None
        return ({"anger": None, "disgust": None, "fear": None, "joy": None, 
        "sadness": None, "dominant_emotion":None})

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting set of emotions, including anger, disgust, fear, joy and sadness, along with their scores
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Create dictionary with emotions and scores
    dict_emo = { 'anger' : anger_score, 'disgust' : disgust_score, \
        'fear' : fear_score, 'joy' : joy_score, \
        'sadness' : sadness_score}
    
    # Get name of the dominant emotion with the highest score
    highest_scorer = max(dict_emo, key=dict_emo.get)

    # Update dictionary with dominant_emotion 
    dict_emo.update({'dominant_emotion' : highest_scorer})
    
    # Returning a dictionary containing emotions, scores and dominant_emotion
    return dict_emo