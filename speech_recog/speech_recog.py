import speech_recognition as sr

def recognize_speech():
    # 创建一个Recognizer对象
    recognizer = sr.Recognizer()

    # 使用麦克风作为音频源
    with sr.Microphone() as source:
        print("請說話...")
        
        # 调整麦克风噪音水平
        recognizer.adjust_for_ambient_noise(source)
        
        # 捕获音频
        audio = recognizer.listen(source)

    try:
        # 使用Google Web Speech API进行语音识别
        text = recognizer.recognize_google(audio, language="zh-TW")
        print("你說了: " + text)
        return text
    except sr.UnknownValueError:
        print("無法識別語音")
    except sr.RequestError as e:
        print("請求錯誤; {0}".format(e))
    return ""

if __name__ == "__main__":
    recognize_speech()
