import scrapy
import logging
from scrapy.http.request import Request
from scrapy.selector import Selector
from ..items import SampleItem
# https://ibank.klikbca.com/accountstmt.do?value(actions)=acctstmtview
#https://ibank.klikbca.com/authentication.do?value(actions)=welcome 
#https://ibank.klikbca.com/authentication.do?value(actions)=logout
class LoginSpider(scrapy.Spider):
    name = 'bank'
    start_urls = ['https://ibank.klikbca.com/login.jsp']
 
 
    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                    'value(user_id)': 'NINGRUMF0212',
                    'value(pswd)': '621974'
            },
            callback=self.authentication_failed
        )

    # def after_login(self, response):
    #     if authentication_failed(response):
    #         self.logger.error("Login failed")
    
    def parse_Page(self, response):
        # gagal = 'iso logout'
        # hxs = Selector(response)    
        # hxs.xpath("//a[@href=\"account_information_menu.htm\"]")
        # print('iso pindah halaman 1')
        # hxs.xpath("//a[@onclick=\"javascript:goToPage('accountstmt.do?value(actions)=acct_stmt');return false;\"]")
        # print('iso pindah halaman 2')
        # hxs.xpath('/html/body/table[3]/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/input')
        # print('iso milih radio button')
        # hxs.xpath('/html/body/table[4]/tbody/tr[2]/td/input[1]')
        # print('iso klik button nampilno datane')
        cek = response.xpath('//font/text()').extract()
        print(cek)
        
        
        data={
                    'value(D1)': '0',
                    'value(r1)': '2',
                    'value(x)': '1',
                    'value(fDt)': '0107',
                    'value(tDt)': '3107',
                    'value(submit1)': 'View Account Statemen',
            }
        url="https://ibank.klikbca.com/accountstmt.do?value(actions)=acctstmtview"
        yield scrapy.FormRequest(
            url,
            formdata= data,
            callback=self.get_data
        )
    
    def get_data(self, response):
        item = SampleItem()
        item['name'] = response.xpath('.//tr[1]/.//tr[3]//td[3]/font/text()').extract_first().encode('utf-8')
        item['periode'] = response.xpath('.//tr[1]/.//tr[4]//td[3]/font/text()').extract_first().encode('utf-8')
        item['kredit'] = response.xpath('.//tr[3]/.//tr[3]//td[3]/font/text()').extract_first().encode('utf-8')
        item['debit'] = response.xpath('.//tr[3]/.//tr[4]//td[3]/font/text()').extract_first().encode('utf-8')
        item['saldo'] = response.xpath('.//tr[3]/.//tr[5]//td[3]/font/text()').extract_first().encode('utf-8')
        yield item
        cek = response.xpath('//font/text()').extract()
        print(cek)
        data={      'value(actions)': 'logout',
                    'value(user_id)': 'NINGRUMF0212',
                    'value(pswd)': '621974'
            }
        url="https://ibank.klikbca.com/authentication.do?value(actions)=logout"
        yield scrapy.FormRequest(
            url,
            formdata= data,
            callback=self.logout
        )
        # logout
        # hxs.xpath('//*[@id="gotohome"]/font/b/a')
        # return Request(callback=self.logout)
    def logout(self, response):
        metu = 'iso metu'
        print(metu)
    def authentication_failed(self, response):
        if "Silakan mengisi User ID anda/Please input your User ID" in response.body:
            print("Login failed")
            return
        elif "Silakan mengisi PIN anda/Please input your PIN" in response.body:
            print("Login failed")
            return
        else:
            # cek = response.xpath('//font/text()').extract()
            # print(cek)
            data={  
                    'value(actions)': 'acct_stmt',
                    'value(user_id)': 'NINGRUMF0212',
                    'value(pswd)': '621974'
            }
            DEFAULT_REQUEST_HEADERS = {
                                            'Referer': 'https://ibank.klikbca.com/authentication.do' 
                                        }
            url="https://ibank.klikbca.com/accountstmt.do?value(actions)=acctstmt"
            yield scrapy.FormRequest(
            url,
            formdata= data,
            callback=self.parse_Page
        )
            # return Request(url="https://ibank.klikbca.com/accountstmt.do?value(actions)=acctstmtview",
            #                 formdata = data,
            #                 # headers=DEFAULT_REQUEST_HEADERS ,
            #                 callback=self.parse_Page)