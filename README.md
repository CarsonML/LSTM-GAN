# LSTM-GAN
The goal of this poject is to use a GAN to generate music (Work in Progress)

# The Data
I got my data from this reddit post:
https://www.reddit.com/r/WeAreTheMusicMakers/comments/3ajwe4/the_largest_midi_collection_on_the_internet/
It is in the form of many midi files, not all of which I ended up using

# Data Processing
First, I converted all the midi files to mxl using musescore batch convert. I did this because since midi files record performance, some of the notes are not the right length, and are instead cut short to make it more like how it would be performed. This was not what I wanted, and by converting to mxl, I was able to get the exact score. Then, I used music21 to sort the files. I only kept files that were written for a single instrument (the code to do this has since been misplaced), and I ended up with about 20,000 files, after removing very short files. Then, I turned the files into numpy arrays and pickled them, using the provided converter.py script. I then went and zipped all the pickle files using a bash loop, while running the conversion script(this is very important, unless you have 350+ gb of space sitting around, they take up alot of space)

# Data Format
After all the processing, the data was in a folder containing each song saved individualy as a zipped pickled list. Each list was made from, and therefore could be converted back to, a numpy array of shape (19,200 , 128). The 19,200 is what I set as the max limit. This was an estimation based of a 200 measure piece. It is so large because I split each quarter note into 24 pieces, so the data could store triplets and down to 32nd notes. The 128 is the number of possible midi pitches. A value in the array is 1 if that note is played at that time, otherwise 0. (although the one at the end of each note is changed to a 0 to differentiate between one long note and two ones of half the length.

# The GAN: Discriminator
The discriminator is made up of several convolutuional layers, a flattening layer, and a dense layer, then a softmax to output. All of the convolutional layers have fairly large strides. I did this because it makes the program not take up 300 + GB of ram, and I figured since the data was detailed enough to forgive the loss since it was 19,200 long.

# The GAN: Generator
The Generator is made up of an LSTM cell that takes in 19,200 random values and outputs 19,200 other values, then devides these by six. The goal is to get the values to range between 0 and 1, but still be able to output a 1, so relu6 was used, then divided by six (currently not sure if this actually works, I have only gotten past one epoch).

# Sampling and Saving
I take a sample and Save every 10 batches. The sample is converted to a midi file using music21. I also have tensorboard set up. The locations to which everything is saved are pretty evident in the code (and I don't remember them at the moment) so I will not list them here.

# Current Progress
I am currently in the process of running the code, and no music has yet been generated. At the first epoch, the network had not yet learned to produce 1's, so the process that reconstructed the music created an empty file

Made while working with Hello World Studio
