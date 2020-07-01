#coding=utf-8
#!/usr/bin/python
# prompt:
# 1. pravite key bigint， 用NOT NULL AUTO_INCREMENT;  
# 2. datetime/timestamp 去掉 'CHARACTER SET utf8mb4 DEFAULT NULL'; 
# 3. 去掉重复字段并提示
# 4. 空行跳过
# 5. 数据不规范，第一个主键字段信息缺失。主键（业务主键名	business_pk_name)   任务元数据编码	task_metadata_id	varchar(40)	非空		

s_file = './data/field_lines_1.txt'
t_file = './output/sql.txt'

def gensql_from_field_lines(s_file, t_file):
    with open(s_file, 'r', encoding='utf-8') as fr:
        line = fr.readline()
        tableName = ''
        tableComm = ''
        pkCol = ''
        sql_pk = ''
        sql_h = ''
        sql_col = ''
        emb = ' CHARACTER SET utf8mb4 NOT NULL COMMENT '
        while line:
            # print(line)
            if line.find('[') == 0 and line.find(')') > 0:
                tableName = extr_between('[', ']', line)
                tableComm = extr_between('(', ')', line)
            else:
                sp = line.split('\t')
                # print(sp)
                if line.find('主键') >= 0:
                    pkCol = sp[1]
                    emb = emb.replace('NOT', 'DEFAULT')
                    sql_pk = '\tPRIMARY KEY (`' + pkCol + '`)\n'
                sql_col += '\t`' + sp[1] + '` ' + sp[2] + ' ' + emb + '\'' + sp[0] + ' ' + sp[-1][:-1] + '\',\n'
            line = fr.readline()
        sql_h = 'DROP TABLE IF EXISTS `' + tableName + '`;\nCREATE TABLE `' + tableName + '` (\n'
        sql_tail = ') ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COMMENT \'' + tableComm + '\';\n'
        # print(sql_h + sql_col + sql_pk + sql_tail)
        fw.write(sql_h + sql_col + sql_pk + sql_tail)

def extr_between(fromReg, toReg, t):
    begin=t.find(fromReg)
    end=t.rfind(toReg)
    ss=t[begin+1:end]
    return ss

if __name__ == '__main__':
    with open(t_file, 'w+', encoding='utf-8') as fw:
        gensql_from_field_lines(s_file, t_file)
    print('process completly ...')