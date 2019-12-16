from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import pickle
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, ElementClickInterceptedException,NoSuchElementException
import pandas as pd
import json
from datetime import datetime

class Alert():
    def __init__(self):
        pass
    def __repr__(self):
        return str(self)
    def __str__(self):
        return str(type(self))+ '\n'+ str(self.__dict__)

class Menu():
    def __init__(self):
        pass
    def __repr__(self):
        return str(self)
    def __str__(self):
        return str(type(self))+ '\n'+ str(self.__dict__)

class Content():
    def __init__(self):
        pass
    def __repr__(self):
        return str(self)
    def __str__(self):
        return str(type(self))+ '\n'+ str(self.__dict__)

class Funcs():
    def click_when_exists(self, element,by='css_selector'):
        if by == 'css_selector':
            element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
        elif by == 'xpath':
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))
        time.sleep(.25)
        element.click()

    def click_when_exists_2(self,element,by='css_selector'):
        tries = 0
        while tries < 10:
            try:
                tries = tries + 1
                self.click_when_exists(element,by)
                break
            except Exception as e:
                if type(e) == ElementClickInterceptedException:
                    continue
                else:
                    raise e

class StoreMenu(Menu):
    def __init__(self):
        self.promo_selector = ''
        self.gold_sleector = ''
        self.silver_sleector = ''
        self.bronze_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div.tab-menu > div > a:nth-child(4)'

class StoreBronzePackContent(Content):
    def __init__(self):
        self.buy_bronze_pack_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div.ut-store-hub-view--content > div:nth-child(2) > div.purchasing > button.currency.call-to-action.coins'
        self.buy_premium_bronze_pack_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div.ut-store-hub-view--content > div:nth-child(2) > div.purchasing > button.currency.call-to-action.points.disabled'

class NavMenu(Menu):
    def __init__(self):
        self.home_selector = 'body > main > section > nav > button.ut-tab-bar-item.icon-home'
        self.squads_selector = ''
        self.squad_builder_challenges_selector = ''
        self.transfer_selector = 'body > main > section > nav > button.ut-tab-bar-item.icon-transfer'
        self.store_selector = 'body > main > section > nav > button.ut-tab-bar-item.icon-store'
        self.club_selector = ''
        self.leaderboards_selector = ''

class StoreHubContent(Content):
    def __init__(self):
        self.menu = StoreMenu()

class TransferListContent(Content):
    def __init__(self):
        self.clear_sold_button_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div > section:nth-child(1) > header > button'
        self.relist_all_button_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div > section:nth-child(2) > header > button'
        self.sold_items_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div > section:nth-child(1) > ul'
        self.unsold_items_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div > section:nth-child(2) > ul'
        self.available_items_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div > section:nth-child(3) > ul'
        self.active_transfers_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div > section:nth-child(4) > ul'

class TransferHubContent(Content):
    def __init__(self):
        self.transfer_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div.tile.has-separator.col-1-2.ut-tile-transfer-list'

class LoginContent(Content):
    def __init__(self):
        pass

class CardMenu(Content):
    def __init__(self):
        self.list_on_transfer_marker_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div > div > div.DetailPanel > div.ut-quick-list-panel-view > div.ut-button-group > button'
        self.compare_price_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div > div > div.DetailPanel > div.ut-button-group > button:nth-child(8)'
        self.send_to_club_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div > div > div.DetailPanel > div.ut-button-group > button:nth-child(5)'
#         self.go_back_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right'
        self.player_bio_selector ='body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div.ut-navigation-container-view--content > div > div.DetailPanel > div.ut-button-group > button.more'
        self.quick_sell_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div.ut-navigation-container-view--content > div > div.DetailPanel > div.ut-button-group > button:nth-child(9) > span.btn-text'
        self.send_to_transfer_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div > div > div.DetailPanel > div.ut-button-group > button:nth-child(7)'
        self.redeem_coins_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div > div > div.DetailPanel > div.ut-button-group > button:nth-child(2)'

class CheckPriceMenu(Content):
    def __init__(self):
        self.go_back_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right'
        self.card_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div.ut-navigation-container-view--content > section > div.paginated-item-list.ut-pinned-list > ul'
        self.go_back_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div.ut-navigation-bar-view.navbar-style-secondary > button'
        self.next_page_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div.ut-navigation-container-view--content > section > div.paginated-item-list.ut-pinned-list > div > button.flat.pagination.next'
        self.auction_price_xpath = './li/div/div[2]/div[2]'
        self.buy_now_price_xpath = './li/div/div[2]/div[3]'
        self.remaining_time_xpath = './li/div/div[2]/div[4]'

class ListCardMenu(CardMenu):
    def __init__(self):
        self.bid_input_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div > div > div.DetailPanel > div.ut-quick-list-panel-view > div.panelActions.open > div:nth-child(2) > div.ut-numeric-input-spinner-control > input'
        self.buy_now_input_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div > div > div.DetailPanel > div.ut-quick-list-panel-view > div.panelActions.open > div:nth-child(3) > div.ut-numeric-input-spinner-control > input'
        self.list_item_button_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section > div > div > div.DetailPanel > div.ut-quick-list-panel-view > div.panelActions.open > button'

class CardComparePriceMenu():
    def __init__(self):
        pass
class HomePageContent(Content):
    def __init__(self):
        self.unassigned_items_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > div.ut-unassigned-tile-view.tile.col-1-1'

class CardListOnTransferMarketMenu():
    def __init__(self):
        pass

class RelistAlert(Alert):
    def __init__(self):
        self.cancel_selector = 'body > div.ut-click-shield.showing > section > div > div > button:nth-child(1)'
        self.yes_selector = 'body > div.view-modal-container.form-modal > section > div > div > button:nth-child(2) > span.btn-text'

class BuyPackAlert(Alert):
    def __init__(self):
        self.ok_selector = 'body > div.view-modal-container.form-modal > section > div > div > button:nth-child(1) > span.btn-text'
        self.cancel_selector = 'body > div.ut-click-shield.showing > section > div > div > button:nth-child(2) > span.btn-text'

class QuickSellWithCountAlert(Alert):
    def __init__(self):
        self.quick_sell_selector = 'body > div.view-modal-container.form-modal > div > div.btn-container > button:nth-child(1)'
        self.cancel_selector = 'body > div.view-modal-container.form-modal > div > div.btn-container > button:nth-child(2)'

class QuickSellAlert(Alert):
    def __init__(self):
        self.quick_sell_selector = 'body > div.view-modal-container.form-modal > section > div > div > button:nth-child(1)'
        self.cancel_selector = 'body > div.view-modal-container.form-modal > section > div > div > button:nth-child(2)'

class PackOpenContent(Content):
    def __init__(self):
        self.new_cards_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-unassigned-view.ui-layout-left > section:nth-child(1) > ul'
        self.duplicate_cards_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-unassigned-view.ui-layout-left > section:nth-child(2) > ul'
        self.is_duplicate_header_selector ='body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-unassigned-view.ui-layout-left > section > header'
class PlayerBioMenu(Content):
    def __init__(self):
        new_cards_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-unassigned-view.ui-layout-left > section:nth-child(1) > ul'
        duplicate_cards_list_selector = 'body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-unassigned-view.ui-layout-left > section:nth-child(2) > ul'


class FutBot(Funcs):
    def __init__(self, config_path='config.json'):
        with open(config_path) as file:
            self.config = json.loads(file.read())
        self.__dict__.update(**self.config)
        self.content = None
        self.card = None
        self.location = "home"
        self.nav = NavMenu()
        self.card_menu = CardMenu()
        self.active_transfers = 0
        self.sold_items = 0
        self.unsold_items = 0
        self.available_items = 0

    def create_driver(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : self.dl_path}
        chromeOptions.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome(executable_path = r"chromedriver.exe",options=chromeOptions) #we will need to ensure that a chromedriver.exe is in the app directory

        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        try:
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
        except:
            print("Could not load all cookies!")
    def go_to_home(self):
        self.click_when_exists(self.nav.home_selector)
        self.content = HomePageContent()

    def go_to_fut(self):
        self.driver.get(self.main_url)


    def enter_login_info(self):
        self.driver.find_element_by_id("email").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("btnLogin").click()

        self.driver.find_element_by_xpath(r'//*[@id="panel-tfa"]/div/div/div/div[3]').click()
        self.driver.find_element_by_id("btnSendCode").click()

        #Click on the login buton
        # self.click_when_exists('#Login > div > div > button.btn-standard.call-to-action')

    def go_to_transfer_hub(self):
        self.click_when_exists(self.nav.transfer_selector)
        self.content = TransferHubContent()

    def go_to_transfer_list(self):
        if type(self.content) != TransferListContent:
            if type(self.content) != TransferHubContent: self.go_to_transfer_hub()
            self.click_when_exists_2(self.content.transfer_list_selector)
            self.content = TransferListContent()

    def go_to_store(self):
        self.click_when_exists(self.nav.store_selector)
        self.content = StoreHubContent()
        time.sleep(1)

    def go_to_bronze_packs(self):
        if type(self.content) != StoreBronzePackContent:
            if type(self.content) != StoreHubContent: self.go_to_store()
            self.click_when_exists(self.content.menu.bronze_selector)
            self.content = StoreBronzePackContent()

    def login(self):
        self.go_to_home()
        self.enter_login_info()

    def clear_sold(self):
        assert type(self.content) == TransferListContent
        self.click_when_exists(self.content.clear_sold_button_selector)
        time.sleep(1)

    def relist_all(self):
        assert type(self.content) == TransferListContent
        self.click_when_exists(self.content.relist_all_button_selector)
        alert = RelistAlert()
        self.click_when_exists(alert.yes_selector)
        time.sleep(1)

    def buy_bronze_pack(self):
#         print(self.content)
        assert type(self.content) == StoreBronzePackContent
#         print(self.content)
        self.click_when_exists(self.content.buy_bronze_pack_selector)
        alert = BuyPackAlert()
        self.click_when_exists(alert.ok_selector)
        self.content = PackOpenContent()

    def get_card(self):
        self.card = Card()

    def check_bio(self):
        self.click_when_exists(self.card_menu.player_bio_selector)

    def make_card(self,element):
        self.card = None
        assert type(self.content) in [TransferListContent, PackOpenContent]
        card_list = element.find_elements_by_xpath('./li')
        self.card = Card(card_list[0],self)

    def set_transfer_counts(self):
        if not type(self.content) == TransferListContent: self.go_to_transfer_list()
        self.sold_items = self.get_list_count(self.content.sold_items_list_selector)
        self.unsold_items = self.get_list_count(self.content.unsold_items_list_selector)
        self.available_items = self.get_list_count(self.content.available_items_list_selector)
        self.active_transfers = self.get_list_count(self.content.active_transfers_list_selector)

    def get_list_count(self,css_selector):
        element = self.driver.find_element_by_css_selector(css_selector)
        count = len(element.find_elements_by_xpath('./li'))
        return count

    def manage_tranfers(self):
        self.set_transfer_counts()
        if self.sold_items > 0: self.clear_sold()
        if self.unsold_items > 0: self.relist_all()
        while self.available_items > 0:
            self.card = None
            cards_list = self.driver.find_element_by_css_selector(self.content.available_items_list_selector)
            self.make_card(cards_list)
            self.card.auction_card()
        if self.active_transfers < 90:
            self.get_more_cards()
        else:
            time.sleep(30)

    def manage_pack_opening(self):
        self.go_to_home()
        time.sleep(3)
        self.click_when_exists(self.content.unassigned_items_selector)
        time.sleep(3)
        self.content=PackOpenContent()
        new_cards_list = self.driver.find_element_by_css_selector(self.content.new_cards_list_selector)
#         try:
#             duplicate_cards_list = self.driver.find_element_by_css_selector(self.content.duplicate_cards_list_selector)
#             new_cards_list = self.driver.find_element_by_css_selector(self.content.new_cards_list_selector)
#             number_of_duplicates = len(self.driver.find_elements_by_xpath('./li'))
#             count = 0
#             while count < number_of_duplicates:
#                 count = count + 1
#                 duplicate_cards_list = self.driver.find_element_by_css_selector(self.content.duplicate_cards_list_selector)
#                 self.card = None
#                 self.make_card(duplicate_cards_list)
#                 self.card.new_from_pack_main()
#                 time.sleep(.75)
#         except NoSuchElementException:
#             pass
        number_of_new_cards = len(new_cards_list.find_elements_by_xpath('./li'))
        count = 0
        while count < number_of_new_cards:
            new_cards_list = self.driver.find_element_by_css_selector(self.content.new_cards_list_selector)
            self.card = None
            self.make_card(new_cards_list)
            self.card.new_from_pack_main()
            time.sleep(.75)


    def get_more_cards(self):
        self.go_to_bronze_packs()
        time.sleep(1)
        self.buy_bronze_pack()
        time.sleep(10)
        self.manage_pack_opening()

    def run(self):
        self.content=None
        count = 0
        max_count = 1000
        while count < max_count:
            try:
                self.content=None
                self.card_menu = CardMenu()
                self.manage_tranfers()
            except Exception as e:
                count = count +1
                print(e)

    def start(self):
        self.create_driver()
        self.go_to_fut()
        self.enter_login_info()
        input('Hit Enter Once you have completed the login process!')

    def main(self):
        self.start()
        self.run()


def update_scraper_dict(config_path,driver, content):
    self = FutBot(config_path)
    self.driver = driver
    self.content = content
    self.wait = WebDriverWait(driver,5)
    return self
# self = FutBot()
# self.create_driver()
# self.go_to_home()
# self.enter_login_info()
if 'bot' in locals():
    bot = update_scraper_dict('config.json',bot.driver, bot.content)

class Card(Funcs):
    def __init__(self, element,parent):
        element.click()
        time.sleep(1)
        self.element = element
        self.parent = parent
        self.driver = element.parent
        self.wait = WebDriverWait(self.driver, 5)
        self.pull_state_from_parent()
        self.df = pd.DataFrame()

        self.name = ''
        self.ovr = ''
        self.league = ''
        self.team = ''
        self.card_type = ''
        self.check_duplicate()

    def check_duplicate(self):
        try:
            self.is_duplicate = self.driver.find_element_by_css_selector(self.parent.content.is_duplicate_header_selector)\
                .text.strip() == 'DUPLICATES\nSend to Transfer List'
        except:
            self.is_duplicate = False

    def push_state_to_parent(self):
        self.parent.card_menu = self.card_menu
        self.parent.content = self.content
        self.parent.wait = self.wait
        self.parent.driver = self.driver

    def pull_state_from_parent(self):
        self.card_menu = self.parent.card_menu
        self.content = self.parent.content
        self.driver = self.parent.driver
        self.wait = self.parent.wait

    def check_price(self):
        assert type(self.card_menu) == CardMenu
#         assert type(self.content) == TransferListContent
        bid_prices = []
        buy_now_prices = []
        remaining_time = []
        self.element.click()
        time.sleep(.5)
        self.click_when_exists(self.card_menu.compare_price_selector)
        time.sleep(.5)
        self.card_menu = CheckPriceMenu()
        self.list_price = None
        max_pages = 6
        page=0

        while True:
            try:
                page = page + 1
                if page > max_pages:
                    raise TimeoutException
                auctions_list = self.driver.find_element_by_css_selector(self.card_menu.card_list_selector)
                #get bid prices
                elements = auctions_list.find_elements_by_xpath(self.card_menu.auction_price_xpath)
                bids = [(int(element.text.split('\n')[1].replace(',',''))) for element in elements]
                bid_prices = bid_prices + bids
                #get buy now prices
                elements = auctions_list.find_elements_by_xpath(self.card_menu.buy_now_price_xpath)
                bids = [(int(element.text.split('\n')[1].replace(',',''))) for element in elements]
                buy_now_prices = buy_now_prices + bids
                #get_remaining_times
                auctions_list = self.driver.find_element_by_css_selector(self.card_menu.card_list_selector)
                elements = auctions_list.find_elements_by_xpath(self.card_menu.remaining_time_xpath)
                times = [element.text.split('\n')[1] for element in elements]
                remaining_time = remaining_time + times
                #go to next page
                self.click_when_exists(self.card_menu.next_page_selector)
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.card_menu.next_page_selector)))
                time.sleep(.5)
            except (TimeoutException,ElementNotInteractableException) as e:
                self.click_when_exists(self.card_menu.go_back_selector)
                break
        self.card_menu = CardMenu()
        self.auction_count = len(bid_prices)
#         print(f'collected {len(bid_prices)} bid_prices')
#         print(f'collected {len(buy_now_prices)} buy_now_prices')
#         print(f'collected {len(remaining_time)} remaining_time')

        self.df['bid_price'] = bid_prices
        self.df['buy_now_price'] = buy_now_prices
        self.df['remaining_time'] = remaining_time

        print(f"Collected {self.auction_count} prices")

        self.card_menu = CardMenu()
        self.content = TransferListContent()
        self.push_state_to_parent()

    def get_post_price(self):
        agg_dict = {'bid_price': 'count',
            'remaining_time': ['max','min']
           }
        lowest = self.df.buy_now_price.min()
        count_lowest = self.df[self.df.buy_now_price == lowest].shape[0]
        self.list_price = self.df.nsmallest(3,'buy_now_price').max()['buy_now_price']

    def post_card(self):
        assert type(self.card_menu) == CardMenu
        assert self.list_price != None
        self.click_when_exists(self.card_menu.list_on_transfer_marker_selector)
        self.card_menu = ListCardMenu()
        time.sleep(.3)
        #fill in start price
        element = self.driver.find_element_by_css_selector(self.card_menu.bid_input_selector)
        element.click()
        time.sleep(.1)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(self.list_price)
        #fill in bid_price
        element = self.driver.find_element_by_css_selector(self.card_menu.buy_now_input_selector)
        element.click()
        time.sleep(.1)
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(self.list_price)
        element.send_keys(Keys.TAB)
        time.sleep(.1)
        #Press Post
        self.driver.find_element_by_css_selector(self.card_menu.list_item_button_selector).click()
        time.sleep(2)

    def get_card_type(self):
        self.card_type = self.element.find_element_by_xpath('div/div[1]/div[1]').get_attribute('class')
#         self.click_when_exists(self.card_menu.player_bio_selector)

    def get_card_name(self):
        self.card_name = self.element.find_element_by_xpath('./div/div[1]/div[2]').text

    def quick_sell_card(self):
        self.click_when_exists(self.card_menu.quick_sell_selector)
        self.alert = QuickSellAlert()
        try:
            self.click_when_exists(self.alert.quick_sell_selector)
        except TimeoutException:
            del(self.alert)
        self.alert = QuickSellWithCountAlert()
        self.click_when_exists(self.alert.quick_sell_selector)

    def send_to_club(self):
        self.click_when_exists(self.card_menu.send_to_club_selector)

    def send_to_transfer_list(self):
        self.click_when_exists(self.card_menu.send_to_transfer_list_selector)

    def redeem_card(self):
        self.click_when_exists(self.card_menu.redeem_coins_selector)

    def auction_card(self,minimum=False):
        if not minimum: self.check_price()
        if not minimum: self.get_post_price()
        if minimum: self.list_price = 200
        print(self.list_price)
        self.post_card()

    def sort_card(self):
        sell_types = ['small player item common ut-item-loaded','small consumable item rare contracts',
                      'small player item rare ut-item-loaded','small consumable item rare']
        quicksell_types = ['small consumable item common contracts']
        club_types = ['small staff item common','small badge item common','small kit item common',
                      'small ball item common','small consumable item common','small staff item rare',
                     'small badge item rare','small manager staff item common ut-item-loaded']
        redeem_types = ['small misc item common']
        if self.card_type in sell_types:
            self.send_to_transfer_list()
        elif self.card_type in quicksell_types:
            self.quick_sell_card()
        elif self.card_type in club_types and not self.is_duplicate:
            self.send_to_club()
        elif self.card_type in club_types and self.is_duplicate:
            self.quick_sell_card()
        elif self.card_type in redeem_types:
            self.redeem_card()
        else:
            print(f"must add type: {self.card_type}" )

    def new_from_pack_main(self):
        self.get_card_type()
        self.get_card_name()
        print(self.card_type)
        print(self.is_duplicate)
        self.sort_card()
        time.sleep(2)


# def update_card(old_card):
#     card = Card(old_card.element, old_card.parent)
#     card.df = old_card.df
#     return self
# # self = FutBot()
# # self.create_driver()
# # self.go_to_home()
# # self.enter_login_info()
# self = update_card(self)

if __name__=='__main__':
    bot=FutBot()
    bot.start()
    bot.run()
