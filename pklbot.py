from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import schedule
import os

####def run_picklebot():

path=os.getcwd();
filename="pklbot.py";
file_path=os.path.join(path, filename);

print(file_path);

path=os.getcwd();
filename="python3.11.1";
file_path=os.path.join(path, filename);

print(file_path);


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()

web = webdriver.Chrome()

web.get('https://www.sevenrooms.com/reservations/playpkl?duration_picker=true&client_id=0fdfb5e4075736517a53e85e3fafdd34853e8f6888f06e392121cb202d992ef85f12a9fa93c1171afddf73133ae8b80a31b22c2611ecbb3d33e8827cff02b407')

time.sleep(2)

SearchButton = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div[5]/div/button')
SearchButton.click()

time.sleep(2)

####CalendarDropdown = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/div/button')
####CalendarDropdown.click()

time.sleep(2)

html = web.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)

time.sleep(4)

#finicky one where I select a time
#<button data-test="sr-timeslot-button" class="WidgetButton-sc-1304nl8-0 TimeSlot__TimeSlotButton-sc-3gsj50-0 iJCtU lfPGKs"><div class="TimeSlot__TimeSlotText-sc-3gsj50-1 jwqCip">5:00 pm</div><div class="TimeSlot__TimeSlotSecondaryText-sc-3gsj50-2 lenWdd">Pickleball </div></button>
TimeSlot1 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[13]/div/button[1]')
TimeSlot2 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[13]/div/button[2]')
TimeSlot3 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[13]/div/button[3]')
TimeSlot4 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[13]/div/button[4]')
TimeSlot5 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[13]/div/button[5]')

if TimeSlot1.is_enabled():
    TimeSlot1.click()
elif TimeSlot2.is_enabled():
    TimeSlot2.click()
elif TimeSlot3.is_enabled():
    TimeSlot3.click()
elif TimeSlot4.is_enabled():
    TimeSlot4.click()
elif TimeSlot5.is_enabled():
    TimeSlot5.click()
else:
    print("g-dangit")


time.sleep(2)

SelectGuest = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div[2]')
SelectGuest.click()

time.sleep(2)

FirstName = "Michael"
first = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/form/div[1]/div[1]/div/input')
first.send_keys(FirstName)

time.sleep(1)

LastName = "Rosen"
last = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/form/div[1]/div[2]/div/input')
last.send_keys(LastName)

time.sleep(1)

EmailAddress = "mrosen6@tulane.edu"
email = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/form/div[2]/div/input')
email.send_keys(EmailAddress)

time.sleep(1)

PhoneNumber = "7818203654"
phone = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[2]/div/div[2]/form/div[3]/div/div/div[2]/div/input')
phone.send_keys(PhoneNumber)

time.sleep(1)

FirstNameCredit = "Michael"
firstcredit = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[1]/div/input')
firstcredit.send_keys(FirstNameCredit)

time.sleep(1)

LastNameCredit = "Rosen"
lastcredit = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div/div[2]/div[1]/div/div[2]/div/input')
lastcredit.send_keys(LastNameCredit)

time.sleep(1)

CardNumber = "4400662999140275"
number = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div/div[2]/div[2]/div/div/iframe')
number.send_keys(CardNumber)

time.sleep(1)

MMYY = "1127"
my = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div/div[2]/div[2]/div/div/iframe')
my.send_keys(MMYY)

time.sleep(1)

CVC = "679"
cvclocation = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div/div[2]/div[2]/div/div/iframe')
cvclocation.send_keys(CVC)

time.sleep(1)

ZIP = "02482"
ziplocation = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[4]/div/div[2]/div[2]/div/div/iframe')
ziplocation.send_keys(ZIP)

time.sleep(1)

html = web.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)

time.sleep(1)

Cancellation_Policy_Click = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[8]/div[1]/button[1]')
Cancellation_Policy_Click.click()

time.sleep(1)

I_Agree_To_The_Venues_Required_Policy = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[8]/div[2]/button[1]')
I_Agree_To_The_Venues_Required_Policy.click()

time.sleep(1)

I_Certify_I_Am_Above_The_Age_Of_18 = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[8]/div[3]/button')
I_Certify_I_Am_Above_The_Age_Of_18.click()

time.sleep(1)

Receive_News = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[8]/div[4]/button[1]')
Receive_News.click()

time.sleep(1)

Reminders = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[5]/div/div[2]/div[8]/div[5]/button')
Reminders.click()

time.sleep(1)

###BigRedButton = web.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/main/div/div/div[1]/div[8]/button')
####BigRedButton.click()

####time.sleep(20)

    
###schedule.every().day.at("21:27:00").do(run_picklebot)
    

####while True:
    ####schedule.run_pending()
    ####time.sleep(1)