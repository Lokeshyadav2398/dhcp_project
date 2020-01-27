fin = open("new_entry.txt",'r')
data = fin.read()
print(data)
fin.close()

fout = open("dhcpd.conf","a")
fout.write(data)