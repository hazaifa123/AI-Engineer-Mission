file  = open("diary.txt",'w')
write = file.write("""Aaj ka din acha tha.
Maine Python seekhi.
Kal aur seekhunga.""")
file.close()
print(write)
