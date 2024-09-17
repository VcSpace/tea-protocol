# npm_username = '0'
# lastname = ''
#
# str_main_package = "\"@/\": \"^1.0.11\",\n  "
# str_packagename = "\"@" + npm_username + "/" + lastname + "\": " + "\"^1.0.0\""
#
# str_add_package_json = "\"dependencies\": {" + "\n  " + str_main_package + str_packagename + "\n}"
#
#
# print(str_add_package_json)
#
#
# import json
# github_username = npm_username
# str_main_package_name = '@/cstr'
# str_package_name = '@{0}/{1}'.format(npm_username, lastname)
#
# data = {
#     "name": "@{0}/{1}".format(npm_username, lastname),
#     "version": "1.0.0",
#     "description": "Convert to the text you want.",
#     "main": "index.js",
#     "repository": {
#         "type": "git",
#         "url": "https://github.com/{0}/{1}.git".format(github_username, lastname)
#       },
#     "keywords": [
#         "string",
#         "convert"
#     ],
#     "author": "{0}".format(npm_username),
#     "license": "MIT",
#     "bugs": {
#         "url": "https://github.com/{0}/{1}/issues".format(github_username, lastname)
#     },
#     "homepage": "https://github.com/{0}/{1}#readme".format(github_username, lastname),
#     "dependencies": {
#         str_main_package_name: "^1.0.11",
#         str_package_name: "^1.0.0"
#     }
# }
#
# json_data = json.dumps(data, indent=4, ensure_ascii=False)
#
# print(json_data)
import os
import shutil
dest_folder = "./dest"
src_dir = "./src"


if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

shutil.copy(src_dir + "/index.js", dest_folder)

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)


dest_dir = os.path.join(dest_folder, 'sub_modules')
shutil.copytree(os.path.join(src_dir, 'sub_modules'), dest_dir, dirs_exist_ok=True)