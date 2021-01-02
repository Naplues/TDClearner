import pickle
import random

class Data_Label(object):
    
    def __init__(self):
          
        self.positive_samples = self.load_positive_samples()    
        print(type(self.positive_samples), len(self.positive_samples))
        self.negative_samples = self.load_negative_samples()
        print(type(self.negative_samples), len(self.negative_samples))
        pass

    
    def load_positive_samples(self):
        '''
        '''
        positive_samples = [] 
        with open('./data/positive_samples/code_change_pro.out', 'r') as cc, \
            open('./data/positive_samples/todo_comments_pro.out', 'r') as todo, \
            open('./data/positive_samples/commit_msg_pro.out', 'r') as msg, \
            open('data/positive_samples/commit_info_pro.out', 'r') as info:
            for cc_line, todo_line, msg_line, info_line in zip(cc, todo, msg, info): 
                cc_line_clear = cc_line.strip()
                todo_line_clear = todo_line.strip().strip('-')
                msg_line_clear = msg_line.strip()  
                info_line_clear = info_line.strip() 
                positive_samples.append( (cc_line_clear, \
                                          todo_line_clear, \
                                          msg_line_clear, \
                                          info_line_clear) )

        return positive_samples

    def load_negative_samples(self):
        '''
        '''
        negative_samples = []
        with open('./data/negative_samples/code_change_pro.out', 'r') as cc, \
            open('./data/negative_samples/todo_comments_pro.out', 'r') as todo, \
            open('./data/negative_samples/commit_msg_pro.out', 'r') as msg,\
            open('./data/negative_samples/commit_info_pro.out', 'r') as info:
            for cc_line, todo_line, msg_line, info_line in zip(cc, todo, msg, info): 
                cc_line_clear = cc_line.strip()
                todo_line_clear = todo_line.strip()
                msg_line_clear = msg_line.strip()
                info_line_clear = info_line.strip()
                negative_samples.append( (cc_line_clear, \
                                          todo_line_clear, \
                                          msg_line_clear, \
                                          info_line_clear) ) 
        return negative_samples

    def label(self):
        '''
        '''
        with open('./data/cc_todo_pairs', 'w') as fout:   
            for code_change, todo_comment, commit_msg, commit_info in self.positive_samples: 
                fout.write( str(code_change) + '\t'  + \
                            str(todo_comment)  + '\t' + \
                            str(commit_msg) + '\t' + \
                            str(+1) + '\t' + \
                            str(commit_info) ) 
                fout.write( '\n' )

            for code_change, todo_comment, commit_msg, commit_info in self.negative_samples: 
                fout.write( str(code_change) + '\t' + \
                            str(todo_comment) + '\t' + \
                            str(commit_msg) + '\t' + \
                            str(0) + '\t' + \
                            str(commit_info) )
                fout.write( '\n' )
        pass
    

def main():
    
    dl = Data_Label()
    dl.label()
    pass

if __name__ == '__main__':
    main()
