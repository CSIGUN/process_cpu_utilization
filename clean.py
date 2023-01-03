#!/opt/homebrew/bin/python3

if __name__ == "__main__":

	inputfile = "log_"
	outputfile = "log_mod_"

	for i in range(0, 808):
		inputfile = inputfile+str(i)
		outputfile = outputfile+str(i)

		with open(inputfile, "rt") as fin:
			with open(outputfile, "wt") as fout:
				for line in fin:
					fout.write(line.replace('\\n', "\n"))
		
		inputfile = "log_"
		outputfile = "log_mod_"

	inputfile = "log_mod_"
	outputfile = "log_final_"

	for i in range(0, 808):
		inputfile = inputfile+str(i)
		outputfile = outputfile+str(i)

		with open(inputfile, "rt") as fin:
			with open(outputfile, "wt") as fout:
				for line in fin:
					fout.write(line.strip("'b"))
		
		inputfile = "log_mod_"
		outputfile = "log_final_"

