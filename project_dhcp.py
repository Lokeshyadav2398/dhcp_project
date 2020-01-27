def get_data(fname):
	fd = open(fname,"r")
	data = fd.readlines()
	return data
	
def get_entry_position(data):
	start_pos = "host"
	end_pos = "}"
	list1 = []
	for i,line in enumerate(data):
		if line.startswith(start_pos):
			spos = i+1
		if line.startswith(end_pos):
			epos = i+1
			list1.append((spos,epos))
	print(list1)
	
def get_next_ip(data):
	sub4 = "fixed-address"
	for i,line in enumerate(data):
		if sub4 in line:
			f = line.split( )
			g = f[1].rstrip(";").split(".")
			h = int(g[3])+1
			h = str(h)
			i = g.pop(3)
			ip = ".".join(g)+"."+ h
			#print(ip)
	return ip
	
def generage_new_entry(sysname, macaddr, new_ip):
	new_entry = []
	new_entry.append("host"+" "+ (sysname)+" "+"{")
	new_entry.append((f"\t\thardware ethernet {macaddr};"))
	new_entry.append(f"\t\tfixed-address {new_ip};")
	new_entry.append(f"\t\toption routers 192.168.1.1;")
	new_entry.append("}")
	print(new_entry)
	wfd = open("new_entry.txt",'w')
	for data in new_entry:
		print(data)
		print("\n")
		wfd.write(data)
		wfd.write("\n")
	return
	
def main():
	fname = "dhcpd.conf"
	data = get_data(fname)		
	entry = get_entry_position(data)
	#last_entry = get_last_entry_data(entry)
	sysname = "Lokesh_laptop"
	macaddr = "A0:B5:D9:D6:E1:F2;"
	new_ip = get_next_ip(data)
	generage_new_entry(sysname,macaddr,new_ip)
if(__name__=="__main__"):
	main()