import os
import re
import json
from nltk.tokenize import sent_tokenize

'''
del_todo_pattern = [ \
'<nl> - / / todo', \
'<nl> - / * todo' ,\
]

undel_todo_pattern = [ \
'<nl> " " " todo', \
"<nl> ' ' ' todo", \
] 
'''

with open('./todo_diff.out', 'r') as fin, \
    open('./todo_deleted.out', 'w') as del_todo, \
    open('./todo_undeleted.out', 'w') as undel_todo:
    for line in fin:
        if len(line.split('todo')) > 2:
            continue
        # print(line.strip())
        repo_file, commit_now, commit_parent, \
        commit_msg_pro, commit_diff_pro = line.strip().split('\t')
        # print(commit_diff_pro)
        commit_diff_pro_splits = commit_diff_pro.split("<nl>") 
        for e in commit_diff_pro_splits:  
            e = e.strip()
            # print(e)
            if e.startswith('-') and "todo" in e:
                # print("founded:", e)
                del_todo.write(line)

            if not e.startswith('+'): 
                if not e.startswith('-'):
                    if "todo" in e:
                        undel_todo.write(line)


'''
with open('./todo_diff.out', 'r') as fin, \
    open('./todo_deleted.out', 'w') as del_todo, \
    open('./todo_undeleted.out', 'w') as undel_todo:
    for line in fin:
        if len(line.split('todo')) > 2:
            continue
        if any(pattern in line.strip() for pattern in del_todo_pattern): 
            del_todo.write(line)
        if any(pattern in line.strip() for pattern in undel_todo_pattern): 
            undel_todo.write(line) 
'''

