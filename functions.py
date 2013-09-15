#functions

#import settings_file
test = 0
def dstAdjust(date, dst_begin, dst_end): #needs to actually use the datetime module
	if date == dst_begin:
		date.time.hh -= 1
	elif date == dst_end:
		date.time.hh += 1
	return date.time.hh

def dataQuery(): #TODO() not finished in the slightest, don't even know what's going on
	query = raw_input('save data from test?: ')
	if query.lower[0] == "y":
		return subjectInput()
	else:
		print 'continuing without saving data'
		return runTest()
		
def subject_input(test): #TODO() make this returnable using incoming test number
	subjectData = {}
	sub_first = raw_input("Subject First Name: ")
	sub_last = raw_input("Subject Last Name: ")
	sub_birth = raw_input("Subject Birthdate: ")
	#test_number += 1
	#test = settings.test_number
	test += 1
	subjectData[test] = {	"first":sub_first,\
						"last":sub_last, \
						"birthdate": sub_birth,
						}
	return subjectData

def solution_query(): #TODO() this seems to be working out fine, finish others and come back to it
	values = []
	count = 1
	while count <= 5:
		sol = float(raw_input("Solution %s: " % (count)))
		values.append(sol)
		count += 1
	print values
	user_input = raw_input('are these values correct? (y/n): ')
	if user_input.lower() == 'n':
		solution_query()
	elif user_input.lower() == 'y':
		print('using %s as calibration solution values' % (values))
		return(values)
	else:
		exit
		
def runTest(): #TODO() not even started yet, for the actual breath reading
	print('test')
def calibration(): #TODO() for running a calibration, should return the calibraiton curve
	print("\nFive solutions are necessary to properly calibrate this instrument.\nFor best results, use values that will bracket the expected result")

def runPump(): #TODO() learn how to interface with motor and such, this will just turn the pump on and off

def sensorRead(): #TODO() learn how to read information from sensors, save to a temp file.
	
def calcValue(sensor): #TODO() calculate breath reading from sensor values

def mouthError(values): #TODO() probably shouldn't be a function, but whatever. make this break the test sequence and enter ready mode.
	if values.average[-5,0] < (max(values) - 0.005):
		return "Mouth Alcohol Detected, run test again" 
		cancelTest()
	
	
def testSequence():
	a = airblank()
	b = breathSample()
	c = calCheck()
	d = quickDiagnostic()
	sequence = raw_input("enter testing sequence (ex. a,b,a,c,a,d,a): ")
	return sequence
#TODO() this should be in that one __name__ is __main__ etc thing that I don't know how to do
subdict = {}
for i in range(3):
	subjectData = subject_input(i)
	for k in subjectData:
		subdict[k] = subjectData[k]
print subdict

print(subjectData[1]["last"] + ", " + subjectData[1]["first"] )
