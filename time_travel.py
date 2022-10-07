import json
import os

if not os.path.exists("timelines.json"):
	with open("timelines.json", 'w') as f:
		d = {"1": 1}
		json.dump(d, f)

def timeline_check():
	read = open("timelines.json", 'r')
	timelines = json.load(read)
	last_key = list(timelines)[-1]
	current_timeline = timelines[last_key]
	toFuture = int(input("Enter the timeline you want to go: "))
	print(f"Your previous timeline you visited: {current_timeline}")
	current_timeline += toFuture
	print(f"The timeline you are being taken now: {current_timeline}")
	timelines[(str(int(last_key)+1))] = toFuture
	read.close()
	append = open("timelines.json", 'a')
	append.seek(0); append.truncate()
	json.dump(timelines, append)

def main():
	print("\n\nDillusioners Time Machine\n\n")
	timeline_check()

main()