# Simple converter

import datetime
import sys

def int_timestamp_to_string(int_timestamp):
  dt_timestamp = datetime.fromtimestamp(int_timestamp)
  return dt_timestamp.strftime()

def main():
  print("Input Timestamp: ", sis.argv[0])

main()
