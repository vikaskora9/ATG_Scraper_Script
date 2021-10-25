# importing sub-modules
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Defining empty Dictionary
Detail = dict()

driver = webdriver.Edge('C:/Users/vikas/Desktop/TANN_MANN/edgedriver_win64/msedgedriver')  # creating webdriver object
# Targetting Careerguide website
driver.get('https://www.careerguide.com/career-options')
container = driver.find_elements_by_class_name('col-md-4')
for i in range(len(container)):
    Sub_cate = []
    try:
        Category = container[i].find_element_by_tag_name('h2')
        if Category.text == 'Institutes in India':
            continue
    except NoSuchElementException:
        break
    Sub_Category = container[i].find_elements_by_tag_name('li')
    for j in range(len(Sub_Category)):
        Sub_cate.append(Sub_Category[j].text)
    # adding both Category and sub-Category in a dictionary
    Detail[Category.text] = Sub_cate

ctr = 0
for k in Detail.keys():
    for l in Detail[k]:
        # Targetting linkedin websites for jobs searching
        driver.get('https://in.linkedin.com/jobs')
        # Searching for gathered Sub-categories
        driver.find_element_by_xpath('//*[@id="JOBS"]/section[1]/input').send_keys(str(l))
        driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section/div[2]/button[2]').click()
        position = driver.find_elements_by_class_name('base-search-card__title')
        loc = driver.find_elements_by_class_name('job-search-card__location')
        organization = driver.find_elements_by_class_name('base-search-card__subtitle')
        for _ in range(len(position)):
            ctr += 1
            print('Scraped Data Sr no. :- ' + str(ctr))
            print('------------------------------------------------------')
            print('Position :- ' + position[_].text)
            print('Organization :- ' + organization[_].text)
            try:
                print('Location :- ' + loc[_].text)
                print('------------------------------------------------------')
            except IndexError:
                print('Location :- Not Available')
                print('------------------------------------------------------')
driver.close()

