import string
from nltk.stem.porter import *

stemmer = PorterStemmer()

def read_test_data(fpath):
    '''
    '''
    test_data = []
    with open(fpath, 'r') as fin:
        for line in fin:
            code_change, \
            todo_comment, \
            commit_msg, \
            label, \
            repo_id, \
            current_commit, \
            parent_commit = line.strip().split('\t')   
            test_data.append( (code_change, todo_comment, commit_msg, label) )
            # break
    return test_data
    pass

def tokenize(code_change, todo_comment, commit_msg): 
    '''
    '''
    table = str.maketrans(dict.fromkeys(string.punctuation))
    code_change_clear = code_change.translate(table)  
    todo_comment_clear = todo_comment.translate(table)
    commit_msg_clear = commit_msg.translate(table)

    # tokenization  
    code_change_tokens = [w.lower() for w in code_change_clear.split()] 
    todo_comment_tokens = [w.lower() for w in todo_comment_clear.split()] 
    commit_msg_tokens = [w.lower() for w in commit_msg_clear.split()]

    # stemming  
    code_change_stem_tokens = [stemmer.stem(w) for w in code_change_tokens] 
    todo_comment_stem_tokens = [stemmer.stem(w) for w in todo_comment_tokens] 
    commit_msg_stem_tokens = [stemmer.stem(w) for w in commit_msg_tokens]
    
    return code_change_stem_tokens, todo_comment_stem_tokens, commit_msg_stem_tokens 


def intersection(candidate_1, candidate_2):
    '''
    '''
    return list( set(candidate_1) & set(candidate_2) ) 
    pass

test_data = read_test_data('./cc_todo_pairs.test')

with open('./cc_todo_overlap.result', 'w') as fout:
    for e in test_data:
        # print(e)
        code_change, todo_comment, commit_msg, label = e[0], e[1], e[2], e[3]

        code_change_tokens, \
        todo_comment_tokens, \
        commit_msg_tokens = tokenize(code_change, todo_comment, commit_msg) 
        
        r = intersection(code_change_tokens, todo_comment_tokens)
        if len(r) > 1:  
            predict_label = 1
        else:
            predict_label = 0

        fout.write(label + '\t' + str(predict_label) + '\n') 
        # print( intersection(code_change_tokens, todo_comment_tokens) )
        # print( intersection(code_change_tokens, commit_msg_tokens) )
        # break

with open('./msg_todo_overlap.result', 'w') as fout:
    for e in test_data:
        # print(e)
        code_change, todo_comment, commit_msg, label = e[0], e[1], e[2], e[3]

        code_change_tokens, \
        todo_comment_tokens, \
        commit_msg_tokens = tokenize(code_change, todo_comment, commit_msg) 
        
        r = intersection(commit_msg_tokens, todo_comment_tokens)
        if len(r) > 1:  
            predict_label = 1
        else:
            predict_label = 0

        fout.write(label + '\t' + str(predict_label) + '\n') 
 
with open('./cc_msg_todo_overlap.result', 'w') as fout:
    for e in test_data:
        # print(e)
        code_change, todo_comment, commit_msg, label = e[0], e[1], e[2], e[3]

        code_change_tokens, \
        todo_comment_tokens, \
        commit_msg_tokens = tokenize(code_change, todo_comment, commit_msg) 
        
        r1 = intersection(code_change_tokens, todo_comment_tokens)
        r2 = intersection(commit_msg_tokens, todo_comment_tokens)
        if len(r1) > 1 or len(r2) > 1:  
            predict_label = 1
        else:
            predict_label = 0

        fout.write(label + '\t' + str(predict_label) + '\n') 
 


