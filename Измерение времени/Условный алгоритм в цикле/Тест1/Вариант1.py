import time

start_time = time.time()

for i in range(1,10000):
	if i % 10 ==1:
		print(i,"ворона")
	if i %10 in (5,6,7,8,9):
		print(i,"ворон")
	if i % 10 in (2,3,4):
		print(i, "вороны")
print(time.time()-start_time,"sec")
#результат 0.04346418380737305 sec
