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
            self.driver.get('https://www.tradingview.com/symbols/DJ-DJI/')
            time.sleep(5)
            dji_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]/span')
            dji_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[1]')
            dji_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[2]')
            self.dji = {'index_name': "道瓊斯工業平均指數",'dji' : dji_index.text, 'dji_change' : dji_change.text, 'dji_percent' : dji_change_percent.text}
            return 0
        except:
            print("dji is not successfully scrapped")
            return 1

    def get_hsi(self):
        try:
            self.driver.get('https://www.tradingview.com/symbols/HSI-HSI/')
            time.sleep(5)
            hsi_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]')
            hsi_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[1]')
            hsi_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[2]')
            self.hsi = {'index_name' : "恒生指數",'hsi' : hsi_index.text, 'hsi_change' : hsi_change.text, 'hsi_percent' : hsi_change_percent.text}  
            return 0   
        except:
            print("hsi is not successfully scrapped")
            return 1   

    def get_gold(self):
            try:
                self.driver.get('https://www.tradingview.com/symbols/COMEX-GC1!/')
                time.sleep(5)
                gold_index = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]')
                gold_change = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[1]')
                gold_change_percent = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/header/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[2]')
                self.gold = {"index_name":"倫敦金",'gold' : gold_index.text, 'gold_change' : gold_change.text, 'gold_percent' : gold_change_percent.text}
                return 0
            except:
                print("gold is not successfully scrapped") 
                return 1

    def close(self):
        self.driver.close()


