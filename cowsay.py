import sys
import os

def main():
	os.system("clear")
	line_nb = 4
	i = 1
	while i < len(sys.argv):
		line_nb = len(sys.argv[i]) + line_nb
		i += 1
	
	print("-" * line_nb)

	i = 1
	while i < len(sys.argv):
		print("\033[1;32;40m{}".format(sys.argv[i]), end =" ")
		i += 1
	print("\033[0;37;40m")
	print("-" * line_nb)

	print('''\r
             \\   ^__^
              \\  (♥♥)\\_______
                 (__)\\       )\\/\\
                     ||----w |        
                     ||     ||
		''')



if __name__== "__main__":
  main()
