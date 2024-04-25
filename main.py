from time import sleep

from selenium import webdriver
# from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# options.add_argument('-headless')


# constants

SITE = r"https://neal.fun/infinite-craft/"


class Asphodel:

    def __init__(self) -> None:
        self.mixes = set()
        
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(0.5)
        
    def __get_items(self) -> None:
        self.items = self.driver.find_elements(By.CSS_SELECTOR, 'div.items-inner div.item')
        
    def open_site(self) -> None:
        self.driver.get(SITE)
        
        # get element center
        self.center = self.driver.find_element(By.CLASS_NAME, 'container')
        # get the clear button
        self.clear = self.driver.find_element(By.CLASS_NAME, 'clear')
        # get search that can be mixed
        self.search = self.driver.find_element(By.CLASS_NAME, 'sidebar-input')
        
    def drag_item(self, item) -> None: # this still isn't working when an item is out of the viewport
        while True:
            try:
                ActionChains(self.driver)\
                    .drag_and_drop(item, self.center)\
                    .perform()
                break
            except:
                ActionChains(self.driver)\
                    .send_keys_to_element(self.search, item.text[2:].strip())\
                    .perform()
            finally:
                self.search.clear()
            
    def gen_stack(self) -> list[tuple]:
        self.__get_items()
        new_stack = list()
        
        for i in range(len(self.items)):
            for j in range(i, len(self.items)):
                mix = (self.items[i], self.items[j])
                if mix not in self.mixes:
                    self.mixes.add(mix)
                    new_stack.append(mix)
                
        return new_stack  
        
    def main(self) -> None:
        self.open_site()
        
        while True:
            stack = self.gen_stack()
            
            if not stack:
                break
            
            print(f'current stack has {len(stack)} mixes to try!')
            
            while stack:
                items = stack.pop()
                print(f'Mixing {items[0].text} and {items[1].text}')
                for item in items:
                    self.drag_item(item)
                self.clear.click()
            print(f'Currently have tried {len(self.mixes)} mixes!')
            
        print()
        print(f'Tried {len(self.mixes)} diffrent combos!')
        print(f'found {len(self.items)} items!')
        
        
if __name__ == '__main__':
    dell = Asphodel()
    dell.main()
