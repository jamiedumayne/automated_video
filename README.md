# Creating videos with AI

I wanted to see if I could create text with AI, then create code to turn it into a video and upload it to social media. I was succesful in doing this. The code in this repo is able to take text, covert it to speech and add a background, then upload the video to YouTube. This [channel](https://www.youtube.com/@dailypawsitivity/) is one that I created using python scripts and AI.

# How it works
The code will generate a text prompt for that day, which then needs to be taken to Chat-GPT (or any other text generation AI). The AI is asked to generate a blog post about why that animal is motivation. The output is saved as a text file in the scripts folder. Python then imports the text and converts it into an audio file, using Microsoft Azure's text-to-speech tool. I downloaded several stock footage backgrounds which are in a vertical format (in the backgrounds folder). The python script randomly selects one of these to use, adds the audio file and trims the video to match the length of the audio. Finally, the script creates a command to upload the video to YouTube from the terminal (the command needs to be run from the same file location as ).


# Running the code
Download all the repository, then run the main.py file (the filepath will need to be set to wherever the files have been downloaded to). There are some pre-requisites required to run the code. Most notably an 0Auth 2.0 connection will need to be setup with the YouTube channel you wish to upload to.


# Improvements

The text is created using an ChatGPT and at the moment is manually created. But the plan is to find a similar AI that has an API which can be called in Python.