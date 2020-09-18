import io
import sys
import json
import time
import urllib
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import unicodedata
from bs4 import BeautifulSoup


# x = str(sys.argv[1])

# y = str(sys.argv[2])

class btn(object):



	__url = 'https://internetbanking.btn.co.id/retail/login/loginRequest'
	__urlC = 'https://internetbanking.btn.co.id/retail/login/checkCookie'
	def __init__(self):
		self.formLogin()

	def formLogin(self):
		''' webdriver : Chrome() Firefox() PhantomJS() '''
		# username ='Ningrum'
		# password = 'NingrumF0212'
		# jawab = ''
		# username =x
		# password = y
		# chrome_options = Options()
		# chrome_options.add_experimental_option("detach", True)
		self.__driver =  webdriver.Chrome(executable_path=r'C:/xampp/htdocs/PANING/public/bca-scrapping-master/chromedriver.exe')
		# self.__driver = webdriver.Firefox()
		self.__driver.wait = WebDriverWait(self.__driver, 5)
		# self.__driver.add_argument('--disable-gpu')
		# alert = self.__driver.switch_to_alert()
		self.__username = 'Ningrum'
		self.__password = 'NingrumF0212'
		self.pertanyaan = ''
		#self.__jawab1 = '1958'
		#self.__jawab2 = '1974'
		#self.__jawab3 = 'BATUMARTA'
		# cookie = self.__driver.get_cookies()
		# print(len(cookie))
		# print(cookie)	
		self.authLogin()
		# Wait for the alert to be displayed
		# wait.until(expected_conditions.alert_is_present())
			
# 	# Click the link to activate the alert
# driver.find_element(By.LINK_TEXT, "See a sample prompt").click()

# # Wait for the alert to be displayed
# wait.until(expected_conditions.alert_is_present())

# # Store the alert in a variable for reuse
# alert = Alert(driver)

# # Type your message
# alert.send_keys("Selenium")

# # Press the OK button
# alert.accept()

	def authLogin(self):

		self.__driver.get(self.__url)			
		username = self.__driver.wait.until(EC.presence_of_element_located((By.NAME, "userName")))
		password = self.__driver.wait.until(EC.element_to_be_clickable((By.NAME, "passwordEncryption")))
		loginBTN = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div/div[5]/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[3]/td[2]/input[2]")))		
		# InptBTN = self.__driver.wait.until(EC.presence_of_element_located((By.NAME, "securityAnswer")))
		# AccBTN =  self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div/div[4]/table/tbody/tr[4]/td[2]/input[1]")))
		# InptBTNAlert = self.__driver.wait.until(EC.presence_of_element_located((By.ID, "headerSecurity")))
		username.send_keys(self.__username)
		password.send_keys(self.__password)
		loginBTN.send_keys(webdriver.common.keys.Keys.SPACE)
		popUp = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='popUp']/table/tbody/tr[2]/td[3]")))
		pq = popUp.text	
		# self.validation(pq)	
		uncode_pq = pq.encode("utf-8")
		# uncode_pq = pq.lstrip()
		string = pq.replace(":", "")
		self.pertanyaan = string.lstrip()
		
		# self.__tanya = self.__driver.validation(string)
		self.validation()
		self.cekMutasi()
	
	def validation(self):
		# self.__driver.find_element_by_name
		# InptBTN = self.__driver.find_element_by_name("securityAnswer")
		# AccBTN = self.__driver.find_element_by_xpath("/html/body/form/div/div[4]/table/tbody/tr[4]/td[2]/input[1]")
		InptBTN = self.__driver.wait.until(EC.presence_of_element_located((By.NAME, "securityAnswer")))
		AccBTN =  self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div/div[4]/table/tbody/tr[4]/td[2]/input[1]")))
		print(self.pertanyaan)
		if self.pertanyaan == "In what city were you born?" :
			print(self.pertanyaan)
			print ('BATUMARTA')
			InptBTN.send_keys("BATUMARTA")
			AccBTN.click()
		elif self.pertanyaan == "In what year was your mother born?":
			print(self.pertanyaan)
			print ('1974')
			InptBTN.send_keys("1974")
			AccBTN.click()
		elif self.pertanyaan == "In what year was your father born?":
			print(self.pertanyaan)
			print ('1958')
			InptBTN.send_keys("1958")
			AccBTN.click()
		else:
			pass
			print("Gak Ngirim")
            # print(question)
			# self.authLogin()



	# def isiPopUp1(self):			
			# loginBTN = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div/div[5]/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[3]/td[2]/input[2]")))		
			# self.__driver.get(self.__url)			
			# InptBTN = self.__driver.wait.until(EC.presence_of_element_located((By.NAME, "securityAnswer")))
			# AccBTN =  self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/form/div/div[4]/table/tbody/tr[4]/td[2]/input[1]")))
			# popUp = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='popUp']/table/tbody")))

			# print(popUp)
			# pertanyaan = ['In what city were you born?', 'In what year was your mother born?', 'In what year was your father born?']
					


	def logout(self):
		try :
			# self.__driver.switch_to.frame(self.__driver.find_element_by_xpath("//*[@id='loginForm']"))
			# self.__driver.switch_to.frame(self.__driver.find_element_by_xpath("//frame[@name=\"logout\"]"))
			# self.__driver.switch_to.frame(self.__driver.find_element_by_xpath("//frame[@name=\"header\"]"))
			logout = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH,"//a[@id=\"SignonButton\"]/img")))
			logout.click()
			print("Anda berhasil logout")
		except TimeoutException:
		    print("Gagal logout")

	def cekMutasi(self):
		# try:
			# Dropdown = self.find_element_by_visible_text("Rekening")
			print("ciyee Wes Iso Login")
			# self.__driver.switch_to_default_content()
			self.__driver.switch_to.frame(self.__driver.find_element_by_xpath("//*[@id=\"primecash_iframe\"]"))
			print("masuk frame")
			Dropdown = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id=\"mainNav\"]/ul/li[1]")))
			Dropdown.click()
			print("iso klik rekening")
			# self.__driver.find_element_by_visible_text('Rekening')
			menuMutasi = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id=\"mainNav\"]/ul/li[1]/div/div/div/div/div[1]/div/div/ul/li[1]/div/div/h3/a")))
			menuMutasi.click()
			print("Iso klik semua rekening ")
			self.__driver.switch_to.frame(self.__driver.find_element_by_xpath("//*[@id=\"mainFrame\"]"))
			# cek_mutasi = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH,"//a[@onclick=\"onDetailClickAcct('22401561890112','SBA');parent.loadingBar();\" ]")))
			try:
				cekMutasi = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class=\"odd\"]/td[1]/div/a")))
				cekMutasi.click()
				# self.__driver.switch_to_default_content()
				print("Alhamdulillah Gusti, Iso ganti ndek data tabel")
				logout = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH,"//a[@id=\"SignonButton\"]/img")))
				logout.click()
			except:
				print("Gak iso ganti ndek data tabel")
				logout = self.__driver.wait.until(EC.presence_of_element_located((By.XPATH,"//a[@id=\"SignonButton\"]/img")))
				logout.click()

 
if __name__ == "__main__":
	options = webdriver.ChromeOptions()
	# chrome_options.add_experimental_option("detach", True)
	options.add_argument("--no-sandbox")
	btn()