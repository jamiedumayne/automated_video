import pandas as pd
import numpy as np
import os
import sys
import azure.cognitiveservices.speech as speechsdk
import random
from transformers import pipeline

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip