import requests
import json

def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        return None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = obj, headers=header)
    formatted_response = json.loads(response.text)
    e = formatted_response['emotionPredictions'][0]['emotion']
    highest_score = -1
    highest_emo = 'Null'
    for k in e:
        if e[k]>highest_score:
            highest_emo = k
            highest_score = e[k]
    e['dominant_emotion']=highest_emo
    return e


