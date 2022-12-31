from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Firefox(executable_path="/driver/geckodriver", options=options)

def youla_service(number: int):
	driver.get('https://connect.vk.com/auth?app_id=7733222&v=0.0.2&redirect_uri=https%3A%2F%2Fyoula.ru%2F&uuid=mOBWhWIJGV0Lve-fVl-5l&redirect_state=vk-connect-auth-redirect&app_settings=eyJ2a2NfYmVoYXZpb3IiOiJ3aXRob3V0X3Bob25lIiwic2VydmljZV9ncm91cHMiOnsiZnVsbF9hdXRoX3ZpYV92a2Nvbm5lY3QiOiJleHAifSwiZXh0ZXJuYWxfZGV2aWNlX2lkIjoiNjM5OWU1YmRiYTEyYSJ9')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.CLASS_NAME, "vkc__TextField__input")
	btn = driver.find_element(By.CLASS_NAME, "vkuiButton__in")
	phone_form.send_keys(number)
	btn.click()
	sleep(2)
	
def yandex_service(number: int):
	driver.get('https://passport.yandex.ru/auth/reg?retpath=%2F%2Fyandex.ru%2Fsupport%2Fid%2Fauthorization%2Fphone-number.html')
	phone_form = driver.find_element(By.ID, "passp-field-phone")
	driver.implicitly_wait(5)
	btn = driver.find_element(By.ID, "passp:phone:controls:next")
	phone_form.send_keys(number)
	btn.click()
	sleep(2)
	
def ivi_service(number: int):
	driver.get('https://www.ivi.ru/profile')
	driver.implicitly_wait(5)
	btn_preload_form = driver.find_element(By.CLASS_NAME, "profileUserInfo__nbl-button_auth").click()
	phone_form = driver.find_element(By.CLASS_NAME, "nbl-input__editbox")
	phone_form.send_keys(f"8{number}")
	phone_form.send_keys(Keys.RETURN)
	sleep(2)
	
def kontur_service(number: int):
	driver.get('https://auth.kontur.ru/phone?customize=cacabinet&back=https%3A%2F%2Fidentity.kontur.ru%2Fconnect%2Fauthorize%3Fclient_id%3DCACabinet%26redirect_uri%3Dhttps%253A%252F%252Fi.kontur-ca.ru%252FAuthCallback%26response_mode%3Dform_post%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520email%2520phone%2520auth.sid%2520auth.factor%2520portal.notarius.ex%2520incarnation%26state%3DOpenIdConnect.AuthenticationProperties%253Dfv8gLCO_Q7zceJpjdte5B3S7SHZiOSXPMVvnb6L4vbwhcxWdmtYuYod4xWC2qJEgOXJoSnFEKjs1usjQ_WzePJVurehFN15xMkH4P79Pjcepyqaa183H4Y3LNQmppSbeRxpQ7jMoShn5HyV660GEe1s_Xi7maK41qHCBMVN0iTUxSgkWS6K1eAH-k_TAjbyEJku9AUGIb_gQI2xDshvpksCLil5EWvRqfVzeXL-W9ew%26nonce%3D638068810151011700.Y2E1ZDQ1ODYtMGQzMC00OTkxLTkzNmQtY2JjNTVhMjgxNzk2NzMzMzM4MzUtM2Q5Yy00N2M3LWJkOTctOThiOTZhOTA4NmY4%26x-client-SKU%3DID_NET461%26x-client-ver%3D5.3.0.0')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.NAME, 'phone')
	phone_form.send_keys(number)
	btn = driver.find_element(By.CSS_SELECTOR, '.react-ui-yrcnz0').click()
	
def vkusvill_service(number: int):
	driver.get('https://vkusvill.ru/personal/')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.CLASS_NAME, 'js-user-form-checksms-api-phone1')
	phone_form.send_keys(number)
	sleep(2)
	btn = driver.find_element(By.CLASS_NAME, 'js-user-form-submit-btn').click()
	
def x5id_service(number: int):
	driver.get('https://id.x5.ru/auth/realms/ssox5id/protocol/openid-connect/auth?client_id=x5id-lk&response_type=code&redirect_uri=https%3A%2F%2Fx5id.ru%2Flk%2Fprofile&response_mode=fragment&state=e1174052-abd6-475b-8856-d83ff0683c02&nonce=aaeaa02d-2571-4d6c-8213-921699612a82&scope=openid+offline_access&code_challenge=vAqPSldWF2tnFaPiQZp9-TT7cDD69pi3jgyEh45HY2M&code_challenge_method=S256')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.ID, 'username')
	phone_form.send_keys(number)
	btn = driver.find_element(By.ID, 'fake_submit_button')
	btn.click()
	sleep(2)
	
def medtochka_service(number: int):
	driver.get('https://app.medtochka.ru/authorization/')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.ID, 'input-28')
	phone_form.send_keys(number)
	phone_form.send_keys(Keys.RETURN)
	sleep(2)
	
	
def magnit_service(number: int):
	driver.get('https://new.moy.magnit.ru/#auth-login')
	driver.implicitly_wait(5)
	preload_form = driver.find_element(By.CLASS_NAME, 'button--login').click()
	phone_form = driver.find_element(By.ID, 'phone')
	phone_form.send_keys(number)
	phone_form.send_keys(Keys.RETURN)
	sleep(2)
	
def cg_service(number: int):
	driver.get('https://new.chitai-gorod.ru/')
	driver.implicitly_wait(5)
	preload_form = driver.find_element(By.CLASS_NAME, 'link-wrapper').click()
	phone_form = driver.find_element(By.CLASS_NAME, 'phone-input__input')
	phone_form.send_keys(number[1:])
	phone_form.send_keys(number)
	phone_form.send_keys(Keys.RETURN)
	sleep(2)
	
def zarubas_service(number: int):
	driver.get('https://народныйзайм.рф/')
	driver.implicitly_wait(5)
	name_form = driver.find_element(By.ID, 'fullName')
	name_form.send_keys('Шаповалова Елена Геннадьевна')
	phone_form = driver.find_element(By.ID, 'indexform-phonenumber')
	phone_form.send_keys(number)
	btn = driver.find_element(By.CLASS_NAME, 'tpl-btn').click()
	
def smotr_service(number: int):
	driver.get('https://smotreshka.tv/reg')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.NAME, 'phone')
	phone_form.send_keys(number)
	phone_form.send_keys(Keys.RETURN)
	
def zdapteka_service(number: int):
	driver.get('https://zdesapteka.ru/auth/')
	driver.implicitly_wait(5)
	phone_form = driver.find_element(By.ID, 'USER_PHONE_POPUP')
	phone_form.send_keys(number)
	phone_form.send_keys(Keys.RETURN)
	
def youdo_service(number: int):
	driver.get('https://youdo.com/')
	driver.implicitly_wait(5)
	preload = driver.find_element(By.CLASS_NAME, 'AnonymousLogin_link__1pGSj').click()
	phone_form = driver.find_element(By.NAME, 'login')
	phone_form.send_keys(f"+7{number}")
	phone_form.send_keys(Keys.RETURN)

	


