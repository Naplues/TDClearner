import os
import json

base_dir = "/data/zpgao/Github_Data/GitHub_Repo/python_repos_diff/"
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
            value['commit_diff_pro'] = v['commit_diff_pro']
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

