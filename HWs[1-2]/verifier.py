import requests

TOKEN = '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'

TASK_PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS', 'ITERATOR']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Refactored', 'Deleted', 'Moved']


def check_prefixes(title):
    res = []
    arr = title.split('-')
    pre = arr[0]
    post = arr[1].split(' ')

    if pre not in TASK_PREFIX:
        res.append("Task prefix must be one of them: {}, {}, {}, {}, {}, {}".format(TASK_PREFIX[0], TASK_PREFIX[1],
                                                                                    TASK_PREFIX[2], TASK_PREFIX[3],
                                                                                    TASK_PREFIX[4], TASK_PREFIX[5]))
    if post[0] not in GROUP:
        res.append("Number of your group must be one of them: {}, {}".format(GROUP[0], GROUP[1]))

    if len(post) > 1 and post[1] not in ACTION:
        res.append("Action must be one of them: {}, {}, {}, {}".format(ACTION[0], ACTION[1], ACTION[2], ACTION[3]))

    return '\n'.join(res)


def send_pr_comment(pr, message_error):
    data = {'body': message_error,
            'path': requests.get(pr['url'] + '/files', headers={'Authorization': 'Token {}'.format(TOKEN),
                                                                'Content-Type': "application/json",
                                                                'Accept': "application/vnd.github.v3+json"
                                                                }).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    r = requests.post(pr['url']+'/comments', headers={'Authorization': 'Token {}'.format(TOKEN),
                                                      'Content-Type': "application/json",
                                                      'Accept': "application/vnd.github.v3+json"
                                                      }, json=data)
    print(r.json())


def get_all_pr_commits(pr):
    return requests.get(pr['commits_url'], headers={'Authorization': 'Token {}'.format(TOKEN),
                                                    'Content-Type': "application/json",
                                                    'Accept': "application/vnd.github.v3+json"
                                                    })


def get_all_user_prs(user_login, repo_name, pr_state):
    return requests.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repo_name, pr_state),
                        headers={'Authorization': 'Token {}'.format(TOKEN),
                                 'Content-Type': "application/json",
                                 'Accept': "application/vnd.github.v3+json"
                                 })


def create_comment(pr):
    all_coms = []
    message = "Your pull request: {}\n".format(pr['title']) + check_prefixes(pr['title']) + '\n\n'
    commits = get_all_pr_commits(pr).json()
    for com in commits:
        all_coms.append(com['commit']['message'])

    for com in all_coms:
        message += 'Your commit: {}\n'.format(com) + check_prefixes(com) + '\n'

    return message


def main():
    all_pr = get_all_user_prs('Savel-cmyk', 'python_au', 'open').json()
    for pr in all_pr:
        if len(create_comment(pr)) > 200:
            send_pr_comment(pr, create_comment(pr))


if __name__ == '__main__':
    main()
