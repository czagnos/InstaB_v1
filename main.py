from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class InstaBot:
    temp = None
    def __init__(self, username, pw):
    
        self.driver = webdriver.Chrome("C:/Users/czagnos/hello/InstaB_v1/chromedriver.exe")
        self.username = username
        self.pw = pw
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

    def get_target_hashtags(self,hashtags):
        hashtags_arr = hashtags.split('/')
        hashtags_length = len(hashtags_arr)
        
        for j in range(hashtags_length):     
            target_hashtags_sharp = self.find_correct_hashtags(hashtags_arr[j],'us')
            target_hashtags       = self.find_correct_hashtags(hashtags_arr[j],'us')
            target_hashtags_len = len(target_hashtags)
            self.__init__(self.username,self.pw)            
            for i in range(target_hashtags_len):
                sleep(2)  
                target_hashtags_sharp[i] = '#' + target_hashtags_sharp[i]
                self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]")\
                .send_keys(target_hashtags_sharp[i])
                sleep(2)  
                self.driver.find_element_by_xpath("//a[contains(@href,'/explore/tags/{}/')]".format(target_hashtags[i]))\
                .click()
                sleep(5)
                self.driver.refresh()



    def find_correct_hashtags(self,hashtag,country): #TODO open tagsfinder link according to country
        self.driver.get("https://www.tagsfinder.com/en-us/similar/")
        self.driver.find_element_by_xpath("//input[@name=\"hashtag\"]")\
            .clear()
        self.driver.find_element_by_xpath("//input[@name=\"hashtag\"]")\
            .send_keys(hashtag)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Search!')]")\
            .click()
        sleep(3)
        hashtagss = self.driver.find_elements_by_xpath("//div[@id=\"hashtagy\"]")
        tempo = hashtagss[0].text.replace(' #',' ').replace('#',' ').split()
        return tempo     

    def dm_selected_accounts(self,accounts,text):
        accounts_list = accounts.split('/')
        accounts_len = len(accounts_list)
        self.driver.find_element_by_xpath("//a[contains(@href,'/direct/inbox/')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Send Message')]")\
            .click()
        for i in range(accounts_len):
            self.driver.find_element_by_xpath("//input[@placeholder=\"Search...\"]")\
                .send_keys(accounts_list[i])
            for j  in range(0,5):     
                self.driver.switch_to.active_element.send_keys(Keys.TAB)
                sleep(1)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER) 
 
            self.driver.find_element_by_class_name('rIacr')\
            .click()
            sleep(3)
            self.driver.find_element_by_xpath("//textarea[contains(@placeholder,'Message...')]")\
            .send_keys(text)
            sleep(2)  
            self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]")\
            .click()
            

    def search_bio(self,text,min_follower):
        self.driver.get("https://www.searchmy.bio/")
        self.driver.find_element_by_xpath("//input[@placeholder=\"Keywords to search user bios\"]")\
                .send_keys(text)
        sleep(1)

        
        self.driver.find_element_by_xpath("//span[contains(text(), 'Followers:')]")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//input[@ng-model=\"min\"]")\
                .send_keys(min_follower)
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Apply')]")\
            .click()    
        sleep(1)        
        self.driver.find_element_by_xpath("//button[contains(text(), 'Search')]")\
            .click()

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        box = self.driver.find_element_by_class_name('search-results')
        links = box.find_elements_by_class_name('search-result-username')
        names = [name.text for name in links ]
        return print(names)

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

my_bot = InstaBot('zagnoscan', '14447403096')
my_bot.search_bio('thought leader',1000)
#my_bot.dm_selected_accounts('isilayko/smdbcr','bu mesaj botla atılmıştır. abilere selam çatışmaya devam.')
#my_bot.get_target_hashtags('milano')
#my_bot.get_target_accounts_followers('smdbcr/ekinbayrakk/zagnoscan')
#my_bot.get_unfollowers()
