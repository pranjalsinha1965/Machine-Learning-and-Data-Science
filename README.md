# Machine-Learning-and-Data-Science
Introduction to Data Science

## Dataset and its structure

1. We can use Urban Sound Classification ( https://urbansounddataset.weebly.com/ ) dataset which is quite popular.
2. Whichever dataset you are using, it is important to understand its structure and how to extract required features out of them.
3. For UrbanSound8K dataset, it can be downloaded using the following link ( https://goo.gl/8hY5ER  ). It downloads a compressed tar file of size around 6GB.
4. On extracting it, it contains two folders named 'audio' and 'metadata'.
5. Audio folder contains 10 folders with name fold1, fold2 and so on, each having approximately 800 audio files of 4s each.
6. Metadata folder contains a .csv file having various columns such as file_id, label, class_id corresponding to label, salience etc.
7. Complete description can be found here https://urbansounddataset.weebly.com/urbansound8k.html

## Research Paper and Resources to follow

1. https://github.com/meyda/meyda/wiki/audio-features
2. https://github.com/tyiannak/pyAudioAnalysis/wiki/3.-Feature-Extraction
3. https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a
4. https://towardsdatascience.com/urban-sound-classification-part-1-99137c6335f9
5. https://www.analyticsvidhya.com/blog/2017/08/audio-voice-processing-deep-learning/

## Library To Use

We can use librosa library which can be installed using 
> pip install librosa
>

## How to Load Audio Files and Extract Features

Using load method of librosa library, we can read audio files. It takes file path as input and returns an array having amplitude samples along with sampling rate of file.

Librosa library has many methods already build to extract features mentioned in resources which then returns another array of features.
We can use various combinations of those features. This is something you can play around and try how and which features like mfcc, spectral features, energy etc affect the classification of audio. 

For eg, in first stage you can extract only mfcc features and then build up a model and check the accuracy. Then try the same with other features. In order to further improve accuracy, you can also try to use more than one type of features and check the results.

## Using CNN to classify sound

This is a very classical way of sound classification as it is observed that similar type of sounds have similar spectrogram (read resource 3 to understand more about spectrogram). A spectrogram is a visual representation of the spectrum of frequencies of sound or other signal as they vary with time. And thus we can train a CNN network which takes these spectrogram images as input and using it tries to generalize patterns and hence classify them.

It uses ffmpeg as backend to convert and read some of the audio files. So to install ffmpeg, you can use 
> apt-get install ffmpeg

Librosa library can read audio files and convert them to there amplitude values for each sample of audio. Let us say there is an audio file of 4s and sampling rate of audio file is 22050 Hz. This means that audio file is made using amplitude samples such that 22050 samples of amplitudes are recorded in each second. Hence a 4s audio file with sampling rate 22050 can be expressed as an array of 4\*22050=88200 size 

# Introduction

1. Neural Machine Translation (NMT) is the task of using artificial neural network models for translation from one language to the other.
2. The NMT model generally consists of an encoder that encodes a source sentence into a fixed-length vector from which a decoder generates a translation.
3. This problem can be thought as a prediction problem, where given a sequence of words in source language as input, task is to predict the output sequence of words in target language.
4. The dataset comes from http://www.manythings.org/anki/, where you may find tab delimited bilingual sentence pairs in different files based on the source and target language of your choice.
5. For this project, you need to use French - English language pairs just to evaluate the projects uniformly for all students.

   #Step-1: Download and clean the data
1. Download the data as zip file and extract it to corresponding txt file. Read this txt file and prepare the list of pairs of language phrases.
2. Now, we will nedd to clean these pairs. For cleaning the text, some of the operations for cleaning are:


*   Remove the non printable charaters, if any
*   Remove punctuations and non-alphabetic charaters
* Convert to lowercase

#Step-2: Split and prepare the data for training the model
1. After cleaning the data, next you need to split the data in train and test.
2. Then, you need to create separate tokenizer for both source language and target language.
3. After creating the tokenizer, you need to encode and pad the input (source language) and output(target language) sequences w.r.t. their individual tokenizers and maximum sequence lengths.
4. Here, in this problem you will essentially be predicting the words in target language, therefore output seuences will need to be converted in one hot encoding.

#Step-3: Define and train the RNN based Encoder-Decoder model
1. First, you need to define the sequential model consisting mainly of two parts Encoder and Decoder 
2. In Encoder, the input sequence shall be passed through an Embedding layer (to train the word embeddings for source language) and then the output from the Embedding layer may be passed through one or more RNN/LSTM layers.
3. Now, to connect this Encoder to Decoder (yet to be defined), we can use RepeatVector layer. (This is because the shape of the output by Encoder is not same as expected shape of Input by Decoder)
4. Now, stack up the Decoder, wherein you may add one or more RNN/LSTM layers and finally the output TimeDistributed Dense layer to get output separately by timesteps.
5. Now, you have defined the model and now this can be trained on the training data, you prepared in last step. Here, you may play with the number of epochs, optimizer, batch size to get the optimum results.

#Step-4: Evaluating the model
Use BLEU score for evaluating your model using NLTK library
