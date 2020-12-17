import pickle
import random

class Data_Label(object):
    
    def __init__(self):
          
        self.positive_samples = self.load_positive_samples()    
        print(type(self.positive_samples), len(self.positive_samples))
        self.negative_samples = self.load_negative_samples()
        print(type(self.negative_samples), len(self.negative_samples))
        
        # 
        pass

    
    def load_positive_samples(self):
        '''
        '''
        positive_samples = [] 
        with open('./data/positive_samples/code_change.out', 'r') as cc, \
            open('./data/positive_samples/todo_comments.out', 'r') as todo: 
            for cc_line, todo_line in zip(cc, todo): 
                cc_line_clear = cc_line.strip()
                todo_line_clear = todo_line.strip().strip('-')
                positive_samples.append( (cc_line_clear, todo_line_clear) )

        return positive_samples
        pass

    def load_negative_samples(self):
        '''
        '''
        negative_samples = []
        with open('./data/negative_samples/code_change_pro.out', 'r') as cc, \
            open('./data/negative_samples/todo_comments_pro.out', 'r') as todo: 
            for cc_line, todo_line in zip(cc, todo): 
                cc_line_clear = cc_line.strip()
                todo_line_clear = todo_line.strip()
                negative_samples.append( (cc_line_clear, todo_line_clear) ) 

        # random sampling to the size of positive samples 
        # negative_samples = random.sample(negative_samples, len(self.positive_samples))
        return negative_samples

    def label(self):
        '''
        '''
        with open('./cc_todo_pairs', 'w') as fout:   
            for code_change, todo_comment in self.positive_samples: 
                fout.write( str(code_change) + '\t'  + str(todo_comment)  + '\t' + str(+1) ) 
                fout.write( '\n' )

            for code_change, todo_comment in self.negative_samples: 
                fout.write( str(code_change) + '\t' + str(todo_comment) + '\t' + str(0) )
                fout.write( '\n' )
        pass
    

def main():

    dl = Data_Label()
    dl.label()
    pass

if __name__ == '__main__':
    main()

