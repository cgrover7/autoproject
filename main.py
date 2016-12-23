#######################################
####
import os
import sys
sys.dont_write_bytecode = True
try:
	from Files.import_lib import *
except ImportError:
	print "No import file found"
	exit(-1)

def main():
	curr_dir=os.getcwd()
	os.system('chmod 0777 Files/setup.sh')
	os.system('sh Files/setup.sh')
	read_config()

if __name__=="__main__":
	main()