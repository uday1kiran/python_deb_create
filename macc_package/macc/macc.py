import subprocess
import argparse
import sys, time

class Macchanger:
 FAIL = '\033[91m'
 OKGREEN = '\033[92m'
 OKCYAN = '\033[96m'
 ORANGE = '\033[93m'
 BOLD = '\033[1m'

 def get_arguments(self):
  parser = argparse.ArgumentParser()
  parser.add_argument("-i","--interface",dest="interface",help="interface to change its MAC address")
  parser.add_argument("-m","--mac",dest="new_mac",help="New MAC address")
  options = parser.parse_args()
  if not options.interface:
    parser.error(self.FAIL+self.BOLD+"[-] Please specify an interface, use --help for more info")
  elif not options.new_mac:
    parser.error(self.FAIL+self.BOLD+"[-] Please specify a new mac address, use --help for more options")
  return options

 def change_mac(self,interface,new_mac):
   subprocess.call(["sudo","ifconfig",interface,"down"])
   subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
   subprocess.call(["sudo","ifconfig",interface,"up"])
   print(self.OKGREEN+"[+]"+self.OKCYAN+" Changing MAC address of interface "+self.ORANGE+interface+" to "+new_mac)
 def slowprint(self,s):
   for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0. / 100)
 def script_header(self):
   self.slowprint('''\033[1;31m \033[95m
CHANGE MAC ADDRESS\033[92m
   ''')


def main():
  mac_changer = Macchanger()
  options = mac_changer.get_arguments()
  mac_changer.script_header()
  mac_changer.change_mac(options.interface,options.new_mac)
  
if __name__ == "__main__":
  main()

