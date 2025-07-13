import speech_recognition as sr
# import pyaudio

class Applicant:
    def __init__(self):
        self.r = sr.Recognizer()
        self.talking = False
        self.mic_index = None
    
    def get_mic_index(self):
        return self.mic_index
    
    def is_recording(self):
        return self.talking

    def start_talking(self):
        self.talking = True

    def stop_talking(self):
        self.talking = False

    def record_speech(self, mic_index):
        if not self.talking:
            return None
        
        try:
            with sr.Microphone(device_index=mic_index) as mic:
                audio = self.r.listen(mic, timeout=5, phrase_time_limit=10)
                transcribed = self.r.recognize_vosk(audio)
                
                return transcribed

        except sr.WaitTimeoutError:
            raise

        except Exception as e:
            raise e

    def log_response(self, mic_index):
        try:
            while(self.is_recording()):
                text = self.record_speech(mic_index)
                # print(f"[DEBUG] Recorded text: {text}")

                if text is None:
                    continue

                if not self.is_recording():
                    break

                return text

        except Exception as e:
            raise

        # print("Wrote text")
        # response = self.record_speech(mic_index)
        # return response
