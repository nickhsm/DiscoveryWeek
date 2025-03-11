# Imports
from tflite_support.task import audio
from tflite_support.task import core
from tflite_support.task import processor
import re

model_path = "models/audio/soundclassifier_with_metadata.tflite"

def audio_process(audio_path):
    """
    Give a audio file (must be WAV) and it will give a dictionary back with name and score.
    """
    # Initialization
    base_options = core.BaseOptions(file_name=model_path)
    classification_options = processor.ClassificationOptions(max_results=2)
    options = audio.AudioClassifierOptions(base_options=base_options, classification_options=classification_options)
    classifier = audio.AudioClassifier.create_from_options(options)

# Alternatively, you can create an audio classifier in the following manner:
# classifier = audio.AudioClassifier.create_from_file(model_path)

# Run inference
    audio_file = audio.TensorAudio.create_from_wav_file(audio_path, classifier.required_input_buffer_size)
    audio_result = classifier.classify(audio_file)

    result_string = str(audio_result)
    print(result_string)

    regex_category = re.compile(r"Category\(.*?\)")
    list_of_owls = regex_category.findall(result_string)

    dictionary_of_results = dict()
    for owl in list_of_owls:
        # Name
        regex_name = re.compile(r"category_name='(.*)'")
        name = regex_name.search(owl).group(1)[2:]

        # Score
        regex_score = re.compile(r"score=(\d\.?\d*)")
        score = regex_score.search(owl).group(1)

        # Insert to dictionary
        dictionary_of_results[name] = score

    print(dictionary_of_results)
