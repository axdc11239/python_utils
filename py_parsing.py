import sys

left_q = 0
content = ""
ready=False
start_write=False

file_name = sys.argv[1]
func_name = sys.argv[2]


with open(file_name) as f:
	for line in f:
		if (func_name in line) and (";" not in line):
			ready=True
		if "}" in line and ready:
			left_q-=1
			
		if ready and left_q > 0:
			start_write=True
			content+=line
		if "{" in line and ready:
			left_q+=1
		if start_write and left_q <=0:
			print(content)
			exit()
		

