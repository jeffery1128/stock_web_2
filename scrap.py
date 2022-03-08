from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time




class scrapper:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  
        self.driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
        self.dji = {}
        self.hsi = {}
        self.gold = {}
        

    def get_dji(self):
        try:
            self.driver.get('https://www.tradingview.com/markets/indices/quotes-major/')
            dji_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]')
            dji_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]/span')
            dji_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[3]/span')
            self.dji = {'index_name': "道瓊斯工業平均指數",'dji' : dji_index.text, 'dji_change' : dji_change.text, 'dji_percent' : dji_change_percent.text}
            return 0
        except Exception as e:
            print("dji is not successfully scrapped")
            print(e)
            return 1

    def get_hsi(self):
        try:
            self.driver.get('https://www.tradingview.com/markets/indices/quotes-major/')
            hsi_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[13]/td[2]')
            hsi_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[13]/td[4]/span')
            hsi_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[13]/td[3]/span')
            self.hsi = {'index_name' : "恒生指數",'hsi' : hsi_index.text, 'hsi_change' : hsi_change.text, 'hsi_percent' : hsi_change_percent.text}  
            return 0   
        except Exception as e:
            print("hsi is not successfully scrapped")
            print(e)
            return 1   

    def get_gold(self):
            try:
                self.driver.get('https://www.tradingview.com/markets/futures/quotes-metals/')
                time.sleep(0.1)
                gold_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]')
                gold_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[4]/span')
                gold_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/span')
                self.gold = {"index_name":"倫敦金",'gold' : gold_index.text, 'gold_change' : gold_change.text, 'gold_percent' : gold_change_percent.text}
                return 0
            except Exception as e:
                print("gold is not successfully scrapped") 
                print(e)
                return 1

    def close(self):
        self.driver.close()


