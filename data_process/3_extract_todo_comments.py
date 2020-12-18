import pickle

class structure_data(object):   
    
    def __init__(self):
        self.del_todo_dict = self.del_todo_structure()
        print(type(self.del_todo_dict), len(self.del_todo_dict))

        self.undel_todo_dict = self.undel_todo_structure()
        print(type(self.undel_todo_dict), len(self.undel_todo_dict))
        # pass

    def del_todo_structure(self):
        '''
        return del_todo_dict
        '''
        del_todo_dict = {} 
        with open('./todo_deleted.out', 'r') as fin:
            for line in fin:
                repo_file, current_commit, parent_commit, commit_msg, diff = line.strip().split('\t') 
                # split diff by '<nl>' 
                diff_split = diff.split('<nl>')
                code_changes = []
                todo_comments = []
                # all_comments = []

                for e in diff_split:
                    # if e.strip().startswith('+') or e.strip().startswith('-'):

                    # if '- #' in e.strip() or \
                    #    '- " " "' in e.strip() or \
                    #    "- ' ' '" in e.strip():
                    #     all_comments.append(e)
                        
                    if 'todo' in e.strip():
                        todo_comments.append(e)
                    else:    
                        code_changes.append(e)

                key = current_commit
                value = {}
                value['repo_file'] = repo_file
                value['current_commit'] = current_commit
                value['parent_commit'] = parent_commit
                value['commit_msg'] = commit_msg
                value['diff'] = diff
                value['code_changes'] = code_changes
                value['todo_comments'] = todo_comments
                # value['all_comments'] = all_comments
                del_todo_dict[key] = value

        return del_todo_dict
    
    def undel_todo_structure(self):
        undel_todo_dict = {}
        
        with open('./todo_undeleted.out', 'r') as fin:
            for line in fin:
                repo_file, current_commit, parent_commit, commit_msg, diff = line.strip().split('\t') 
                # split diff by '<nl>' 
                diff_split = diff.split('<nl>')
                code_changes = []
                todo_comments = []
                # all_comments = []

                for e in diff_split:
                    # if e.strip().startswith('+') or e.strip().startswith('-'):
                    # if '#' in e.strip() or \
                    #    '" " "' in e.strip() or \
                    #    "' ' '" in e.strip():
                    #     all_comments.append(e)
                        
                    if 'todo' in e.strip():
                        todo_comments.append(e)
                    else:    
                        code_changes.append(e)

                key = current_commit
                value = {}
                value['repo_file'] = repo_file
                value['current_commit'] = current_commit
                value['parent_commit'] = parent_commit
                value['commit_msg'] = commit_msg
                value['diff'] = diff
                value['code_changes'] = code_changes
                value['todo_comments'] = todo_comments
                # value['all_comments'] = all_comments
                undel_todo_dict[key] = value
                # print(undel_todo_dict)
                # break

        return undel_todo_dict

    def save(self):
        '''
        '''
        # save del_todo_dict 
        with open('./del_todo_dict.pkl', 'wb') as handler:
            pickle.dump(self.del_todo_dict, handler)

        # save undel_todo_dict
        with open('./undel_todo_dict.pkl', 'wb') as handler:
            pickle.dump(self.undel_todo_dict, handler)

def main():  

    sd = structure_data()   
    sd.save()
    pass

if __name__ == '__main__':
    main()

