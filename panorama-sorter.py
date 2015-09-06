#!/usr/bin/python
import os

cwd = os.getcwd()
dirlist = os.listdir(cwd)
dirlist = [x for x in dirlist if x.startswith('ST')] # only keep those items beginning with ST

#pp.pprint(dirlist)

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

complete = False
index = 0

while not complete:
	# determine file name and number of the first STA_****
	if len(dirlist) > 0 and dirlist[index].startswith('STA'):
		print 'Set: ' + dirlist[index] # found a STA_**** file
		alphabet_index = 0 # beginning at letter A; only used in while loop below, starting with B
		number = dirlist[index][4:8]
		
		os.mkdir(cwd + '/STA_' + number) # create subfolder to move all files of the set into, named after the first file
		os.rename(cwd + '/' + dirlist[index], cwd + '/STA_' + number + '/' + dirlist[index]) # move file
		del dirlist[index] # remove from dirlist to avoid finding it again in the next loop
		
		# search for STB_**** and following:
		set_complete = False
		while (not set_complete) and (alphabet_index < 26):
			alphabet_index += 1 # next letter
			searchitem = 'ST' + alphabet[alphabet_index] + '_' + str(int(number) + alphabet_index).zfill(4) + '.JPG' # this is the next filename to search for
			if searchitem in dirlist:
				print '...  ' + searchitem # actually found the next filename in sequence!
				os.rename(cwd + '/' + searchitem, cwd + '/STA_' + number + '/' + searchitem) # move file
				dirlist.remove(searchitem) # file was moved, so remove it from dirlist
			else:
				set_complete = True # next filename in sequence was not found, so the set must be complete; leaving the while loop
		print 'Set complete!\n' # set must be complete on loop exit; either due to next filename not found or the last file being STZ_****
		index = 0 # start over at beginning of dirlist for next iteration
	else:
		if index < (len(dirlist)-1):
			index += 1 # last file item was not a STA_**** file, but there are more files left, so try the next one
		else:
			complete = True # no files left in dirlist, so the job is done (note: doesn't work if the first photos are missing, i.e. if a set begins with STB_**** or later, those files will be left unsorted
			print 'Sorting complete!'

