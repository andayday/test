from flask import Flask, render_template, abort
import json
from os import listdir
from os.path import isfile, join

g_path = '/root/myflask/zixun/files/'

def list_all_files(path):
	return [ f for f in listdir(path) if isfile(join(path, f))]

def file_is_exist(filename):
	return os.path.exists(filename)

def json_file_dumps(path):
	pass

def json_file_loads(path):
	try:
		with open(path, 'r', encoding = 'utf-8') as f:
			return json.load(f)
	except IOError:
		print('Error: no found file or open file failed')

def get_news(path):
	news = json_file_loads(path)
	return news


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.route('/')
def index():
	list_files = list_all_files(g_path)
	filenames = {}
	for list_file in list_files:
		title = get_news(join(g_path, list_file)).get('title', '')
		filenames[title] = list_file.split('.')[0]
	return render_template('base.html', filenames = filenames)


@app.route('/files/<filename>')
def file(filename):
	list_files = list_all_files(g_path)
	for list_file in list_files:
		name = list_file.split('.')[0]
		print('name:{} filename: {}'.format(name, filename))
		if name == filename:
			news = get_news(join(g_path, list_file))
			return render_template('file.html', news = news)
	abort(404)
	



if __name__ == '__main__':
	app.run()


