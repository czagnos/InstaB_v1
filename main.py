from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class InstaBot:
    temp = None
    def __init__(self, username, pw):
    
        self.driver = webdriver.Chrome()
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

    



    def get_common_names(self,first_account,index):
            def save_temp(temp):
                store_temp = temp
                return store_temp
            temp = first_account
            if(index == 0):
                save_temp(temp)
                return(print("First"))
            

            
            return 
            

    def get_target_accounts_followers(self,accounts):
        accounts_arr = accounts.split('/')
        array_length = len(accounts_arr)
        for i in range(array_length):
            
            self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]")\
            .send_keys(accounts_arr[i])
            sleep(3)  
            self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(accounts_arr[i]))\
            .click()
            sleep(2)  
            self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
            target_followers = self._get_names()
            sleep(2)
            commons = self.get_common_names(target_followers,i)
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
        sleep(2)
        sugs = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul') 
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(4)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
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
my_bot.get_target_accounts_followers('ekinbayrakk/smdbcr')
#my_bot.get_unfollowers()
