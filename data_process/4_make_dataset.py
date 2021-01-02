import pickle

class Dataset(object):
        
    def __init__(self):
         
        self.del_todo_lst = self.load_lst('./del_todo.pkl')
        print("del_todo_lst:", type(self.del_todo_lst), len(self.del_todo_lst))
        
        self.undel_todo_lst = self.load_lst('./undel_todo.pkl')
        print("undel_todo_lst:", type(self.undel_todo_lst), len(self.undel_todo_lst))
        
        # pair del_todo-code_change as positive samples 
        self.pos_cc_todo_pairs = self.get_cc_todo_pairs(self.del_todo_lst)
        print("positive samples:", type(self.pos_cc_todo_pairs), len(self.pos_cc_todo_pairs))

        # pair undel_todo-code_change as negative samples
        self.neg_cc_todo_pairs = self.get_cc_todo_pairs(self.undel_todo_lst) 
        print("negative sampels:", type(self.neg_cc_todo_pairs), len(self.neg_cc_todo_pairs))
        pass
    
    def load_lst(self, fpath): 
        '''
        (
         repo_file, 
         current_commit, 
         parent_commit,
         commit_msg,
         code_changes, 
         todo_comments
        )
        '''
        with open(fpath, 'rb') as handler:
            todo_lst = pickle.load(handler)
        return todo_lst
    
    def get_cc_todo_pairs(self, load_lst):
        '''
        code_change, todo pair
        '''
        cc_todo_pairs = [] 
        
        # for k, v in load_dict.items():
        for e in load_lst:
            repo_file = e[0] 
            current_commit = e[1] 
            parent_commit = e[2] 
            commit_msg = e[3] 
            code_change = e[4] 
            todo_comments = e[5] 

            # list to string
            code_change = "<nl>".join(code_change)
            # print("code_change:", code_change)
            # list to string  
            todo_comments = " ".join(todo_comments)
            # print("todo_comments:", todo_comments)
            todo_comments = todo_comments.strip().lstrip('-')

            if len(set(code_change.split())) < 5:  
                continue 
            if len(set(todo_comments.split())) < 5:
                continue
            # make sure it is a Python comment  
            if '#' in todo_comments or \
                '"""' in todo_comments or \
                "'''" in todo_comments:
                cc_todo_pairs.append( (code_change, todo_comments, commit_msg, \
                                        repo_file, current_commit, parent_commit) ) 
            # print(todo_comments)
            # print(code_change)
        
        return cc_todo_pairs
        # pass 
    
    def output(self):
        '''
        '''
        # with open('./summary', 'w') as summ:
        #     for k, v in self.todo_deleted_dict.items():
        #         summ.write(str(v['current_commit']) + '\t' + \
        #                    str(v['commit_msg']) + '\t' + \
        #                    str(v['diff']) + '\n') 

        with open('./positive_samples/code_change.out', 'w') as cc, \
            open('./positive_samples/todo_comments.out', 'w') as todo, \
            open('./positive_samples/commit_msg.out', 'w') as msg, \
            open('./positive_samples/commit_info.out', 'w') as info:
            for code_change, todo_comment, commit_msg, \
                repo_file, current_commit, parent_commit in self.pos_cc_todo_pairs: 
                # code_change = "<nl>".join(code_change)
                cc.write(code_change + "\n")
                # todo_comment = " ".join(todo_comment)
                todo.write(todo_comment + "\n")
                msg.write(commit_msg + "\n")
                info.write(repo_file + '\t' + current_commit + '\t' + parent_commit + '\n')

        with open('./negative_samples/code_change.out', 'w') as cc, \
            open('./negative_samples/todo_comments.out', 'w') as todo, \
            open('./negative_samples/commit_msg.out', 'w') as msg, \
            open('./negative_samples/commit_info.out', 'w') as info:
            for code_change, todo_comment, commit_msg, \
                repo_file, current_commit, parent_commit in self.neg_cc_todo_pairs: 
                cc.write(code_change + '\n')
                todo.write(todo_comment + '\n')
                msg.write(commit_msg + "\n")
                info.write(repo_file + '\t' + current_commit + '\t' + parent_commit + '\n')

def main():  
    '''
    '''
    dataset = Dataset()
    dataset.output()
    pass

if __name__ == '__main__':
    main()

