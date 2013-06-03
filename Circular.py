# Circular buffer straight forward approach
from sys import stdin
import re
INTEGER_RE = "(\d+)" 

def process_input(f = stdin):
  int_regex = re.compile(INTEGER_RE) 
  line = f.readline()
  N = int( int_regex.findall(line)[0] )
  start = end = 0
  el_nbr = 0
  _buffer = [0] * N


  while True:
    line = f.readline()

    if line[0] == 'L':
      res = []
      if el_nbr == 0:
        print
        continue
      elif start < end:
        for i in xrange(start, end):
          res.append(_buffer[i])
      else: 
        for i in xrange(start, N):
          res.append(_buffer[i])
        for i in xrange(0, end):
          res.append(_buffer[i])

      print '\n'.join(res)

    elif line[0] == 'Q':

      break

    elif line[0] == 'A':
      n = int( int_regex.findall(line[2:])[0] )
      for i in xrange(n):
        val = f.readline().rstrip(' \t\n\r')

        _buffer[end] = val
        end += 1
        if end == N:
          end = 0
        if el_nbr == N:
          
          start = end
        else:
          el_nbr += 1

    elif line[0] == 'R':
      n = int( int_regex.findall(line[2:])[0] )
      el_nbr -= n

      if start < end:
        start += n
      else:
        start += n
        if start >= N:
          start -= N

process_input()

