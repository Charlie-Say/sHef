#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

"""
This program will take in user voice and translate into text. *DONE*



------------ Pseudocode -------------

- download libraries
- documents?
- import libraries
- identify microphone
- activate input devices
- decide API tool to use for voice recognition

- need to make conditional statements depending on the speech recognition input

def questions():

    if (output == "what pairs well" || output == "what goes with" || output == ANY OTHER COMBINATION):
        iterate through sentence and find key words

    if (output == "season"):
        run through foodprint.org scraper




NOTES:
- we are using two different sites, so when we identify sentences from voice recognition, it needs
to call the correct function for the correct Selenium program and scraping function/module



"""

import speech_recognition as sr



def speech_to_text():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`

        audio_recording = r.recognize_google(audio)

        # make every word into list item
        split_audio_list = audio_recording.split()


        #
        print(split_audio_list)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


speech_to_text()



# translator function
def translator(x):

    #if condition for "does ___ go with ____?"

    #if condition for pairings "What is good with ____?"

    #if condition for season "What's in season?"

    return x