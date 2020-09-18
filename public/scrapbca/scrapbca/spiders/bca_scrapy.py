# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy import Spider
# from scrapy.http import FormRequest
# from scrapy.selector import Selector
# from scrapy.utils.response import open_in_browser
# from ..items import SampleItem


# class QuotesSpider(scrapy.Spider):
#     name = "BCAtes"
#     start_urls = ['https://ibank.klikbca.com/authentication.do']
#     # login_url = 'https://ibank.klikbca.com/authentication.do'
    
#     def parse(self, response):
# #         token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
#         open_in_browser(response)
#         return FormRequest.from_response(response,
#                                             formdata={['value(pswd)': '621974',
#                                             'value(user_id)': 'NINGRUMF0212']
#                                              },callback=self.SCRAPE_DATA)
        


#     def SCRAPE_DATA(self, response):
#         # tables=[] 
            # hxs = Selector(response)    
            # hxs.xpath("//a[@href=\"account_information_menu.htm\"]")
            # print('iso pindah halaman 1')
            # hxs.xpath("//a[@onclick=\"javascript:goToPage('accountstmt.do?value(actions)=acct_stmt');return false;\"]")
            # print('iso pindah halaman 2')
            # hxs.xpath('/html/body/table[3]/tbody/tr[5]/td/table/tbody/tr[2]/td[1]/input')
            # print('iso milih radio button')
            # hxs.xpath('/html/body/table[4]/tbody/tr[2]/td/input[1]')
            # print('iso klik button nampilno datane')
#         item = SampleItem()
#         # item['name'] = response.xpath('html/body/table[3]/tbody/tr[1]/td/table/tbody/tr[3]/td[3]/font/text()').extract()
#         # item['periode'] = response.xpath('html/body/table[3]/tbody/tr[1]/td/table/tbody/tr[4]/td[3]/font/text()').extract()
#         # item['kredit'] = response.xpath('html/body/table[3]/tbody/tr[3]/td/table/tbody/tr[3]/td[3]/font/text()').extract()
#         # item['debit'] = response.xpath('html/body/table[3]/tbody/tr[3]/td/table/tbody/tr[4]/td[3]/font/text()').extract()
#         # item['saldo'] = response.xpath('html/body/table[3]/tbody/tr[3]/td/table/tbody/tr[5]/td[3]/font/text()').extract()
#         # item['saldo'] = hxs.xpath('//b/text()').getall()
#         # yield item
#         # for table in response.xpath('//table'):
#         item['name'] = response.xpath('//b/text()').getall()
#         yield item
#         # hxs.xpath('//*[@id="gotohome"]/font/b/a')
#         # print('iso logout')
#         # return

        