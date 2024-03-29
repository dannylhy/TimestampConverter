# Simple converter

import datetime
import getopt
import sys

def int_timestamp_to_string(int_timestamp):
  dt_timestamp = datetime.fromtimestamp(int_timestamp)
  return dt_timestamp.strftime()

def usage():
  print ('converter.py -i <int_timestamp> -s <str_timestamp>')
  
def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hi:s:", ["help","int_ts=","str_ts="])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  for o, a in opts:
    if o == "-t":
      if not isinstance(a, int):
        print("Invalid timestamp. ", a)
        sys.exit(2)
      print("Input timestamp :", a)
      print("Output string :", int_timestamp_to_string(a))
    elif o in ("-h", "--help"):
      usage()
      sys.exit(2)
    else:
      assert False, "unhandled option"

main(sys.argv[1:])
