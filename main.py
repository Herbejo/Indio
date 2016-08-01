import markdown2
import io
import re
import os

#returns a list of the tags and what line they are on
def getTags(path):
	output = []
	hand = open(path)
	i = 0
	for line in hand:
	    line = line.rstrip()
	    i = i + 1
	    if re.search('\[([^]]+)\]', line) :
	        output.append(line.replace('\t', '').replace(' ', ''))
	        output.append(i)
	return output

#takes path to md file and returns htlm string
def markdownToHtml(path):
	f = open(path, "r")
	data = f.read()
	f.close()
	converted = markdown2.markdown(data)
	return converted

#writes content into path at line 
def writeTag(path, line, content):
	r = open(path, "r") 
	contents = r.readlines()
	r.close
	contents.insert(line, content)
	del contents[line-1]
	w = open(path, "w")
	contents = "".join(contents) 
	w.write(contents)
	w.close()

#the real deal
def main():
	for file in os.listdir("."):
		if file.endswith(".html"):
			page = file
			tags = getTags(page)
			if len(tags) != 0:
				if os.path.isdir(tags[0]):
					for file in os.listdir(tags[0]):
						if file.endswith(".md"):
							content = markdownToHtml(tags[0] + "/" + file)
							writeTag(page, tags[1], content)

main()



