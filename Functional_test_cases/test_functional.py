import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_Functional:

    @pytest.mark.home_page
    def test_home_page_loading_succesfully(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        logo = driver.find_element(By.XPATH, "(//a[@id='nav-logo-sprites'])[1]")
        assert logo.is_displayed()

    @pytest.mark.home_page
    def test_sign_in_button(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        hello_sign_in = driver.find_element(By.XPATH, "(//span[normalize-space()='Account & Lists'])[1]")
        sign_in = driver.find_element(By.XPATH, "//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner']["
                                                "normalize-space()='Sign in']")

        act = ActionChains(driver)
        act.move_to_element(hello_sign_in).move_to_element(sign_in).click().perform()
        sign_in_confirmation = driver.find_element(By.XPATH, "//h1[normalize-space()='Sign in']")
        assert sign_in_confirmation.is_displayed()

    @pytest.mark.home_page
    def test_sign_up_button(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        hello_sign_in = driver.find_element(By.XPATH, "(//span[normalize-space()='Account & Lists'])[1]")
        new_customer = driver.find_element(By.XPATH, "(//a[@class='nav-a'][normalize-space()='Start here.'])[1]")

        act = ActionChains(driver)
        act.move_to_element(hello_sign_in).move_to_element(new_customer).click().perform()
        sign_up_confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Create account'])[1]")
        assert sign_up_confirmation.is_displayed()

    @pytest.mark.home_page
    def test_bestseller_category_display(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        best_seller_element = driver.find_element(By.XPATH,
                                                  "(//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers'])[1]")
        assert best_seller_element.is_displayed()

    @pytest.mark.home_page
    def test_product_details_page_is_opening(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        search_input = driver.find_element(By.XPATH, "(// input[@ id='twotabsearchtextbox'])[1]")
        search_input.send_keys("VETRA Volleyball Soft Touch Volley "
                               "Ball Official Size 5 Outdoor Indoor Beach Gym Game Ball New")
        driver.find_element(By.XPATH, "(//input[@id='nav-search-submit-button'])[1]").click()
        ball_element = driver.find_element(By.XPATH, "(//span[normalize-space()='VETRA Volleyball Soft Touch Volley "
                                                     "Ball Official Size 5 Outdoor Indoor Beach Gym Game Ball New'])["
                                                     "1]")
        ball_element.click()
        ball_page_details = driver.find_element(By.XPATH, "(//span[@id='productTitle'])[1]").text
        assert ball_page_details == ("VETRA Volleyball Soft Touch Volley Ball Official Size 5 Outdoor Indoor Beach Gym "
                                     "Game Ball New")

    @pytest.mark.actual
    @pytest.mark.home_page
    def test_product_details_page_is_opening(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        search_input = driver.find_element(By.XPATH, "(// input[@ id='twotabsearchtextbox'])[1]")
        search_input.send_keys("JZK 2 Dummy Fake Surveillance Security CCTV Dome Camera With LED Blinking Real "
                               "imitation for Home Security, White")
        driver.find_element(By.XPATH, "(//input[@id='nav-search-submit-button'])[1]").click()
        camera_element = driver.find_element(By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal']["
                                                       "contains(text(),'2 Dummy Fake Surveillance Security CCTV Dome"
                                                       " Camer')])[1]")
        camera_element.click()
        add_to_basket = driver.find_element(By.ID, "add-to-cart-button")
        add_to_basket.click()
        basket = driver.find_element(By.XPATH, "(//a[@href='/cart?ref_=sw_gtc'])[1]").click()
        time.sleep(2)
        total_basket = driver.find_element(By.XPATH, "(//span[@id='sc-subtotal-label-activecart'])[1]")
        assert total_basket.text == "Subtotal (1 item):"
