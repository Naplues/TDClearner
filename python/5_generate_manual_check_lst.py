import json

with open('./python_repos_info.json', 'r') as json_f:
    py_repos_info = json.load(json_f)

for k, v in py_repos_info.items():
    print(k)
    print(type(k))
    print(v)
    break

def generate_url():
    '''
    '''
    with open('./data/positive_samples/commit_info_pro.out', 'r') as fin, \
        open('./example_check_url.out', 'w') as fout:
        for line in fin: 
            # print(line.strip())
            repo_file, current_commit, parent_commit = line.strip().split('\t')
            repo_id = repo_file.strip().rstrip('.json') 
            # print(repo_id, current_commit)
            # print(py_repos_info[repo_id])

            repo_url = py_repos_info[repo_id]['repo_clone_url']
            # print(repo_url)
            commit_url = repo_url.split('.git')[0] + '/commit/' + str(current_commit)
            # print(commit_url)
            # break
            fout.write( commit_url )
            fout.write('\n')

    with open('./data/negative_samples/commit_info.out', 'r') as fin, \
        open('./motivation_check_url.out', 'w') as fout:
        for line in fin: 
            # print(line.strip())
            repo_file, current_commit, parent_commit = line.strip().split('\t')
            repo_id = repo_file.strip().rstrip('.json') 
            # print(repo_id, current_commit)
            # print(py_repos_info[repo_id])

            repo_url = py_repos_info[repo_id]['repo_clone_url']
            # print(repo_url)
            commit_url = repo_url.split('.git')[0] + '/commit/' + str(current_commit)
            # print(commit_url)
            # break
            fout.write( commit_url )
            fout.write('\n')

generate_url()

