from utils import *
from Bert_MLP import Config

class Data_Encode(object):

    def __init__(self):

        print('Loading Dataset ...')    
        self.code_change_lst, \
        self.todo_comment_lst, \
        self.commit_msg_lst, \
        self.label_lst = self.load_data_lst()

        assert len(self.todo_comment_lst) == len(self.code_change_lst)
        assert len(self.todo_comment_lst) == len(self.label_lst)
        assert len(self.todo_comment_lst) == len(self.commit_msg_lst)
        print(type(self.code_change_lst), len(self.code_change_lst))
        print("Dataset Loaded!")

        print("Loading BERT Model...")
        self.bert_model, \
        self.tokenizer = self.load_BERT()
        print("BERT Loaded!")


        print("Bert Encoding...")
        self.encoded_code_change = self.bert_encode(self.code_change_lst)
        self.encoded_todo_comment = self.bert_encode(self.todo_comment_lst)
        self.encoded_commit_msg = self.bert_encode(self.commit_msg_lst)

        pass

    def load_data_lst(self):
        code_change_lst = []
        todo_comment_lst = []
        commit_msg_lst = []
        label_lst = []
        with open('./data/cc_todo_pairs', 'r') as fin:
            for line in fin:
                code_change, todo_comment, commit_msg, label = line.strip().split('\t')
                label = int(label)
                code_change_lst.append( code_change )
                todo_comment_lst.append( todo_comment )
                commit_msg_lst.append( commit_msg )
                label_lst.append( label )
        return code_change_lst, todo_comment_lst, commit_msg_lst, label_lst

    def load_BERT(self):
        '''
        '''
        ## Tokenize & Input Formatting
        ## Import model/tokenizer 
        ## Load the BERT model
        bert_model = BertModel.from_pretrained('./Model')
        bert_model.cuda()
        # print("Loading BERT Tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained('./Model')
        return bert_model, tokenizer
        pass
    
    def bert_encode(self, input_lst): 
        # bert encoding 
        encoded_input = self.tokenizer(input_lst, padding=True, truncation=True, max_length=128, return_tensors='pt')
        return encoded_input
        # input_ids = encoded_input['input_ids']
        # token_type_ids = encoded_input['token_type_ids']
        # attention_masks = encoded_input['attention_mask'] 

        # return input_ids, token_type _ids, attention_masks

    def save(self):
        '''
        save encoded dataset
        '''
        encoded_data = (self.encoded_code_change, self.encoded_todo_comment, self.encoded_commit_msg)
        
        labels = np.asarray(self.label_lst)

        with open('./data/encoded_data.pkl', 'wb') as handler:
            pickle.dump(encoded_data, handler)
       
        with open('./data/labels.pkl', 'wb') as handler:
            pickle.dump(labels, handler)
        # with open('./data/encoded_code_change.pkl', 'wb') as handler:
        #     pickle.dump(self.encoded_code_change, handler)

        # with open('./data/encoded_todo_comment.pkl', 'wb') as handler:
        #     pickle.dump(self.encoded_todo_comment, handler)
        
        # with open('./data/encoded_commit_msg.pkl', 'wb') as handler:
        #     pickle.dump(self.encoded_commit_msg, handler)



def main():
    
    dp = Data_Encode()
    dp.save()
    pass

if __name__ == '__main__':
    main()
