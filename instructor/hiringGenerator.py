

import random

def main():

	allApps = list()
	for num in range(5000): 
		app = list()
		for grade in range(7): 
			app.append(random.randint(55, 100))
		allApps.append(app)

	print(allApps)

main()