#coding=utf-8
#!/usr/bin/python

fd = {}
s_file = './data/index.json'
t_file = './data/ourProject.json'
out_file = './output/res_searchSS.txt'

for l in open(s_file, 'r', encoding='utf-8'):
    ar = l.split(' ')
    if len(ar) == 2:
        fd[ar[0]] = ar[1]
 
with open(out_file, 'w', encoding='utf-8') as fw:
    for l in open(t_file, 'r', encoding='utf-8'):
        ar = l.split(' ')
        if len(ar) == 2:
            if ar[0] in fd:
                fw.write(' '.join([ ar[0],fd[ar[0]].strip('\n'),ar[0],ar[1]]))
 
print('ok')