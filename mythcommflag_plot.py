#!/usr/bin/env python
import re
import numpy as np
import matplotlib.pyplot as plt

COMM_DELIM = re.compile(r'^framenum:\s+(?P<framenum>\d+)\s+marktype:\s+(?P<marktype>\d+)')
TOTAL_FRAMES = re.compile(r'^totalframecount:\s+(?P<totalframes>\d+)')


total_frames = 0
com_intervals = []

first = True
f = open('output.txt')
for line in f:
	m = COMM_DELIM.match(line)
	if m:
		d = m.groupdict()
		if first and d['marktype'] == '4':
			start = int(d['framenum'])
		elif not first:
			if d['marktype'] == '4':
				start = int(d['framenum'])
			elif d['marktype'] == '5':
				com_intervals.append((start, int(d['framenum'])))
		first = False
	else:
		m = TOTAL_FRAMES.match(line)
		if m:
			total_frames = int(m.groupdict()['totalframes'])

print(total_frames)
print(com_intervals)

all_data = np.zeros((1,total_frames), dtype=np.uint8)
for s,e in com_intervals:
	for i in range(s,e+1):
		all_data[0,i] = 1 

print(all_data)
print(np.sum(all_data))

plt.pcolor(all_data)
#plt.show()
plt.savefig('commercials.png')
