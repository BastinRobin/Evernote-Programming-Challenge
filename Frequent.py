from sys import stdin
def process(f = stdin):
  line = f.readline().rstrip(' \t\n\r')
  N  = int( line )

  unique = {}

  for i in xrange(N):
    term = f.readline().rstrip(' \t\n\r')
    if term in unique:
      unique[term] += 1
    else:
      unique[term] = 1

  line = f.readline().rstrip(' \t\n\r')
  k = int( line )

  heap = [(0, '')] * k
  heap_size = 0

  for count in unique.values():

    if heap_size == k:
        if count < heap[0]:
            continue
        pos = 0
        child_pos = 2 * pos + 1   
        while child_pos < heap_size:
            right_pos = child_pos + 1
            if right_pos < heap_size and heap[child_pos] > heap[right_pos]:
                child_pos = right_pos
            if heap[child_pos] >= count:
                break
            heap[pos] = heap[child_pos]
            pos = child_pos
            child_pos = 2*pos + 1
        heap[pos] = count
    else:

        heap[heap_size] = count
        pos = heap_size
        heap_size += 1
        while pos > 0:
            parent_pos = (pos - 1) >> 1
            parent = heap[parent_pos]
            if count < parent:
                heap[pos] = parent
                pos = parent_pos
            else:
                break
        heap[pos] = count

  results = sorted([(1./count, term) for (term, count) in unique.items() if count >= heap[0]])[:k]
  for (count, term) in results:
    print term

process()

