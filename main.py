from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class InstaBot:
    temp = None
    def __init__(self, username, pw):
    
        self.driver = webdriver.Chrome("C:/Users/czagnos/hello/InstaB_v1/chromedriver.exe")
        self.username = username
        self.driver.get("https://instagram.com")
        
    
        # sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
        #     .click()a
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    
    def save_temp(self,temp):
        store_temp = temp
        return store_temp


    def get_common_names(self,first_account,temp):
        
        result = list(set(temp)&set(first_account))
        
        return result 
            

    def get_target_accounts_followers(self,accounts):
        accounts_arr = accounts.split('/')
        array_length = len(accounts_arr)
        temp = None
        for i in range(array_length):
            
            self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]")\
            .send_keys(accounts_arr[i])
            sleep(4)  
            self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(accounts_arr[i]))\
            .click()
            sleep(5)  
            self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
            target_followers = self._get_names()
            sleep(3)
            if i == 0:
                temp = target_followers
                continue
            commons = self.get_common_names(target_followers,temp)
            temp = commons
        
        print(commons)

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        sleep(2)
        not_following_back = [user for user in following if user not in followers]
        #get unfollow the unfollowers TODO
        print(not_following_back)

    def _get_names(self):
        sleep(3)
        sugs = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul') 
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(4)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.refresh()
        return names

my_bot = InstaBot('USER', 'PASS')
my_bot.get_target_accounts_followers('smdbcr/ekinbayrakk/zagnoscan')
#my_bot.get_unfollowers()
