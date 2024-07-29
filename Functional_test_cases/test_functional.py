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

    @pytest.mark.home_page
    def test_add_to_cart(self, driver):
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

    @pytest.mark.home_page
    def test_cart_button_is_functioning(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        basket_element = driver.find_element(By.XPATH, "(// span[normalize-space() = 'Basket'])[1]")
        basket_element.click()
        confirmation = driver.find_element(By.CSS_SELECTOR, "div[class='a-row sc-your-amazon-cart-is-empty'] h2").text
        assert confirmation == "Your Amazon Cart is empty"

    @pytest.mark.home_page
    def test_remove_button_in_cart_working(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        search_input = driver.find_element(By.XPATH, "(// input[@ id='twotabsearchtextbox'])[1]")
        search_input.send_keys("JOxeDerm Body Care 2% Salicylic Acid Spray 150ml/ 5fl.oz")
        driver.find_element(By.XPATH, "(//input[@id='nav-search-submit-button'])[1]").click()
        product = driver.find_element(By.XPATH, "//div[@class='s-widget-container s-spacing-small "
                                                "s-widget-container-height-small celwidget slot=MAIN "
                                                "template=SEARCH_RESULTS widgetId=search-results_3']//h2["
                                                "@class='a-size-mini a-spacing-none a-color-base "
                                                "s-line-clamp-3']//span[1]")
        product.click()
        add_to_cart = driver.find_element(By.XPATH, "(//input[@id='add-to-cart-button'])[1]").click()
        basket = driver.find_element(By.XPATH, "(//a[@href='/cart?ref_=sw_gtc'])[1]")
        basket.click()
        delete_product = driver.find_element(By.XPATH, "(//input[@value='Delete'])[1]")
        delete_product.click()
        confirmation = driver.find_element(By.XPATH, "(//h1[normalize-space()='Your Amazon Cart is empty.'])[1]").text
        assert confirmation == "Your Amazon Cart is empty."

    @pytest.mark.home_page
    def test_product_reviews(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        search_input = driver.find_element(By.XPATH, "(// input[@ id='twotabsearchtextbox'])[1]")
        search_input.send_keys("JOxeDerm Body Care 2% Salicylic Acid Spray 150ml/ 5fl.oz")
        driver.find_element(By.XPATH, "(//input[@id='nav-search-submit-button'])[1]").click()
        product = driver.find_element(By.XPATH, "//div[@class='s-widget-container s-spacing-small "
                                                "s-widget-container-height-small celwidget slot=MAIN "
                                                "template=SEARCH_RESULTS widgetId=search-results_3']//h2["
                                                "@class='a-size-mini a-spacing-none a-color-base "
                                                "s-line-clamp-3']//span[1]")
        product.click()
        reviews = driver.find_element(By.XPATH, "(//span[@id='acrCustomerReviewText'])[1]")
        reviews.click()
        confirmation = driver.find_element(By.XPATH, "//h3[normalize-space()='Top reviews from United Kingdom']").text
        assert confirmation == "Top reviews from United Kingdom"

    @pytest.mark.actual
    @pytest.mark.home_page
    def test_website_footer(self, driver):
        driver.get("https://www.amazon.co.uk/")
        cookies = driver.find_element(By.ID, "sp-cc-accept").click()
        footer = driver.find_element(By.LINK_TEXT, "Gift Cards").click()
        confirmation = driver.find_element(By.CSS_SELECTOR, "div[class='a-column a-span12 aok-float-right "
                                                            "apb-browse-col-pad-left "
                                                            "apb-browse-two-col-center-margin-right'] div:nth-child("
                                                            "1) div:nth-child(1) div:nth-child(1) h1:nth-child(1)").text
        assert confirmation == "Gift Cards & Top Up"
