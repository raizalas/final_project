'''
A function to make a POST API call to the Watson NLP API
and returns the emotion detection value

'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Emotion detection of a given string to the Watson NLP API
    '''
    url = (
    'https://sn-watson-emotion.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=obj, headers=headers, timeout=10)
    json_response = json.loads(response.text)
    score_dict = {}
    if response.status_code == 200:
        emotion_scores = json_response['emotionPredictions'][0]['emotion']
        for emotion, score in emotion_scores.items():
            score_dict[emotion] = score
        dominant_emotion = max(score_dict, key=score_dict.get)
        score_dict['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        score_dict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            }
    return score_dict
