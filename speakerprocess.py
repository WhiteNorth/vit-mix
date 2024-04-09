# AISHELL3 speaker rerank
import re

a1 = open('corpus/AISHELL3/train/spk-info.txt', 'r', encoding='utf-8')  # 读取说话人名单
a2 = open('corpus/AISHELL3/train/content-list.txt', 'r+', encoding='utf-8')  # 读取需要修改的list
a3 = open('corpus/AISHELL3/train/filelist.txt', 'w', encoding='utf-8')  # 读取需要修改的list
line_org = a1.readlines()[3:]  # 跳过前三行，读取说话人行
line_org_list = a2.readlines()
n_speaker = 142
for line1 in line_org:
    line1 = line1.split('\t')
    for line2 in line_org_list:
        line2 = line2.split('|')
        if line1[0][3:7] == line2[1]:
            line2[1] = re.sub(line1[0][3:7], str(n_speaker), line2[1])
            line2 = line2[0] + '|' + line2[1] + '|' + line2[2]
            a3.write(line2)
    n_speaker = n_speaker + 1

a1.close()
a2.close()
a3.close()
