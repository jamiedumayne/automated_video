# Creating videos with AI

I wanted to see if I could create text with AI, then create code to turn it into a video and upload it to social media. I was succesful in doing this. The code in this repo is able to take text, covert it to speech and add a background, then upload the video to YouTube. This [channel](https://www.youtube.com/@dailypawsitivity/) is one that I created using python scripts and AI.

# How it works
The code will generate a text prompt for that day, which then needs to be taken to ChatGPT (or any other text generation AI). The AI is asked to generate a blog post about why that animal is motivation. The output is saved as a text file in the scripts folder. Python then imports the text and converts it into an audio file, using Microsoft Azure's text-to-speech tool. I downloaded several stock footage backgrounds which are in a vertical format (in the backgrounds folder). The python script randomly selects one of these to use, adds the audio file and trims the video to match the length of the audio. Finally, the script creates a command to upload the video to YouTube from the terminal (the command needs to be run from the same file location as  upload.py). Additionally, the title and description are pulled in from a text file which will need to be filled from ChatGPT.


# Running the code
Download all the repository, then run the main.py file (the filepath will need to be set to wherever the files have been downloaded to). There are some pre-requisites required to run the code. Most notably an 0Auth 2.0 connection will need to be setup with the YouTube channel you wish to upload to.


# Improvements
- Use an API for text generation. The text is currently manually taken to and from ChatGPT. There is an API available however it costs to use this service. In the future I will find a way to fund this and then setup the API.
- Upload to other platforms, such as: Instagram and Tiktok.
- Use more interesting video backgrounds. I'd like to generate videos that are more relevant to the video topic. There are some stock video websites which have API access. I'd take the video's prompt and download a selection of relevant videos. Then use the python script to randomly choose which videos to includ and edit them together. A more advanced version would be to summarise each senetence in one or two words, then get videos that match that.
- Generate subtitles. It would be more interesting if the viewers had something to read whilst watching the video. To create subtitles I need a .srt file, which is a text file with timestamps. This could be generated using a speech-to-text tool.