"""
Created by Luo Pan

It is for assignment 3. The program decodes RF Signals using post processing.
It identifies all of the preambles in a sample and print them all out.
"""

#!/usr/bin/env python

# Import python numerical processing libraries
from numpy import *
from scipy import *
from pylab import *

# Load in data in float32 format
data = fromfile("output.float32", float32)
print "Loaded %d samples"%(len(data))

# Converts the data to binary and stores to binary list
binary = []

# Binary used to identify button A
aList = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]

# Binary used to identify button B
bList = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]

# Binary used to identify button C
cList = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0]

# Binary used to identify button D
dList = [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]

# variable used to identify the boundary between 0 and 1
previous = 0

# Analysis shows the short pulse is about 416 long and the long pulse is about 1248 long
# reach500 is set to 1 if the counter reach 500. reach1000 is set to 1 if the counter reach 1000
# If the data > 0.5 and the counter is less than 500, append 1 to the binary list (short pulse)
# If the data > 0.5 and the counter is between 500 and 1000, append another 1 to the binary list.
# If the data > 0.5 and the counter is greater than 1000, append 1 to the binary list (long pulse)
# The similar approach is applied to data less than 0.5
reach500 = 0
reach1000 = 0
counter = 0

for d in data:
	if d > 0.5:
		if previous == 0:
			# reset variables
			counter = 0
			reach500 = 0
			reach1000 = 0
			binary.append(1)
			# now the previous number is 1
			previous = 1
		counter = counter + 1
		if counter > 500 and reach500 == 0:
			binary.append(1)
			reach500 = 1
		if counter > 1000 and reach1000 == 0:
			binary.append(1)
			reach1000 = 1
	else:
		if previous == 1:
			# reset variables
			counter = 0
			reach500 = 0
			reach1000 = 0
			binary.append(0)
			# now the previous number is 0
			previous = 0
		counter = counter + 1
		if counter > 500 and reach500 == 0:
			binary.append(0)
			reach500 = 1
		if counter > 1000 and reach1000 == 0:
			binary.append(0)
			reach1000 = 1
	#endif
#endloop

signalLength = len(binary)
compareListLen = len(aList)

for i in range(signalLength - compareListLen):
	if aList == binary[i:i+compareListLen]:
		print "Found preamble at binary list index " + str(i)
		print binary[i:i+compareListLen]
		print "[Button A]"
	elif bList == binary[i:i+compareListLen]:
		print "Found preamble at binary list index " + str(i)
		print binary[i:i+compareListLen]
		print "[Button B]"
	elif cList == binary[i:i+compareListLen]:
		print "Found preamble at binary list index " + str(i)
		print binary[i:i+compareListLen]
		print "[Button C]"
	elif dList == binary[i:i+compareListLen]:
		print "Found preamble at binary list index " + str(i)
		print binary[i:i+compareListLen]
		print "[Button D]"
#endloop
