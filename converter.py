from music21 import *
import os
import json
import numpy as np
import pickle
counter = 0
for piece in os.listdir('Real_Music'):
	#print(piece)
	notes = []
	try:
		#print(piece)
		s = converter.parse("/Users/carson/desktop/Real_Music/" + piece)
	#print(s)
		a = s.flat
		for item in a.notes:
			if isinstance(item, note.Note):
				notes.append([item.pitch.midi, item.quarterLength, item.offset])
			if isinstance(item, chord.Chord):
				for item2 in item.pitches:
					notes.append([item2.midi, item.quarterLength, item.offset])
		x = np.zeros((128,19200))
		for item in notes:
			for i in range(int(item[1] * 24)-2):
				x[int(item[0]),int(item[2]* 24 + i)] = 1
		filename = "/Users/carson/numpys/" + str(counter) + ".pickle"
		#print(x[:,0])
		with open(filename, 'wb+') as handle:
			pickle.dump(list(x), handle, protocol=pickle.HIGHEST_PROTOCOL)
			print("wrote" + piece + "to file")
			counter += 1

	except:
		print("oopsie")

