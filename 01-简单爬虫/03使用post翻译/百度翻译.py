################################百度翻译#################################
import urllib.request as request;
import urllib.parse as parse;
import json;
import time;

while True:
	url = "http://fanyi.baidu.com/v2transapi";
	str = input("请输入要翻译的内容:\n");

	#设置提交表单
	data = {};
	data['from'] = 'en';
	data['to'] = 'zh';
	data['query'] = str;
	data['transtype'] = 'translang';
	data['simple_means_flag'] = '3';
	data = parse.urlencode(data).encode('unicode_escape');
	req = request.Request(url, data);
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36');
	response = request.urlopen(req);
	html = response.read().decode("unicode_escape");

	#打印输出结果,爬虫好像不能返回JSON
	index1 = html.index('"dst":"');
	index2 = html.index(',"src"');
	print("==============");
	print(html[index1+7: index2-1]);
	print("==============");
	print("");
