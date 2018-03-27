"""
Template code for your hiring algorithm

The structure of each application:
0: Intro to CS
1: Data Structures
2: Software Engineering
3: Algorithms
4: Computer Organization
5: Operating Systems
6: Overall College GPA

The list representing a single application would look like this:
[100, 95, 80, 89, 91, 75, 83]

"""

from allApps import lottaApps



exampleList = [[93, 89, 63, 88, 60, 73, 80], [100, 63, 57, 96, 58, 71, 78], [81, 91, 99, 78, 57, 87, 86], [81, 73, 100, 57, 91, 60, 66], [86, 89, 64, 81, 69, 93, 92], [78, 63, 88, 95, 59, 98, 90], [55, 74, 68, 55, 69, 94, 80], [64, 77, 75, 92, 77, 72, 83], [95, 58, 92, 62, 77, 64, 59], [94, 78, 84, 83, 68, 63, 76]]


def getBestApplicants(appList):
	""" Given applicant data, return the most qualified applications

		input:
		- appList: a 2D list containing lists of application data

		output:
		- a 2D list of the best applications
	"""
	finalists = list()

	for app in appList:
		finalists += [app]


	return finalists


# Change exampleList to lottaApps once you have it working
# This will change your data to the big dataset
finalists = getBestApplicants(exampleList)
print('')
print("-------------------------")
print("The finalists are...")
for finalist in finalists:
	print(finalist)
