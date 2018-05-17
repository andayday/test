import json
from os import listdir
from os.path import isfile, join

def test():
	with open('/root/myflask/zixun/files/helloshiyanlou.json', 'r', encoding = 'utf-8') as f:
		return json.load(f)
g_path = '/root/myflask/zixun/files/'
def list_all_files(path):
	return [ f for f in listdir(path) if isfile(join(path, f))]
if __name__ == '__main__':
	content = test()
	print(type(content))
	print((content))

	list_files = list_all_files(g_path)
	print(list_files)

