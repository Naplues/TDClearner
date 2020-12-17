from utils import *
from Bert_MLP import Config

# Get the lists of questions 
questions = df.question.values.tolist()
cs0 = df.cs0.values.tolist()
labels = df.label.values.tolist()

# Tokenize & Input Formatting
## Import model/tokenizer 
## Load the BERT model
print("Loading BERT Model...")
bert_model = BertModel.from_pretrained('./Model')
bert_model.cuda()
print("Loading BERT Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained('./Model')
# tokenizer = tokenizer_class.from_pretrained('./Model', do_lower_case=True)

# Required Formatting
## 1. sentences to ids
## 2. Padding & Truncating                          
## 3. Attention Masks
## 4. 
# Combine question + cs0 as the first inputs
encoded_qc0 = tokenizer(questions, cs0, padding=True, truncation=True, max_length=128, return_tensors='pt')
print("encoded_qc0:", type(encoded_qc0), len(encoded_qc0))
qc0_input_ids = encoded_qc0['input_ids']
qc0_token_type_ids = encoded_qc0['token_type_ids']
qc0_attention_masks = encoded_qc0['attention_mask']

print("qc0_input_ids:", type(qc0_input_ids), qc0_input_ids.shape)
print("qc0_type_ids:", type(qc0_token_type_ids), qc0_token_type_ids.shape)
print("qc0_attn_mask:", type(qc0_attention_masks), qc0_attention_masks.shape)

# Convert list to numpy array
qc0_input_ids = qc0_input_ids.cpu().detach().numpy()
qc0_token_type_ids = qc0_token_type_ids.cpu().detach().numpy()
qc0_attention_masks = qc0_attention_masks.cpu().detach().numpy()
print("qc0_input_ids:", type(qc0_input_ids), qc0_input_ids.shape )
print("qc0_type_ids:", type(qc0_token_type_ids), qc0_token_type_ids.shape )
print("qc0_attn_mask:", type(qc0_attention_masks), qc0_attention_masks.shape )

labels = np.asarray(labels)

with open('./Data/encoded_qc0.pkl', 'wb') as handle: 
    pickle.dump(encoded_qc0, handle) 

with open('./Data/labels.pkl', 'wb') as handle:
    pickle.dump(labels, handle)

# Training and Validation Split on qc0


