from utils import *
from Bert_MLP import Model, Config
# from Bert_CNN import Model, Config

# Load the iterator
with open('./validation_dataloader.pkl', 'rb') as handler:
    validation_dataloader = pickle.load(handler)
print("validation dataloader loaded!")

PATH = './model_save/epoch1/model.ckpt'
config = Config()
# model = Model(config)
model = Model(config).to(config.device)
model.load_state_dict(torch.load(PATH))
model.eval()
print('Model Loaded!')

# exit()
# ========================================
#              Testing 
# ========================================

# After the completion of each training epoch, measure our performance on
# our validation set. 
print("")
print("Running Validation...")

t0 = time.time()
# Put the model in evaluation mode--the dropout layers behave differently
# during evaluation.

# Tracking variables
total_eval_accuracy = 0
total_eval_loss = 0
nb_eval_steps = 0

# Evaluate data for one epoch 
for batch in validation_dataloader:
    # Unpack this training batch from our dataloader 
    # As we unpack the batch, we will also copy each tensor to the GPU using 'to' method
    # 'batch' contains three pytorch tensors:
    # [0]: input ids
    # [1]: attention masks
    # [2]: labels
    b_input_ids   = batch[0].to(config.device)
    b_input_mask  = batch[1].to(config.device)
    b_input_types = batch[2].to(config.device)
    b_labels = batch[3].to(config.device)
    
    with torch.no_grad():
    # Forward pass, calculate logit predictions.  
    # token_type_ids is the same as "segment ids",  
    # which differentiates sentence 1 and 2 in 2-sentence tasks.  
    # values prior to applying an activation function like the softmax. 
        b_input = (b_input_ids, b_input_mask, b_input_types)
        b_outputs = model(b_input)

    loss = F.cross_entropy(b_outputs, b_labels)
    # Accumulate the validation loss.
    total_eval_loss += loss.item()
     
    # move labels to CPU 
    preds = torch.max(b_outputs.data, 1)[1].cpu().numpy()
    labels = b_labels.to('cpu').numpy()
    # print("preds:", type(preds), preds.shape)
    print("preds:", preds)
    # print("labels:", type(labels), labels.shape)
    print("labels:", labels)
 
    # Calculate the accuracy for this batch of test sentences, and
    total_eval_accuracy += flat_accuracy(preds, labels)
    # print("total eval acc:", total_eval_accuracy)
    # break
    

# Report the final accuracy for this testing run.
print(total_eval_accuracy)
print(len(validation_dataloader))
avg_val_accuracy = total_eval_accuracy / len(validation_dataloader)
print("  Accuracy: {0:.4f}".format(avg_val_accuracy))

