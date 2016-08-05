
import os, sys, subprocess, math

query = os.path.dirname(os.path.abspath(__file__))+'/UPLOAD_FOLDER/query'

subprocess.call('hmmsearch blue.hmm {} > blue.output'.format(query),shell=True)
subprocess.call('hmmsearch yellow.hmm {} > yellow.output'.format(query),shell=True)
subprocess.call('hmmsearch red.hmm {} > red.output'.format(query),shell=True)

samples = {}
expected_blue = float("4.08E-37")
with open ('blue.output', 'r') as f:
	blue_results =[]
	for line in f:
		if 'Description' in line:
			for line in f:
				if 'Domain annotation' not in line:
					blue_results.append(line)	
				elif 'Domain annotation' in line:
					break
	blue_results.pop(0)
	del blue_results[-2:]
	for i in blue_results:
		element = i.strip().split('  ')
		NAME= element[-1]
		samples[NAME] = []
		Evalue = float(element[0])
		bscore = math.log((Evalue / expected_blue),2)
		bscore = math.log10(Evalue)
		samples[NAME].append(bscore)

expected_red = float("3.71E-45")
with open ('red.output', 'r') as f2:
        red_results =[]
        for line in f2:
                if 'Description' in line:
                        for line in f2:
                                if 'Domain annotation' not in line:
                                        red_results.append(line)
                                elif 'Domain annotation' in line:
                                        break
        red_results.pop(0)
        del red_results[-2:]
        for i in red_results:
                element = i.strip().split('  ')
                NAME= element[-1]
                Evalue = float(element[0])
	        rscore = math.log((Evalue / expected_red),2)
		rscore = math.log10(Evalue)
		samples[NAME].append(rscore)

expected_yellow = float("2.69E-45")
with open ('yellow.output', 'r') as f3:
        yellow_results =[]
        for line in f3:
                if 'Description' in line:
                        for line in f3:
                                if 'Domain annotation' not in line:
                                        yellow_results.append(line)
                                elif 'Domain annotation' in line:
                                        break
        yellow_results.pop(0)
        del yellow_results[-2:]
        for i in yellow_results:
                element = i.strip().split('  ')
                NAME= element[-1]
                Evalue = float(element[0])
		yscore = math.log((Evalue / expected_yellow),2)
		yscore = math.log10(Evalue)
		samples[NAME].append(yscore)

for ID in samples:
	match =  min(samples[ID], key=float)
	pos= [i for i,x in enumerate(samples[ID]) if x == match]
	if pos == [0]:
		print ID, 'is most likely blue expressing'
		print 'blue score:',abs( samples[ID][0])
		print 'yellow score:', abs(samples[ID][2])
		print 'red score:', abs(samples[ID][1])
	elif pos == [1]:
		print ID, 'is most likely red expressing'
		print 'blue score:', abs(samples[ID][0])
                print 'yellow score:', abs(samples[ID][2])
                print 'red score:', abs(samples[ID][1])
	elif pos == [2]:
		print ID, 'is most likely yellow expressing'
		print 'blue score:', abs(samples[ID][0])
                print 'yellow score:', abs(samples[ID][2])
                print 'red score:', abs(samples[ID][1])

os.remove('blue.output')
os.remove('red.output')
os.remove('yellow.output')
os.remove(query)
