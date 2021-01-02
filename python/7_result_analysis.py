import pickle
import json

class Result_Analysis(object):
    
    def __init__(self):
        
        self.repos_info = self.load_repos_info() 
        self.test_result = self.load_result('./result/test_result/test_result.pkl') 
        print(type(self.test_result), len(self.test_result))

        self.true_positive = self.get_true_positive() 
        print("true positives:", type(self.true_positive), len(self.true_positive))
        self.true_negative = self.get_true_negative()
        print("true negatives:", type(self.true_negative), len(self.true_negative))

        self.false_positive = self.get_false_positive() 
        print("false positives:", type(self.false_positive), len(self.false_positive))
        self.false_negative = self.get_false_negative()
        print("false negatives:", type(self.false_negative), len(self.false_negative))

        assert len(self.test_result) == (len(self.true_positive) + \
                                         len(self.true_negative) + \
                                         len(self.false_positive) + \
                                         len(self.false_negative) )
        pass
    
    def load_repos_info(self): 
        with open('./python_repos_info.json', 'r') as json_f:
            py_repos_info = json.load(json_f)
        return py_repos_info

    def load_result(self, result_path): 
        '''
        test_result
        (
            code_change, \
            todo_comment, \
            commit_msg, \
            label, \
            pred_label, \
            neg_prob, \
            pos_prob
        )
        '''
        with open(result_path, 'rb') as handler:
            result = pickle.load(handler)
        return result 
    
    def get_true_positive(self): 
        '''
        '''
        true_positive = []
        for e in self.test_result:
            code_change = e[0]
            todo_comment = e[1]
            commit_msg = e[2]
            true_label = e[3]
            pred_label = e[4]
            neg_prob = e[5]
            pos_prob = e[6]

            if true_label == 1 and pred_label == 1:
                true_positive.append(e)
        return true_positive
    
    def get_true_negative(self):
        '''
        '''
        true_negative = []
        for e in self.test_result: 
            code_change = e[0]
            todo_comment = e[1]
            commit_msg = e[2]
            true_label = e[3]
            pred_label = e[4]
            neg_prob = e[5]
            pos_prob = e[6]

            if true_label == 0 and pred_label == 0:
                true_negative.append(e)
        return true_negative 

    def get_false_positive(self): 
        '''
        '''
        false_positive = []
        for e in self.test_result:
            code_change = e[0]
            todo_comment = e[1]
            commit_msg = e[2]
            true_label = e[3]
            pred_label = e[4]
            neg_prob = e[5]
            pos_prob = e[6]

            if true_label == 0 and pred_label == 1:
                false_positive.append(e)
        return false_positive

    def get_false_negative(self):
        '''
        '''
        false_negative = []
        for e in self.test_result: 
            code_change = e[0]
            todo_comment = e[1]
            commit_msg = e[2]
            true_label = e[3]
            pred_label = e[4]
            neg_prob = e[5]
            pos_prob = e[6]

            if true_label == 1 and pred_label == 0:
                false_negative.append(e)
        return false_negative 
    
    def output(self):
        '''
        '''
        with open('./result/false_positive.out', 'w') as fout: 
            for e in self.false_positive:  
                code_change = e[0]
                todo_comment = e[1]
                commit_msg = e[2]
                true_label = e[3]
                pred_label = e[4]
                neg_prob = e[5]
                pos_prob = e[6]

                # construct commit_url
                info = e[7]
                repo_file, \
                current_commit, \
                parent_commit = info[0], info[1], info[2]
                repo_id = repo_file.strip().rstrip('.json') 
                repo_url = self.repos_info[repo_id]['repo_clone_url']
                commit_url = repo_url.split('.git')[0] + '/commit/' + str(current_commit)

                fout.write( code_change + '\t' + \
                            todo_comment + '\t' + \
                            commit_msg + '\t' + \
                            str(true_label) + '\t' + \
                            str(pred_label) + '\t' + \
                            str(neg_prob) + '\t' + \
                            str(pos_prob) + '\t' + \
                            str(commit_url) )
                fout.write( '\n' ) 

        with open('./result/false_negative.out', 'w') as fout:
            for e in self.false_negative:  
                code_change = e[0]
                todo_comment = e[1]
                commit_msg = e[2]
                true_label = e[3]
                pred_label = e[4]
                neg_prob = e[5]
                pos_prob = e[6]

                # construct commit_url
                info = e[7]
                repo_file, \
                current_commit, \
                parent_commit = info[0], info[1], info[2]
                repo_id = repo_file.strip().rstrip('.json') 
                repo_url = self.repos_info[repo_id]['repo_clone_url']
                commit_url = repo_url.split('.git')[0] + '/commit/' + str(current_commit)


                fout.write( code_change + '\t' + \
                            todo_comment + '\t' + \
                            commit_msg + '\t' + \
                            str(true_label) + '\t' + \
                            str(pred_label) + '\t' + \
                            str(neg_prob) + '\t' + \
                            str(pos_prob) + '\t' + \
                            str(commit_url) )
                fout.write( '\n' )

def main():
    ra = Result_Analysis()
    ra.output()
    pass

if __name__ == '__main__':
    main()

