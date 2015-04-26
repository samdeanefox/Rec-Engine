from methods import *
import time

time_start = time.time()

print jsonConvert('subset.json')

time_end = time.time()
total_time = time_end - time_start
print '\nRuntime: ' + str(total_time)