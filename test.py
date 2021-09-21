#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import export_to_telegraph
from export_to_telegraph import export, _formaturl, exportAllInText, getTitle
import os
import sys
from bs4 import BeautifulSoup
from telegram.ext import Updater
import album_sender

with open('bot_token') as f:
	bot_token = f.read().strip()
tele = Updater(bot_token, use_context=True)
chat = tele.bot.get_chat(420074357)

urls = [
	'https://www.thestandnews.com/society/%E5%A4%A7%E5%9F%94%E8%BB%8A%E7%A6%8D%E4%B8%80%E5%80%8B%E6%9C%884-%E6%AD%B2%E7%94%B7%E7%AB%A5%E5%8F%AF%E7%9F%AD%E8%B7%9D%E9%9B%A2%E6%AD%A5%E8%A1%8C-%E5%B9%B4%E5%BA%95%E6%88%96%E5%8F%AF%E9%87%8D%E8%BF%94%E6%A0%A1%E5%9C%92'
]

s = '''
'''

def testExportAllInText():
	soup = BeautifulSoup(s, features="lxml")
	print(exportAllInText(soup))

def testExport():
	for url in urls:
		print(export_to_telegraph.getTitle(url))
		print(export_to_telegraph.article.getAuthor(url))
		# print('原文：', url)
		# r = export_to_telegraph.export(url, True, True, True)
		# print('导出：', r)
		# os.system('open ' + _formaturl(r) + ' -g')
		# print('')

def test():
	testExport()
	# testExportAllInText()

def testAlbum():
	album = export_to_telegraph.getAlbum(urls[0])
	print(album)
	album_sender.send_v2(chat, album)

if __name__=='__main__':
	testExport()