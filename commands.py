# import webbrowser
# from datetime import datetime
# from speech import speak
#
# # Optional: Wikipedia and WolframAlpha (install via pip)
# import wikipedia
# import wolframalpha
#
# # Replace with your own WolframAlpha App ID (free at: https://developer.wolframalpha.com)
# WOLFRAM_APP_ID = "EKWVHQ-7L7A7TGTE2"  # ← Replace this!
# client = wolframalpha.Client(WOLFRAM_APP_ID)
#
# def process_command(command):
#     """Processes user commands and executes appropriate actions."""
#     if "open google" in command:
#         speak("Opening Google")
#         webbrowser.open("https://www.google.com")
#
#     elif "who are you" in command or "your name" in command:
#         speak("I am Jarvis, your voice assistant.")
#
#     elif "exit" in command or "quit" in command:
#         speak("Goodbye Haadi!")
#         exit()
#
#     else:
#         response = ask_local_ai(command)
#         print(f"🔹 AI Response: {response}")
#         speak(response)
#
# def ask_local_ai(prompt):
#     """Attempts multiple ways to answer: keywords → WolframAlpha → Wikipedia."""
#     prompt = prompt.lower()
#
#     # Local hardcoded logic
#     if "time" in prompt:
#         return f"The time is {datetime.now().strftime('%I:%M %p')}."
#     elif "day" in prompt:
#         return f"Today is {datetime.now().strftime('%A')}."
#     elif "date" in prompt:
#         return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."
#
#     # Try WolframAlpha
#     try:
#         res = client.query(prompt)
#         answer = next(res.results).text
#         return answer
#     except Exception:
#         pass
#
#     # Try Wikipedia
#     try:
#         return wikipedia.summary(prompt, sentences=2)
#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"Please be more specific. Options: {e.options[:3]}"
#     except Exception:
#         return "Sorry, I couldn't find an answer."
#

#
# import webbrowser
# from datetime import datetime
# from speech import speak
#
# # Optional: Wikipedia and WolframAlpha
# import wikipedia
# import wolframalpha
#
# # Replace with your actual Wolfram Alpha App ID
# WOLFRAM_APP_ID = "EKWVHQ-7L7A7TGTE2"  # ← INSERT YOUR KEY HERE
# client = wolframalpha.Client(WOLFRAM_APP_ID)
#
# def process_command(command):
#     """Processes user commands and executes appropriate actions."""
#     if "open google" in command:
#         speak("Opening Google")
#         webbrowser.open("https://www.google.com")
#
#     elif "who are you" in command or "your name" in command:
#         speak("I am Jarvis, your voice assistant.")
#
#     elif "exit" in command or "quit" in command:
#         speak("Goodbye Haadi!")
#         exit()
#
#     else:
#         response = ask_local_ai(command)
#         print(f"🔹 AI Response: {response}")
#         speak(response)
#
# def ask_local_ai(prompt):
#     """Attempts keyword → WolframAlpha → Wikipedia (with fix)."""
#     prompt = prompt.lower()
#
#     # Local responses
#     if "time" in prompt:
#         return f"The time is {datetime.now().strftime('%I:%M %p')}."
#     elif "day" in prompt:
#         return f"Today is {datetime.now().strftime('%A')}."
#     elif "date" in prompt:
#         return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."
#
#     # WolframAlpha
#     try:
#         res = client.query(prompt)
#         answer = next(res.results).text
#         return answer
#     except Exception:
#         pass
#
#     # Wikipedia (with search to avoid bad match like Errol Musk)
#     try:
#         search_results = wikipedia.search(prompt)
#         if search_results:
#             summary = wikipedia.summary(search_results[0], sentences=2)
#             return summary
#         else:
#             return "Sorry, I couldn't find anything on Wikipedia."
#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"Please be more specific. Options: {e.options[:3]}"
#     except Exception:
#         return "Sorry, I couldn't find an answer."



import webbrowser
from datetime import datetime
from speech import speak

import wikipedia
import wolframalpha
# from duckduckgo_search import ddg
from duckduckgo_search import ddg


# 🔑 Insert your actual Wolfram Alpha App ID here
WOLFRAM_APP_ID = "EKWVHQ-7L7A7TGTE2"  # ← Replace this!
client = wolframalpha.Client(WOLFRAM_APP_ID)

def process_command(command):
    """Processes voice command and routes it."""
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "who are you" in command or "your name" in command:
        speak("I am Jarvis, your voice assistant.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye Haadi!")
        exit()

    else:
        response = ask_local_ai(command)
        print(f"🔹 AI Response: {response}")
        speak(response)

def ask_local_ai(prompt):
    """Answer using WolframAlpha → Wikipedia → DuckDuckGo"""
    prompt = prompt.lower()

    # Local simple questions
    if "time" in prompt:
        return f"The time is {datetime.now().strftime('%I:%M %p')}."
    elif "day" in prompt:
        return f"Today is {datetime.now().strftime('%A')}."
    elif "date" in prompt:
        return f"Today's date is {datetime.now().strftime('%B %d, %Y')}."

    # Try WolframAlpha
    try:
        res = client.query(prompt)
        answer = next(res.results).text
        return answer
    except Exception:
        pass

    # Try Wikipedia
    try:
        search_results = wikipedia.search(prompt)
        if search_results:
            summary = wikipedia.summary(search_results[0], sentences=2)
            return summary
    except Exception:
        pass

    # Try DuckDuckGo
    try:
        results = ddg(prompt, max_results=1)
        if results:
            result = results[0]
            if 'body' in result and result['body']:
                return result['body']
            elif 'snippet' in result:
                return result['snippet']
    except Exception:
        pass

    return "Sorry, I couldn’t find an answer."

