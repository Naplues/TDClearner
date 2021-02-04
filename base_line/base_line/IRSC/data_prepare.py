with open('./data/train/cc_todo_pairs.train', 'r') as fin, \
    open('./data/train_doc_label', 'w') as fout:
    
    for line in fin:
        # print(line.strip())
        code_change, \
        todo_comment, \
        commit_msg, \
        label, \
        repo_file, \
        current_commit, \
        parent_commit = line.strip().split('\t')
        # print(code_change)
        # print(label)
        # prepross code_change, replace _ with " "
        code_change = code_change.replace("_", " ")

        doc = code_change + " " + todo_comment 
        label = label 
        fout.write(doc + '\t' + str(label) + '\n')
        # break
   
with open('./data/test/cc_todo_pairs.test', 'r') as fin, \
    open('./data/test_doc_label', 'w') as fout:
    
    for line in fin:
        # print(line.strip())
        code_change, \
        todo_comment, \
        commit_msg, \
        label, \
        repo_file, \
        current_commit, \
        parent_commit = line.strip().split('\t')
        # print(code_change)
        # print(label)
        # prepross code_change, replace _ with " "
        code_change = code_change.replace("_", " ")

        doc = code_change + " " + todo_comment 
        label = label 
        fout.write(doc + '\t' + str(label) + '\n')
 

