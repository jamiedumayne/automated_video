import pandas as pd
import numpy as np
import os
import sys
import azure.cognitiveservices.speech as speechsdk
import random
from transformers import pipeline

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

#list of animals
#https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54