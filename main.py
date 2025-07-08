from speech import recognize_speech, speak
from commands import process_command
def main():
    speak("Hello Haadi, I am Jarvis, your assistant. How can I assist you? ")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
