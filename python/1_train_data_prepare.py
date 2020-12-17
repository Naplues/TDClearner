from utils import *
from Bert_MLP import Config

# Import DataSet 
code_change_lst = []
todo_comment_lst = []
label_lst = []
with open('./cc_todo_pairs', 'r') as fin:
    for line in fin: 
        code_change, todo_comment, label = line.strip().split('\t')
        label = int(label)
        code_change_lst.append( code_change )
        todo_comment_lst.append( todo_comment )
        label_lst.append( label )

assert len(code_change_lst) == len(todo_comment_lst)
assert len(todo_comment_lst) == len(label_lst)
print("code_change_lst:", type(code_change_lst), len(code_change_lst))
print("todo_comment_lst:", type(todo_comment_lst), len(todo_comment_lst))
print("label_lst:", type(label_lst), len(label_lst))

## Tokenize & Input Formatting
## Import model/tokenizer 
## Load the BERT model
print("Loading BERT Model...")
bert_model = BertModel.from_pretrained('./Model')
bert_model.cuda()
print("Loading BERT Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained('./Model')
print("BERT Loaded!")

#  Required Formatting
## 1. sentences to ids
## 2. Padding & Truncating                          
## 3. Attention Masks
## 4. 
# Combine question + cs0 as the first inputs
encoded_cc_todo = tokenizer(code_change_lst, todo_comment_lst, padding=True, truncation=True, max_length=128, return_tensors='pt')
print("encoded_cc_todo:", type(encoded_cc_todo), len(encoded_cc_todo))
cc_todo_input_ids = encoded_cc_todo['input_ids']
cc_todo_token_type_ids = encoded_cc_todo['token_type_ids']
cc_todo_attention_masks = encoded_cc_todo['attention_mask']

print("cc_todo_input_ids:", type(cc_todo_input_ids), cc_todo_input_ids.shape)
print("cc_todo_type_ids:", type(cc_todo_token_type_ids), cc_todo_token_type_ids.shape)
print("cc_todo_attn_mask:", type(cc_todo_attention_masks), cc_todo_attention_masks.shape)

# Convert list to numpy array
cc_todo_input_ids = cc_todo_input_ids.cpu().detach().numpy()
cc_todo_token_type_ids = cc_todo_token_type_ids.cpu().detach().numpy()
cc_todo_attention_masks = cc_todo_attention_masks.cpu().detach().numpy()
print("qc0_input_ids:", type(cc_todo_input_ids), cc_todo_input_ids.shape )
print("qc0_type_ids:", type(cc_todo_token_type_ids), cc_todo_token_type_ids.shape )
print("qc0_attn_mask:", type(cc_todo_attention_masks), cc_todo_attention_masks.shape )

labels = np.asarray(label_lst)

with open('./encoded_cc_todo.pkl', 'wb') as handle: 
    pickle.dump(encoded_cc_todo, handle) 

with open('./labels.pkl', 'wb') as handle:
    pickle.dump(labels, handle)

# Training and Validation Split on qc0
# Use 97% for training and 3% for validation
train_inputs, validation_inputs, train_labels, validation_labels = train_test_split(cc_todo_input_ids, \
                                                                                    labels, \
                                                                                    random_state=2018, \
                                                                                    test_size=0.1)
# Do the same for attention_mask
train_masks, validation_masks, _, _ = train_test_split(cc_todo_attention_masks, \
                                                       labels, \
                                                       random_state=2018, \
                                                       test_size = 0.1)

# Do the same for token_type_ids
train_types, validation_types, _, _ = train_test_split(cc_todo_token_type_ids, \
                                                       labels, \
                                                       random_state=2018, \
                                                       test_size = 0.1)


# Convert to Pytorch Data Types
train_inputs = torch.tensor(train_inputs)
train_masks = torch.tensor(train_masks)
train_types = torch.tensor(train_types)

train_inputs = torch.tensor(train_inputs)
train_masks = torch.tensor(train_masks)
train_types = torch.tensor(train_types)

validation_inputs = torch.tensor(validation_inputs)
validation_masks = torch.tensor(validation_masks)
validation_types = torch.tensor(validation_types)

validation_inputs = torch.tensor(validation_inputs)
validation_masks = torch.tensor(validation_masks)
validation_types = torch.tensor(validation_types)

train_labels = torch.tensor(train_labels)
validation_labels = torch.tensor(validation_labels)

print("train_inputs:", type(train_inputs), train_inputs.shape)
print("train_masks:", type(train_masks), train_masks.shape)
print("train_types:", type(train_types), train_types.shape)
print("train_labels:", type(train_labels), train_labels.shape)

print("val_inputs:", type(validation_inputs), validation_inputs.shape)
print("val_masks:", type(validation_masks), validation_masks.shape)
print("val_types:", type(validation_types), validation_types.shape)
print("val_labels:", type(validation_labels), validation_labels.shape)

config = Config()

batch_size = config.batch_size
print("batch_size:", batch_size)

# Create the DataLoader for our training set.
train_data = TensorDataset(train_inputs, train_masks, train_types, \
                           train_labels)
train_sampler = RandomSampler(train_data)
train_dataloader = DataLoader(train_data, sampler=train_sampler, batch_size=batch_size)
print(type(train_dataloader))

# Create the DataLoader for our validation set.
validation_data = TensorDataset(validation_inputs, validation_masks, validation_types, \
                                validation_labels)
validation_sampler = SequentialSampler(validation_data)
validation_dataloader = DataLoader(validation_data, sampler=validation_sampler, batch_size=batch_size)
print(type(validation_dataloader))

# Save DataLoader
with open('./train_dataloader.pkl', 'wb') as handle:
    pickle.dump(train_dataloader, handle)

with open('./validation_dataloader.pkl', 'wb') as handle:
    pickle.dump(validation_dataloader, handle)


print("Finished!")
# exit()
