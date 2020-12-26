import os
import re
import json
from nltk.tokenize import sent_tokenize

del_todo_pattern = [ \
'<nl> - # todo', \
'<nl> - # # todo', \
'<nl> - # # # todo', \
'<nl> - # # # # todo', \
'<nl> - # # # # # todo', \
'<nl> - " " " todo', \
"<nl> - ' ' ' todo", \
]

undel_todo_pattern = [ \
'<nl> # todo', \
'<nl> # # todo', \
'<nl> # # # todo', \
'<nl> # # # # todo', \
'<nl> # # # # # todo', \
'<nl> " " " todo', \
"<nl> ' ' ' todo", \
] 


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


