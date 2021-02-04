from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def get_stat(y_true, y_pred):
    
    TP = TN = 0 
    FP = FN = 0 
    for true_label, pred_label in zip(y_true, y_pred): 

        if true_label == 1 and pred_label == 1:
            TP += 1
        elif true_label == 0 and pred_label == 0:
            TN += 1
        elif true_label == 1 and pred_label == 0:
            FP += 1
        elif true_label == 0 and pred_label == 1:
            FN +=1  
    return TP, TN, FP, FN 

def get_accuracy(TP, TN, FP, FN):
    return 1.0*(TP + TN)/(TP + TN + FP + FN)

def get_precision(TP, TN, FP, FN):
    return 1.0*(TP)/(TP + FP)

def get_recall(TP, TN, FP, FN):
    return 1.0*(TP)/(TP + FN)

def get_f1(TP, TN, FP, FN):
    precision = get_precision(TP, TN, FP, FN) 
    recall = get_recall(TP, TN, FP, FN) 
    f1_score = 2.0 * precision * recall / (precision + recall) 
    return f1_score

def get_result(result_fpath): 
    
    y_true = []
    y_pred = []

    with open(result_fpath, 'r') as result:
        for line in result:
            true_label, pred_label = line.strip().split('\t')
            y_true.append( int(true_label) ) 
            y_pred.append( int(pred_label) )

    TP, TN, FP, FN = get_stat(y_true, y_pred)
    # print(TP, TN, FP, FN)
    accuracy = get_accuracy(TP, TN, FP, FN) 
    # print("cc_todo_overlap accuracy:", accuracy)
    precision = get_precision(TP, TN, FP, FN)
    # print("cc_todo_overlap precision:", precision)
    recall = get_recall(TP, TN, FP, FN)
    # print("cc_todo_overlap recall:", recall)
    f1 = get_f1(TP, TN, FP, FN)
    # print("cc_todo_overlap f1:", f1)
    return accuracy, precision, recall, f1 

result_fpath = './result/test_result/test.result'
accuracy, precision, recall, f1 = get_result(result_fpath) 
print("cc_todo_overlap accuracy:", accuracy)
print("cc_todo_overlap precision:", precision)
print("cc_todo_overlap recall:", recall)
print("cc_todo_overlap f1:", f1)

