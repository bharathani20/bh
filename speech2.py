>>> with harvard as source:
...     audio = r.record(source, duration=4)
...
>>> r.recognize_google(audio)