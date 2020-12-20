from utils import *

class Config(object):

    def __init__(self): 
        self.model_name = 'bert'
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  
        self.num_classes = 2
        self.bert_path = './Model'
        self.hidden_size = 768
        self.tokenizer = BertTokenizer.from_pretrained(self.bert_path)
        self.batch_size = 16
        self.num_epochs = 10 


class Model(nn.Module):
    
    def __init__(self, config):
        super(Model, self).__init__()
        self.bert = BertModel.from_pretrained(config.bert_path)
        for param in self.bert.parameters():
            param.requires_grad = True 
        self.fc0 = nn.Linear(config.hidden_size, 512)
        self.fc1 = nn.Linear(512, 128)
        self.fc2 = nn.Linear(128, config.num_classes)

    # def forward(self, input_ids, attention_mask, token_type_ids):
    def forward(self, cc_todo_pair):
        
        input_ids, input_mask, input_types = cc_todo_pair[0], cc_todo_pair[1], cc_todo_pair[2] 

        _, pooled = self.bert(input_ids = input_ids, \
                                attention_mask = input_mask, \
                                token_type_ids = input_types) 

        features = self.fc0(pooled)
        features = self.fc1(features)
        out = self.fc2(features)
        return out


