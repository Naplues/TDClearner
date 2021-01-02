def output_pro_file(src_path, index):
    '''
    '''
    src_lst = [] 
    with open(src_path, 'r') as src_file:
        for line in src_file:
            src_lst.append(line.strip())

    tgt_path = '.' + src_path.split('.')[1] + '_pro.out'
    with open(tgt_path, 'w') as tgt_file: 
        for i, e in enumerate(src_lst):
            if i in index: 
                tgt_file.write(e + '\n')

todo_comment_lst = []
todo_comment_reserved = {}
todo_comment_reserved_index = {}

# Filter out the same todo comments 
with open('./positive_samples/todo_comments.out', 'r') as td:
    for line in td:
        todo_comment_lst.append(line.strip()) 

for i, e in enumerate(todo_comment_lst):
    todo_comment_reserved_index[i] = 1  
    # if e not in todo_comment_reserved: 
    #     todo_comment_reserved[e] = 1 
    #     todo_comment_reserved_index[i] = 1  
    # else:
    #     continue

print("positive_samples:\n")
print(type(todo_comment_reserved), len(todo_comment_reserved))
print(type(todo_comment_reserved_index), len(todo_comment_reserved_index))

output_pro_file('./positive_samples/todo_comments.out', todo_comment_reserved_index)
output_pro_file('./positive_samples/code_change.out', todo_comment_reserved_index)
output_pro_file('./positive_samples/commit_msg.out', todo_comment_reserved_index)
output_pro_file('./positive_samples/commit_info.out', todo_comment_reserved_index)

#############################
#   negative samples        #
#############################

todo_comment_lst = []
todo_comment_reserved = {}
todo_comment_reserved_index = {}

# Filter out the same todo comments 
with open('./negative_samples/todo_comments.out', 'r') as td:
    for line in td:
        todo_comment_lst.append(line.strip()) 

for i, e in enumerate(todo_comment_lst):
    if e not in todo_comment_reserved: 
        todo_comment_reserved[e] = 1 
        todo_comment_reserved_index[i] = 1  
    else:
        continue

print("negative_samples:\n")
print(type(todo_comment_reserved), len(todo_comment_reserved))
print(type(todo_comment_reserved_index), len(todo_comment_reserved_index))

output_pro_file('./negative_samples/todo_comments.out', todo_comment_reserved_index)
output_pro_file('./negative_samples/code_change.out', todo_comment_reserved_index)
output_pro_file('./negative_samples/commit_msg.out', todo_comment_reserved_index)
output_pro_file('./negative_samples/commit_info.out', todo_comment_reserved_index)

