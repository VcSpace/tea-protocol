import os
import time
import json
import shutil
import getpass
import random
import string
import subprocess
import asyncio
import base64

from github import Github
from github import Auth
from github import InputGitTreeElement


# using an access token
# https://github.com/settings/tokens?type=beta
# https://zhuanlan.zhihu.com/p/501496337
"""
npm init --scope=username
"""

auth = Auth.Token("github_pat_****")

g = Github(auth=auth)

async def get_reponame(prefix):
    random.seed(time.time())

    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{prefix}-{random_string}", random_string


async def create_repo(name):
    user = g.get_user()
    repo = user.create_repo(name, description="Is " + name)
    file_content = 'Hello, world!'

    encoded_content = base64.b64encode(file_content.encode('utf-8')).decode('utf-8')

    repo.create_file("README.md", "initial commit", encoded_content)

    print("New repository created:", repo.full_name)
    return repo


async def create_package(npm_username, lastname, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    package_directory = os.path.join(directory, lastname)

    if not os.path.exists(package_directory):
        os.makedirs(package_directory)

    scope = f"@{npm_username}"
    node_command = f'npm init --scope={scope} --yes'

    process = subprocess.Popen(node_command, shell=True, cwd=package_directory, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f'Package "{lastname}" created successfully in directory "{package_directory}".')
        # print(stdout.decode())
    else:
        print('An error occurred:')
        # print(stderr.decode())

async def add_packagejson(main_package_name, github_username, str_package_name, repo_name, npm_username, dir):
    data = {
        "name": "@{0}/{1}".format(npm_username, repo_name),
        "version": "1.0.0",
        "description": "Convert to the text you want.",
        "main": "index.js",
        "repository": {
            "type": "git",
            "url": "https://github.com/{0}/{1}.git".format(github_username, repo_name)
        },
        "keywords": [
            "string",
            "convert"
        ],
        "author": "{0}".format(npm_username),
        "license": "MIT",
        "bugs": {
            "url": "https://github.com/{0}/{1}/issues".format(github_username, repo_name)
        },
        "homepage": "https://github.com/{0}/{1}#readme".format(github_username, repo_name),
        "dependencies": {
            main_package_name: "^1.0.11",
            str_package_name: "^1.0.0"
        }
    }

    with open(dir + "/package.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



async def copy_files_to(src_dir, dest_dir):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.copy(src_dir + "/index.js", dest_dir)


async def push_to_repo(repo, dir):
    local_path = 'your_local_directory_path'
    github_path = 'your_github_directory_path'

    commit_message = 'Add files'
    master_ref = repo.get_git_ref('heads/main')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)

    element_list = []
    for entry in os.listdir(dir):
        try:
            with open(os.path.join(dir, entry), 'rb') as input_file:
                data = input_file.read()
            element = InputGitTreeElement(entry, '100644', 'blob', data.decode('utf-8'))
            element_list.append(element)
        except Exception as e:
            print(e)


    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
    print("upload files to github")


async def publish_npm(dir):
    os.environ['HTTP_PROXY'] = 'http://127.0.0.1:8889'
    os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:8889'
    result = subprocess.run('npm publish --access=public', shell=True, cwd=dir, capture_output=True, text=True, env=os.environ)
    print("npm publish: ", result)


async def main():
    prefix = ''  # 改
    npm_username = ''  # 改
    main_package_name = '@/'  # 改
    github_username = npm_username  # 改
    repo = ''
    for _ in range(0, 25):
        # 创建github仓库
        repo_name, lastname = await get_reponame(prefix)
        task1 = asyncio.create_task(create_repo(repo_name))

        # 创建npm包
        task2 = asyncio.create_task(create_package(npm_username, lastname, './npmpackage'))

        # 等待创建仓库和包的任务完成
        repo, _ = await asyncio.gather(task1, task2)

        # 修改packagejson
        package_name = '@{0}/{1}'.format(npm_username, repo_name)
        task3 = asyncio.create_task(add_packagejson(main_package_name, github_username, package_name, repo_name, npm_username, "./npmpackage/" + lastname))

        # 拷贝文件
        src_path = "./node_files"
        task4 = asyncio.create_task(copy_files_to(src_path, "./npmpackage/" + lastname))

        # 等待修改package.json和拷贝文件的任务完成
        await asyncio.gather(task3, task4)

        # 上传到npm
        task5 = asyncio.create_task(publish_npm("./npmpackage/" + lastname))

        # 上传到github
        task6 = asyncio.create_task(push_to_repo(repo, "./npmpackage/" + lastname))
        await asyncio.gather(task5, task6)


asyncio.run(main())
g.close()
