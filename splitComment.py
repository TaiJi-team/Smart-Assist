s_file = './data/execute_register.txt'
f = open(s_file, 'r', encoding='utf-8')
line = f.readline()

f_names = []
# f_types = []
f_comms = []
while line:
    ss = line.split()
    f_names.append(ss[0].lower())
    # f_types.append(ss[1])
    if ',--' in line:
        sc = line.split(',--')[1]
        if '，' in sc:
            f_comms.append(sc.split('，')[0])
        else:
            f_comms.append(sc)
                
    line = f.readline()

f.close()

list = s_file.split("/")
out_file='./output/' + list[len(list) - 1] 
# print('out_file: ' + out_file)

fo = open(out_file, "w", encoding='utf-8')
for f_name in f_names:
    # print(f_name)
    fo.write(f_name + '\n')
fo.write("----------------------------- \n")
# for f_type in f_types:
#     # print(f_type)
#     fo.write(f_type + '\n')

for f_comm in f_comms:
    # print(f_comm)
    fo.write(f_comm + '\n')

fo.close()