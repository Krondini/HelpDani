def parseFiles(req_filename, assign_filename, event_filename):
	req_fo = open(req_filename, 'r')
	event_fo = open(event_filename, 'r')
	assign_fo = open(assign_filename, 'a')

	req_header = req_fo.readline() #Store Request.csv header
	req_line = req_fo.readline()

	event_header = event_fo.readline() #Store Event.csv header
	event_line = event_fo.readline()

	assign_header = assign_fo.readline() #Store Assignment.csv header
	assign_line = assign_fo.readline()

	while req_line:

		req_line = req_line.strip().split(',')
		event_line = event_line.strip().split(',')
		assign_line = assign_line.strip().split(',')


		name = req_line[0] #Get kid's name
		sex = req_line[1] #Get kid's sex
		age = int(req_line[2]) #Get age value as int
		
		for i in range(3, 8):
			#First event
			if(req_line[i] == 'x') and (assign_line[2] == ""):
				assign_line[2] = req_header[i]
			#Second event
			elif(req_line[i] == 'x') and (assign_line[5] == ""):
				assign_line[5] = req_header[i]
			#Third event
			elif(req_line[i] == 'x') and (assign_line[8] == ""):
				assign_line[8] = req_header[i]
				


		req_line = req_fo.readline()

	return

def main():
	parseFiles("Request.csv", "Assignment.csv", "Event.csv")
	return

if __name__ == '__main__':
	main()