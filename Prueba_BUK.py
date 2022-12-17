#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# In[228]:


driver = webdriver.Chrome()


# In[229]:


driver.get('https://www.demoblaze.com/index.html')


# In[201]:


#sign in process
driver.find_element(By.ID, "signin2").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@onclick="register()"]//preceding-sibling::button').click()
time.sleep(1)
driver.find_element(By.ID, "signin2").click()
time.sleep(2)
driver.find_element(By.ID, "sign-username").send_keys("username_prueba5")
driver.find_element(By.ID, "sign-password").send_keys("password3")


# In[202]:


driver.find_element(By.XPATH, '//*[@onclick="register()"]').click()
time.sleep(1)
alert = driver.switch_to.alert.accept()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@onclick="register()"]//preceding-sibling::button').click()


# In[203]:


#log in process
driver.find_element(By.ID, "login2").click()
time.sleep(1)
driver.find_element(By.ID, "loginusername").clear()
driver.find_element(By.ID, "loginpassword").clear()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@onclick="logIn()"]//preceding-sibling::button').click()
time.sleep(1)
driver.find_element(By.ID, "login2").click()
time.sleep(1)


# In[204]:


driver.find_element(By.ID, "loginusername").send_keys("username_prueba5")
driver.find_element(By.ID, "loginpassword").send_keys("password3")


# In[205]:


driver.find_element(By.XPATH, '//*[@onclick="logIn()"]').click()
time.sleep(3)


# In[206]:


#alert = driver.switch_to.alert.accept()


# In[207]:


#Home button navbar
driver.find_element(By.XPATH, '//a[@class="nav-link" and @href="index.html"]').click()
time.sleep(1)


# In[208]:


#Contact button navbar
driver.find_element(By.XPATH, '//a[@class="nav-link" and @data-target="#exampleModal"]').click()
time.sleep(1)
driver.find_element(By.ID, "recipient-email").send_keys("prueba@bukprueba.cl")
driver.find_element(By.ID, "recipient-name").send_keys("Merlina Addams")
driver.find_element(By.ID, "message-text").send_keys("Hola, tengo información sobre el monstruo")


# In[209]:


driver.find_element(By.XPATH, '//*[@onclick="send()"]').click()
time.sleep(3)
alert = driver.switch_to.alert.accept()


# In[210]:


#About us navbar
driver.find_element(By.XPATH, '//*[@class="nav-link" and @data-target="#videoModal"]').click()


# In[211]:


driver.find_element(By.XPATH, '//*[@class="vjs-big-play-button"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//button[@class="vjs-play-control vjs-control vjs-button vjs-playing" and @title="Pause"]').click()


# In[212]:


driver.find_element(By.XPATH, '//div[@id="videoModal"]/child::div/child::div/child::div[3]/child::button').click()


# In[213]:


#Click on Cart navbar
driver.find_element(By.ID, "cartur").click()
time.sleep(1)


# In[214]:


#Click on Logo
driver.find_element(By.ID, "nava").click()


# In[215]:


#Click on Prev button carousel
driver.find_element(By.XPATH, '//*[@class="carousel-control-prev-icon"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="carousel-control-prev-icon"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="carousel-control-prev-icon"]').click()


# In[216]:


#Click on Next button carousel
driver.find_element(By.XPATH, '//*[@class="carousel-control-next-icon"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="carousel-control-next-icon"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="carousel-control-next-icon"]').click()


# In[217]:


#Testing Categories
driver.find_element(By.ID, "cat").click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@class="list-group"]//child::a[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@class="list-group"]//child::a[3]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@class="list-group"]//child::a[4]').click()
time.sleep(2)
driver.find_element(By.ID, "cat").click()


# In[218]:


#Scroll Down
driver.execute_script("window.scrollTo(0, 300)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(0.5)
driver.execute_script("window.scrollTo(0, 1080)")


# In[219]:


#Pressing Previous-Next buttons
driver.find_element(By.ID, "next2").click()
time.sleep(2)
driver.find_element(By.ID, "prev2").click()
time.sleep(2)


# In[220]:


#Clicking on a card img
driver.find_element(By.LINK_TEXT, value="Nokia lumia 1520").click()
time.sleep(2)
#driver.back()
driver.find_element(By.XPATH, '//*[@onclick="addToCart(2)"]').click()
time.sleep(2)
alert = driver.switch_to.alert.accept()


# In[221]:


#Go to Cart with a product
driver.find_element(By.ID, "cartur").click()
time.sleep(2)


# In[222]:


#Deleting a product on the list
driver.find_element(By.XPATH, '//*[@id="page-wrapper"]//child::div//child::div//child::div//child::table//child::tbody//child::tr//child::td[4]//child::a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//a[@class="nav-link" and @href="index.html"]').click()
time.sleep(2)


# In[232]:


#Adding a product again to complete the purchasing process
driver.find_element(By.LINK_TEXT, value="Nexus 6").click()
time.sleep(2)
#driver.back()
driver.find_element(By.XPATH, '//*[@onclick="addToCart(3)"]').click()
time.sleep(2)
alert = driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.ID, "cartur").click()


# In[233]:


#Complete the purchase process
driver.find_element(By.XPATH, '//*[@data-toggle="modal" and @data-target="#orderModal"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@id="name"]').clear()
driver.find_element(By.XPATH, '//input[@id="country"]').clear()
driver.find_element(By.XPATH, '//input[@id="city"]').clear()
driver.find_element(By.XPATH, '//input[@id="card"]').clear()
driver.find_element(By.XPATH, '//input[@id="month"]').clear()
driver.find_element(By.XPATH, '//input[@id="year"]').clear()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@id="name"]').send_keys("Matias Gonzalez")
driver.find_element(By.XPATH, '//input[@id="country"]').send_keys("Chile")
driver.find_element(By.XPATH, '//input[@id="city"]').send_keys("Santiago")
driver.find_element(By.XPATH, '//input[@id="card"]').send_keys("1234 5678 9101 1121")
driver.find_element(By.XPATH, '//input[@id="month"]').send_keys("12")
driver.find_element(By.XPATH, '//input[@id="year"]').send_keys("28")


# In[234]:


#Clicking the Purchase button
driver.find_element(By.XPATH, '//*[@onclick="purchaseOrder()"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[@class="confirm btn btn-lg btn-primary"]').click()
time.sleep(2)


# In[226]:


#LOG OUT
driver.find_element(By.ID, "logout2").click()
time.sleep(3)


# In[235]:


#FIN
driver.close()
