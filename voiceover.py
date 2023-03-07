#generate voiceover from text
#set save location and filename

def text_to_voice(text):
    save_loc = file_path+"/audio/"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    #setup adio settings and set filepath to save
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True,
                                                 filename=save_loc+audio_filename)

    #Choose voice and language
    speech_config.speech_synthesis_voice_name='en-GB-HollieNeural'
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

audio_filename = file + ".wav"
text_to_voice(file_text)