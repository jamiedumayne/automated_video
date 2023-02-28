def video_edit():
    #import sound
    os.chdir("/home/jamie/Documents/Test/Tiktok_bot/audio/")
    audio = AudioFileClip(audio_filename)
    aud_length = audio.duration #get audio length

    #import background
    os.chdir("/home/jamie/Documents/Test/Tiktok_bot/backgrounds/")
    background_file = random.choice(os.listdir("C:/Users/jamie/OneDrive/Documents/Lancaster/Tiktok_bot/backgrounds/"))
    clip1 = VideoFileClip(background_file).subclip(0,aud_length) #takes from 18 - 23 seconds
    
    #add subtitles, file needs to be a srt file (not txt)
    #os.chdir("C:/Users/jamie/OneDrive/Documents/Lancaster/Tiktok_bot/scripts/")
    #generator = lambda txt: TextClip(txt, font='Arial', fontsize=16, color='white')
    #subtitles = SubtitlesClip(file), generator)

    #edit together
    combined = concatenate_videoclips([clip1])
    #combined = CompositeVideoClip([clip1, subtitles.set_pos(('center','bottom'))])

    #save video
    os.chdir("/home/jamie/Documents/Test/Tiktok_bot/finished_vids/")
    combined.audio = CompositeAudioClip([audio])
    video_name = "test_video2.mp4"
    combined.write_videofile(video_name)

video_edit()