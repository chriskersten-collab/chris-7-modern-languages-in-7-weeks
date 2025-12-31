# compares all-expanded.m3u with OK3-v.m3u and outputs any lines from OK3-v.m3u
# that are not in all-expanded.m3u

# load all-expanded.m3u
all_expanded_lines = []
with open("all-expanded.m3u", "r") as f:
    first_exp_line = f.readline()
    #print(f"First line of all-expanded.m3u: {first_exp_line.strip()}")
#    while not EOFError:
    while True:
        extinf_line = f.readline()
        #print(f"Read extinf line: {extinf_line.strip()}")
        if not extinf_line:
            break
        path_line = f.readline()
        #print(f"Read path line: {path_line.strip()}")   
        if not path_line:
            break
        all_expanded_lines.append([extinf_line, path_line])
    

#print(f"Why is this not printing!? {len(all_expanded_lines)} lines loaded.")

#for display_line in all_expanded_lines:
#    print(display_line)

# load OK3-v.m3u
all_OK3_lines = []
with open("OK3-v.m3u", "r") as f:
    first_OK3_line = f.readline()
    #print(f"First line of OK3-v.m3u: {first_OK3_line.strip()}")

    while True:
        extinf_line = f.readline()
        #print(f"Read extinf line: {extinf_line.strip()}")
        if not extinf_line:
            break
        path_line = f.readline()
        #print(f"Read path line: {path_line.strip()}")   
        if not path_line:
            break
        all_OK3_lines.append([extinf_line, path_line])
    

#print(f"Why is this not printing!? {len(all_OK3_lines)} lines loaded.")

#print(all_OK3_lines[0][0])
#print(all_OK3_lines[1][0])

for OK3_line in all_OK3_lines:
    extinf_OK3 = OK3_line[0]
    #print(f"extinf_OK3: {extinf_OK3.strip()} ")
    # compare extinf_03 to somethingin all_expanded_lines
    for expanded_line in all_expanded_lines:
        extinf_expanded = expanded_line[0]
        #print(f"  xtinf_expanded: {extinf_expanded.strip()} ")
        if extinf_OK3 == extinf_expanded:
            #print(f"Found match for: {extinf_OK3.strip()}")
            all_OK3_lines.remove(OK3_line)
            break

#print(all_OK3_lines)
with open("dupes_found_OK3.m3u", "w") as f:
    f.write(first_OK3_line)
    for line in all_OK3_lines:
        f.write(line[0])
        f.write(line[1])