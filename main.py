from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"



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
        """
        This function opens the inf craft site, finds the center and clear elements
        """
        self.driver.get(SITE)
        
        # get element center
        self.center = self.driver.find_element(By.CLASS_NAME, 'container')
        # get the clear button
        self.clear = self.driver.find_element(By.CLASS_NAME, 'clear')
        
    def drag_item(self, item) -> None:
        """
        The `drag_item` function attempts to drag an item to a specific location on a webpage using
        ActionChains in Python, scrolling into view if necessary.
        
        :param item: The `item` parameter in the `drag_item` method is a web element that you
        want to drag and drop to a specific location on a web page.
        """
        while True:
            try:
                ActionChains(self.driver)\
                    .drag_and_drop(item, self.center)\
                    .perform()
                break
            except:
                self.driver.execute_script('arguments[0].scrollIntoView()', item)
            
    def gen_stack(self) -> list[tuple]:
        """
        This function generates a list of unique tuples by combining items from a given list.
        :return: A list of tuples is being returned.
        """
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
        """
        This function opens the site, generates a stack of items to mix, mixes the items, clears the mix,
        and keeps track of the number of mixes tried and items found, continuing until it has tried all combinations
        """
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
