#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import export_to_telegraph
from export_to_telegraph import export, _formaturl, exportAllInText
import os
import sys
from bs4 import BeautifulSoup

urls = [
	'https://www.zhihu.com/question/24762672/answer/33939678'
]

s = '''
'''

def testExportAllInText():
	soup = BeautifulSoup(s, features="lxml")
	print(exportAllInText(soup))

def testExport():
	if len(sys.argv) > 1:
		mode = sys.argv[1]
	else:
		mode = ''
	if mode == 'open':
		mode = ''
	for url in urls:
		if not mode in url:
			continue
		print('原文：', url)
		r = export(url, True, True, False)
		print('导出：', r)
		if 'open' in str(sys.argv):
			os.system('open ' + _formaturl(r) + ' -g')
		print('')

def test():
	testExport()
	# testExportAllInText()

if __name__=='__main__':
	test()