import requests,os,sys,json,random,time
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
a = (R+'''
 mmmmm  mm   m'''+W+''' mmmmmm m    m'''+R+'''
   #    #"m  #'''+W+''' #      ##  ##'''+R+'''
   #    # #m #'''+W+''' #mmmmm # ## #'''+R+'''
   #    #  # #'''+W+''' #      # "" #'''+R+'''
 mm#mm  #   ##'''+W+''' #      #    #'''+G+'''V1''')

b = (R+'''
  mmmmmm   mmm   mm'''+W+'''  mmmmmmmm  mmm  mmm'''+R+'''
  ""##""   ###   ##'''+W+'''  ##""""""  ###  ###'''+R+'''
    ##     ##"#  ##'''+W+'''  ##        ########'''+R+'''
    ##     ## ## ##'''+W+'''  #######   ## ## ##'''+R+'''
    ##     ##  #m##'''+W+'''  ##        ## "" ##'''+R+'''
  mm##mm   ##   ###'''+W+'''  ##        ##    ##'''+R+'''
  """"""   ""   """'''+W+'''  ""        ""    ""'''+G+'''V1''')
c = (R+'''
    __|  \  |'''+W+''' ____|  \  |'''+R+'''
     |    \ |'''+W+''' |     |\/ |'''+R+'''
     |  |\  |'''+W+''' __|   |   |'''+R+'''
   ___|_| \_|'''+W+'''_|    _|  _|'''+G+'''V1''')
d = (R+'''
    _____   __'''+W+'''________  ___
   /  _/ | / /'''+W+''' ____/  |/  /'''+R+'''
   / //  |/ /'''+W+''' /_  / /|_/ /'''+R+'''
 _/ // /|  /'''+W+''' __/ / /  / /'''+R+'''
/___/_/ |_/'''+W+'''_/   /_/  /_/'''+G+'''V1''')

def diacak():
	acak = [a,b,c,d]
        m = "".join(random.sample(acak,1))
        os.system("clear")
        print m

def main():
	diacak()
	print
	print C+"  Author Bl4ck Dr460n"
	print
	no = raw_input("Input Phone Number (ex : 6289xxx )> ")
	b = requests.get('http://apilayer.net/api/validate?access_key=43fc2577cf1cdb2eb522583eaee6ae8f&number='+no+'&country_code=&format=1')
	js = json.loads(b.text)
	try:
		print Y+"Local Format > "+G+js['local_format']
		time.sleep(2)
	except KeyError:
		print Y+"Local Format > "+R+"Not Found"
		time.sleep(2)
	try:
		print Y+"Country Code > "+G+js['country_code']
		time.sleep(2)
	except KeyError:
		print Y+"Country Code > "+R+"Not Found"
		time.sleep(2)
	try:
		print Y+"Location > "+G+js['location']
	except KeyError:
		print Y+"Location > "+R+"Not Found"

if __name__ == '__main__':
	main()
