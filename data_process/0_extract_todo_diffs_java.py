import os
import json
import re

def diff_processer(diff):
    diff = delete_diff_header(diff)
    diff = replace_commit_id(diff)
    diff = replace_num(diff)
    diff = tokenize_diff(diff)
    return diff

def get_commit_id_regex():
    reexp = r'[\da-fA-F]{7,}\.{2}[\da-fA-F]{7,}|[\da-fA-F]{30,}'
    return reexp

def delete_diff_header(diff):
    '''
    Delete diff header 
    '''
    pattern = r'diff --git .*?(?=(---|Binary files|$))'  
    new_diff = re.sub("\n", "<nl>", diff)
    new_diff = re.sub(pattern, "", new_diff)
    new_diff = re.sub("<nl>", "\n", new_diff)
    new_diff = new_diff.strip()
    return new_diff

def replace_commit_id(diff):
    diff_pattern = get_commit_id_regex()
    new_diff = re.sub(diff_pattern, "<commit_id>", diff)
    return new_diff

def replace_num(diff):
    new_diff = re.sub(r"(\s\d+)"," NUM ", diff)
    return new_diff

def tokenize_by_punctuation(msg):
    punctuation = r'([!"#$%&\'()*+,-./:;<=>?@\[\]^`{|}~]|\\(?!n))'
    new_msg = re.sub(punctuation, r' \1 ', msg)
    id_regex = r'< (commit_id|issue_id) >'
    new_msg = re.sub(id_regex, r'<\1>', new_msg)
    new_msg = " ".join(re.sub(r'\n', ' <nl> ', new_msg).split())
    return new_msg

def tokenize_diff(diff):
    new_diff = re.sub(r'([^-]|^)---(?!-)', r'\1mmm', diff)
    new_diff = re.sub(r'([^+]|^)\+\+\+(?!\+)', r'\1ppp', new_diff)
    new_diff = re.sub(r'index .*', '', new_diff)
    new_diff = re.sub(r'@@.{0,30}@@', 'SEP', new_diff)
    return tokenize_by_punctuation(new_diff)

base_dir = "/data/zpgao/Github_Data/GitHub_Repo/java_repos_diff/"
diff_files = os.listdir(base_dir)

td_keywords = [\
               'todo',  \
               'to do ', \
              ]

print(type(diff_files), len(diff_files))

for f in diff_files:

    todo_diff = {}
    repo_id = f.strip().strip('.json')
    print(f, repo_id)

    with open(base_dir + f, 'r') as diff_file:
        diff_dict = json.load(diff_file)
    # print(type(diff_dict), len(diff_dict))
    # print(diff_dict)

    for k, v in diff_dict.items():
        # print(k)
        # print(v)
        commit_diff = v['commit_diff'].lower()
        diff_pro = diff_processer(v['commit_diff'])

        if any(word in commit_diff for word in td_keywords):
            # print(k)
            # print(commit_diff)
            # save this diff to todo_diff 
            key = k
            value = {}
            value['repo_file'] = f
            value['commit_diff'] = v['commit_diff'] 
            value['commit_now'] = v['commit_now'] 
            value['commit_parent'] = v['commit_parent']
            value['commit_diff_pro'] = diff_pro 
            value['commit_msg'] = v['commit_msg'] 
            todo_diff[key] = value 
            # break
    
    # print(type(todo_diff), len(todo_diff))
    # save todo_diff 
    if len(todo_diff) > 0:
        tgt_fpath = './todo_diff/' + str(repo_id) + '_todo.json'
        with open(tgt_fpath, 'w') as fp: 
            json.dump(todo_diff, fp)
    # break

