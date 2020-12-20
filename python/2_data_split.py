from utils import *
from Bert_MLP import Config

class Data_Split(object):
    
    def __init__(self):

        self.config = Config()
        self.batch_size = self.config.batch_size 
        print("batch_size:", self.batch_size)

        self.encoded_data = self.load_encoded_data()
        self.encoded_code_change, \
        self.encoded_todo_comment, \
        self.encoded_commit_msg = self.encoded_data
        print(type(self.encoded_code_change), len(self.encoded_code_change))

        self.labels = self.load_labels()
        print(type(self.labels), len(self.labels))
         
        self.train_cc, self.test_cc = self.train_test_split(self.encoded_code_change)
        self.train_todo, self.test_todo = self.train_test_split(self.encoded_todo_comment)
        self.train_msg, self.test_msg = self.train_test_split(self.encoded_commit_msg)
        # print(self.train_cc[3] == self.train_todo[3])
        # print(self.train_cc[3] == self.train_msg[3])
        
        self.train_dataloader, self.test_dataloader = self.make_dataloader()
        pass
        
    def load_labels(self):
        '''
        '''
        with open('./data/labels.pkl', 'rb') as handler:
            labels = pickle.load(handler)
        return labels
    
    def load_encoded_data(self):
        with open('./data/encoded_data.pkl', 'rb') as handler:
            encoded_data= pickle.load(handler)
        return encoded_data

    def train_test_split(self, encoded_):
        # Training and Validation Split on qc0
        # Use 97% for training and 3% for validation
        
        input_ids, \
        token_type_ids, \
        attention_masks = encoded_['input_ids'], encoded_['token_type_ids'], encoded_['attention_mask']
        
        train_inputs, test_inputs, \
        train_masks, test_masks, \
        train_types, test_types, \
        train_labels, test_labels = train_test_split(input_ids, \
                                                     attention_masks, \
                                                     token_type_ids, \
                                                     self.labels, \
                                                     random_state=2018, \
                                                     test_size=0.1)
        
        # Convert to Pytorch Data Types
        train_inputs = torch.tensor(train_inputs)
        train_masks = torch.tensor(train_masks)
        train_types = torch.tensor(train_types)
        train_labels = torch.tensor(train_labels)
        
        test_inputs = torch.tensor(test_inputs)
        test_masks = torch.tensor(test_masks) 
        test_types = torch.tensor(test_types) 
        test_labels = torch.tensor(test_labels) 
        
        print("train_:", type(train_inputs), train_inputs.shape, train_masks.shape, train_types.shape, train_labels.shape)
        print("test_:", type(test_inputs), test_inputs.shape, test_masks.shape, test_types.shape, test_labels.shape)
        train_data = (train_inputs, train_masks, train_types, train_labels)
        test_data = (test_inputs, test_masks, test_types, test_labels)
        return train_data, test_data
    
    def make_dataloader(self):
        '''
        '''
        # make the train_dataloader 
        train_data = TensorDataset(self.train_cc[0], self.train_cc[1], self.train_cc[2],\
                                    self.train_todo[0], self.train_todo[1], self.train_todo[2], \
                                    self.train_cc[3])
        train_sampler = RandomSampler(train_data)
        train_dataloader = DataLoader(train_data, sampler=train_sampler, batch_size=self.batch_size)

        # make the test_dataloader 
        test_data = TensorDataset(self.test_cc[0], self.test_cc[1], self.test_cc[2],\
                                    self.test_todo[0], self.test_todo[1], self.test_todo[2], \
                                    self.test_cc[3])
        test_sampler = RandomSampler(test_data)
        test_dataloader = DataLoader(test_data, sampler=test_sampler, batch_size=self.batch_size)
        return train_dataloader, test_dataloader
    
    def save_dataloader(self):
        '''
        '''
        with open('./data/train_dataloader.pkl', 'wb') as handler:
            pickle.dump(self.train_dataloader, handler) 
        
        with open('./data/test_dataloader.pkl', 'wb') as handler:
            pickle.dump(self.test_dataloader, handler) 
        pass


def main():
    
    ds = Data_Split()
    ds.save_dataloader()
    pass

if __name__ == '__main__':
    main()


