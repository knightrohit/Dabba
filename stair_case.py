--Triple set
def step_1(stairs):
	global count
	stairs -= 1
	if stairs == 0:
		count += 1
		return True
	if stairs > 0:
		work(stairs)
	else:
		return False

	
def step_2(stairs):
	global count
	stairs -=  2
	if stairs == 0:
		count += 1
		return True
	if stairs > 0:
		work(stairs)
	else:
		return False


def step_3(stairs):
	global count
	stairs -=  3
	if stairs == 0:
		count += 1
		return True
	if stairs > 0:
		work(stairs)
	else:
		return False
		
		
def work(stairs):
	step_1(stairs)
	step_2(stairs)
	step_3(stairs)