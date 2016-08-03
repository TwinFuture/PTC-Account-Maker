############## Copyright TwinFuture All Rights Reserved! ############
import time;
import os;

import selenium.webdriver.chrome.service as service;
from selenium import webdriver;
from selenium.common.exceptions import TimeoutException;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.keys import Keys;
print("Started...");

############### Change password to your liking.. ####################
##### You can change the email address if you have a catchall #######
## Using the email below is fine, do not add anything before the @ ##
password = "PasswordUni"; # Your desired password
email = "@uniquez-home.com"; #Only if you OWN a domain with a catchall
country = "GB"; # Your country code, Only suppors 2 characters!

#####################################################################
#######                                                       #######
####### DO NOT EDIT BELOW UNLESS YOU KNOW WHAT YOU ARE DOING! #######
#######                                                       #######
#####################################################################
# Get all the email usernames from emails.txt and store them inside an array
emails = [line.strip() for line in open('emails.txt')];
emails = [var for var in emails if var];
eCount = len(emails);
print("Started... Attempting to create "+ str(eCount) + " acounts");
curEmail = 0;

def launchChrome(curEmail) :
        if curEmail != eCount :
                # Load the chrome driver
                chromedriver = "./chromedriver/chromedriver.exe";
                os.environ["webdriver.chrome.driver"] = chromedriver;

                # Set chrome to incognito mode.
                chrome_options = webdriver.ChromeOptions();
                chrome_options.add_argument("--incognito");
                # Load chrome options!
                driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options);

                # Navigate to the signup page.
                driver.get('https://club.pokemon.com/uk/pokemon-trainer-club/sign-up/');

                timeout = 30; # seconds
                try:
                        element_present = EC.presence_of_element_located((By.ID, 'sign-up-theme'));
                        WebDriverWait(driver, timeout).until(element_present);
                        # print ("Page is ready! Submitting age verification");
                        signup(curEmail, driver);
                except TimeoutException:
                        if driver.current_url == "https://club.pokemon.com/uk/pokemon-trainer-club/sign-up/" :
                                time.sleep(1);
                                signup(curEmail, driver);
                        else :
                                print ("Loading took too much time! Trying again!");
                                driver.close();
                                driver.quit();
                                time.sleep(1);
                                launchChrome(curEmail);
        else :
                print("End OF LIST");
                print("FINISHED................................");
                driver.close();
                driver.quit();
                time.sleep(1);

def signup(curEmail, driver):
                time.sleep(2);
                driver.find_element(By.XPATH, '//input[@id="id_dob"]').click();
                driver.execute_script('document.getElementsByClassName("month")[0].style.display = "block";');
                driver.find_element(By.XPATH, '//select[@class="month"]/option[@value="4"]').click();
                driver.execute_script('document.getElementsByClassName("year")[0].style.display = "block";');
                driver.find_element(By.XPATH, '//select[@class="year"]/option[@value="1985"]').click();
                driver.find_element(By.XPATH, '//td/div[text()="25"]').click();
                driver.find_element(By.XPATH, '//button[@class="picker__button--clear"]').click();
                driver.execute_script('document.getElementsByName("country")[0].setAttribute("value", "'+country+'")');
                driver.execute_script('document.getElementsByName("country")[1].setAttribute("value", "'+country+'")');
                driver.find_element(By.XPATH, '//input[@value="Continue"]').submit();

                timeout = 30 # seconds
                try:
                        element_present = EC.presence_of_element_located((By.ID, 'user-signup-create-account-form'));
                        WebDriverWait(driver, timeout).until(element_present)
                        # print ("Page is ready! Imputting User Details!");
                        driver.find_element_by_id("id_username").send_keys(emails[curEmail]);
                        driver.find_element_by_id("id_password").send_keys(password);
                        driver.find_element_by_id("id_confirm_password").send_keys(password);
                        driver.find_element_by_id("id_email").send_keys(emails[curEmail]+email);
                        driver.find_element_by_id("id_confirm_email").send_keys(emails[curEmail]+email);
                        driver.find_element_by_id("id_screen_name").send_keys(emails[curEmail]);
                        driver.find_element_by_id("id_terms").click();
                        driver.find_element(By.XPATH, '//input[@value=" Continue"]').submit();
                        try:
                                element_present = EC.presence_of_element_located((By.ID, 'gus-wrapper'));
                                WebDriverWait(driver, timeout).until(element_present);
                                if driver.current_url == "https://club.pokemon.com/uk/pokemon-trainer-club/forgot-password?msg=users.email.exists" :
                                        print ("This account already exists! "+emails[curEmail]+ ". Moving on");
                                        curEmail = curEmail + 1;
                                        driver.close();
                                        driver.quit();
                                        time.sleep(1);
                                        launchChrome(curEmail);
                                else :
                                        print ("Account Created: "+emails[curEmail]+email);
                                        # print("Creating next account in your list!");
                                        ## Save made accounts to a file
                                        with open('created.txt', 'a') as file:
                                            file.write("\n" + emails[curEmail]);

                                        curEmail = curEmail + 1;
                                        driver.close();
                                        driver.quit();
                                        time.sleep(1);
                                        launchChrome(curEmail);
                        except TimeoutException:
                                        print ("Opps, the details didn't quiet go through, trying again!");
                                        driver.close();
                                        driver.quit();
                                        time.sleep(1);
                                        launchChrome(curEmail);
                        
                except TimeoutException:
                        print ("Opps, the age verification didn't go through properly, trying again!");
                        driver.close();
                        driver.quit();
                        time.sleep(1);
                        launchChrome(curEmail);

launchChrome(curEmail);
