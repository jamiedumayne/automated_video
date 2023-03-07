def video_edit():
    #import sound
    os.chdir(file_path + "audio/")
    audio = AudioFileClip(audio_filename)
    aud_length = audio.duration #get audio length

    #import background
    os.chdir(file_path + "backgrounds/")
    background_file = random.choice(os.listdir(file_path + "backgrounds/"))
    clip1 = VideoFileClip(background_file).subclip(0,aud_length)

    #edit all clips together
    combined = concatenate_videoclips([clip1])
    #combined = CompositeVideoClip([clip1, subtitles.set_pos(('center','bottom'))])

    #save video
    os.chdir(file_path + "finished_vids/")
    combined.audio = CompositeAudioClip([audio])
    video_name = file + ".mp4"
    combined.write_videofile(video_name)

video_edit()