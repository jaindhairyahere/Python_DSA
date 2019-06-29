import os

def disk_usage(path):
	total = os.path.getsize(path)

	if os.path.isdir(path):
		for subentry in os.listdir(path):
			total += disk_usage(os.path.join(path,subentry))

	return total

