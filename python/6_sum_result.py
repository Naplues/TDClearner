import pickle

def make_test_result_file():
    '''
    '''    
    test_result = []
    with open('./data/test_data/cc_todo_pairs.test', 'r') as test_data, \
        open('./data/test_data/test_prob.csv', 'r') as test_prob: 

        for data_line, result_line in zip(test_data, test_prob):
            data_line_split = data_line.strip().split('\t')
            code_change = data_line_split[0]
            todo_comment = data_line_split[1]
            commit_msg = data_line_split[2]
            label = data_line_split[3]
            info = data_line_split[4:]

            label = int(label)
            neg_prob, pos_prob = result_line.strip().split(',') 
            neg_prob = float(neg_prob) 
            pos_prob = float(pos_prob) 
            
            if neg_prob > pos_prob:
                pred_label = 0     
            else:
                pred_label = 1

            # print(neg_prob, pos_prob, label)
            test_result.append( (code_change, todo_comment, commit_msg, label, \
                                 pred_label, neg_prob, pos_prob, \
                                 info ) )
            # break
    return test_result
    pass
    
def make_train_result_file():
    '''
    '''    
    train_result = []
    with open('./data/train_data/cc_todo_pairs.train', 'r') as train_data, \
        open('./data/train_data/train_prob.csv', 'r') as train_prob: 

        for data_line, result_line in zip(train_data, train_prob):
            data_line_split = data_line.strip().split('\t')
            code_change = data_line_split[0]
            todo_comment = data_line_split[1]
            commit_msg = data_line_split[2]
            label = data_line_split[3]
            info = data_line_split[4:]

            label = int(label)
            
            neg_prob, pos_prob = result_line.strip().split(',') 
            neg_prob = float(neg_prob) 
            pos_prob = float(pos_prob) 
            
            if neg_prob > pos_prob:
                pred_label = 0     
            else:
                pred_label = 1

            # print(neg_prob, pos_prob, label)
            train_result.append( (code_change, todo_comment, commit_msg, label, \
                                  pred_label, neg_prob, pos_prob, \
                                  info ) )
            # break
    return train_result
    pass
 
test_result = make_test_result_file()
print("test_result:", type(test_result), len(test_result))
with open('./result/test_result/test_result.pkl', 'wb') as handler:
    pickle.dump(test_result, handler)   

train_result = make_train_result_file()
print("train_result:", type(train_result), len(train_result))
with open('./result/train_result/train_result.pkl', 'wb') as handler:
    pickle.dump(train_result, handler)


