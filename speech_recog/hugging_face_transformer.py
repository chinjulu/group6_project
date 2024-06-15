import speech_recognition as sr
from transformers import pipeline

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("請說話...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="zh-TW")
        print("你說了: " + text)
        return text
    except sr.UnknownValueError:
        print("無法識別語音")
    except sr.RequestError as e:
        print("請求錯誤; {0}".format(e))
    return ""

def analyze_sentiment(text):
    # 使用Hugging Face的情感分析模型
    sentiment_pipeline = pipeline("sentiment-analysis", model="uer/roberta-base-finetuned-jd-binary-chinese")
    result = sentiment_pipeline(text)
    return result[0]['label']

if __name__ == "__main__":
    text = recognize_speech()
    if text:
        if "麥當勞" in text:
            print("偵測到麥當勞")
        if text == "去讀書":
            print("Sooo sad...")
        sentiment = analyze_sentiment(text)
        print("情感分析结果: " + sentiment)
