"""
The script has created to search data in youtube.
The script takes first string from the given text and perform search in youtube.
After getting results, it iterates over all found videos, and get the names of videos,
which contains previously given text in it's title.
Loop continues while the count of found elements are less then 10.
At the end, found video titles' list returned.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import platform

# Element locators
class PageLocators:
    searchField     = (By.ID, 'search')
    searchButton    = (By.ID, 'search-icon-legacy')
    videoTitle      = '//a[contains(@title,"%s")]'

# This class contains methods for testing youtube
class TestYoutube():
    # Open driver and navigate to youtube
    def __init__(self):

        if (platform.system()) == "Windows":
            print(f'platform.system() = {platform.system()}')
            self.driver = webdriver.Chrome('chromedriver.exe')
        elif (platform.system()) == "Linux":
            print(f'platform.system() = {platform.system()}')
            self.driver = webdriver.Chrome('chromedriver')
        else:
            print(f'platform.system() = {platform.system()}, which is not supported by this script!')
            exit()
        self.driver.get('https://youtube.com')
        self.driver.maximize_window()

    # This function searches in the
    def test_youtube(self, searchText='Frank Sinatra'):
        # Helper elements
        collectedListElemCount  = 0
        elementsCount           = 0
        titleList               = []

        # Get first string from the given text
        splittedList = searchText.split(' ')
        print(splittedList)
        try:
            # If given string doesn't contain 2 substrings, exit the script
            if len(splittedList) == 1:
                raise Exception("Error: Please enter correct value for search, which contains 2 strings!")

            # Write in search field and click on Search button
            searchField = self.driver.find_element(*PageLocators.searchField)
            searchField.send_keys(splittedList[0])
            self.driver.find_element(*PageLocators.searchButton).click()

            # Iterate over found elements, while the count of elements is less then 10, which title contains given text
            while(collectedListElemCount < 10):
                # Get all the available elements, which title contains  given text
                elements = self.driver.find_elements_by_xpath(PageLocators.videoTitle%(searchText))

                # Get found elements count,
                # Run over the new found elements and fill titles' list
                currentListLength = len(elements)
                for i in range(elementsCount,currentListLength):
                    titleList.append(elements[i].get_attribute('title'))
                    collectedListElemCount += 1
                    if collectedListElemCount == 10:
                        break
                elementsCount = currentListLength
                self.driver.find_element_by_tag_name('html').send_keys(Keys.END)

            self.driver.close()
            return titleList
        except Exception as e:
            print(e)
            self.driver.close()

if __name__=='__main__':
    testYoutube = TestYoutube()
    print(testYoutube.test_youtube('John Lennon'))


