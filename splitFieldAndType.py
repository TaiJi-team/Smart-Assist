s_file = './data/task_examp.txt'
f = open(s_file, 'r')
line = f.readline()

f_names = []
f_types = []
while line:
    ss = line.split()
    f_names.append(ss[0].replace('`', ''))
    f_types.append(ss[1])
                
    line = f.readline()

f.close()

list = s_file.split("/")
out_file='./output/' + list[len(list) - 1] 
# print('out_file: ' + out_file)

fo = open(out_file, "w")
for f_name in f_names:
    # print(f_name)
    fo.write(f_name + '\n')
fo.write("----------------------------- \n")
for f_type in f_types:
    # print(f_type)
    fo.write(f_type + '\n')

fo.close()