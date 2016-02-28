#IT'S working
import requests
import re

url = input("Enter a website to extract info: ")
resp  = requests.get("http://" +url)
page=resp.text

def scrap():
	print('-----------------------------------------')
	print('1.Website url')
	print('2.Email')
	print('3.Mobile number')
	print('4.Exit')
	print('-----------------------------------------')

	opt=int(input('What do you want to extract?:'))
	re_list=[]
	if opt==1:
		re_list=re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',page)
		for item in re_list:
			print (item)
		scrap()
	elif opt==2:
		re_list=re.findall(r'[\w\.-]+@[\w\.-]+',page)
		for item in re_list:
			print (item)
		scrap()
	elif opt==3:
		re_list=re.findall(r'^[789]\d{9}$',page)
		for item in re_list:
			print (item)
		scrap()
	elif opt==4:
		return
	else:
		print('Wrong option')
		scrap()

	
scrap()		



