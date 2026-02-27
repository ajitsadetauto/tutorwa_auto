import os
import re
import time
from playwright.sync_api import Page, Locator, expect
from datetime import datetime, timedelta

class PageObjects:
    def __init__(self, page: Page):
        self.page = page



    def verify_success_message(self, xpath:str, exp:str):
        success_message = self.page.locator(xpath)
        success_message.wait_for(state="visible", timeout=5000)
        text = success_message.inner_text()
        assert text == exp, f"[FAIL] Unexpected message: {text}"
        print(f"[PASS] Success message verified: {text}")



    def create_account_fun(self, email:str, password:str):
        self.page.get_by_role("link", name="Sign up").click()
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.locator('//input[@id="password"]').fill(password)
        self.page.locator('//input[@id="confirmPassword"]').fill(password)
        self.page.get_by_role("button", name="Create Account").click()
        self.verify_success_message("//div[text()='Email already in use']","Email already in use")


    def login_function(self, email:str, password:str):
        signIn=self.page.get_by_role("heading", name="Sign In", exact=True)
        expect(signIn).to_be_visible()
        print("Login page displayed")
        self.page.get_by_role("link", name="Google Signin/Signup Button").click()
        self.page.get_by_role("textbox", name="Email or phone").fill(email)
        self.page.get_by_role("button", name="Next").click()
        self.page.get_by_role("textbox", name="Enter your password").fill(password)
        self.page.get_by_text("Show password").click()
        self.page.get_by_role("button", name="Next").click()
        time.sleep(18)
        expect(self.page).to_have_url("https://devapp.tutorwand.com/teacher/dashboard")
        


    def assign_fastrack_test(self):
        #Click on Create button.
        self.page.locator('//span[normalize-space()="Create"]').click()
        #wait for 5 seconds
        self.page.locator('(//button[@type="primary"][normalize-space()="Create"])[2]').click()
        self.page.get_by_role("textbox", name="Assessment Name").fill("Test Fastrack data")
        print('Test Fastrack data add in assessment name field')
        self.page.get_by_role("button", name="Select board").first.click()
        self.page.get_by_role("option", name="CBSE").click()
        print('CBSE is selected from Select board')
        self.page.get_by_role("button", name="Select board CBSE").nth(1).click()
        self.page.get_by_role("option", name="10").click()
        print('10th selected from class')
        self.page.get_by_role("button", name="Select board CBSE").nth(2).click()
        self.page.get_by_role("option", name="Science", exact=True).click()
        print('Science selected as subject')
        self.page.get_by_role("button", name="Select topic and subtopic").click()
        self.page.get_by_role("option", name="Select All").get_by_role("checkbox").check()
        print('All topic & sub-topics are selected')
        self.page.keyboard.press("Tab")
        self.page.keyboard.press("Tab")
        for a in range(3):
            self.page.keyboard.press("ArrowRight")
        
        for a in range(5):
            self.page.keyboard.press("ArrowLeft")
        
        for a in range(2):
            self.page.keyboard.press("ArrowRight")
        print('difficulty level moves correctly.')
        self.page.locator('//button[text()="Next"]').click()
        print('Fastrack Review page displayed')


    def fastrack_review_question(self):
        #swap function
        for n in range(10):
            swap=self.page.locator('//*[@data-testid="LoopIcon"]').nth(n)
            swap.click()

        self.page.locator('//button[text()="Next"]').click()
        print('Fastrack Schedule page displayed correctly.')
        

    def schedule_page_data(self):
        self.page.locator('//div[@id="tree-simple-select"]').click()
        self.page.locator('//span[text()="SAT class"]').click()
        self.page.keyboard.press('Escape')
        self.page.locator('//input[@type="number"]').fill('60')
        checkbox = self.page.locator('//label[contains(@class,"css-1jaw3da")]')
        count = checkbox.count()
        
        for ch in range(count):
            checkbox.nth(ch).check()
            data = checkbox.nth(ch).text_content()
            print(data, 'is selected')

        self.page.locator('//button[text()="Assign"]').click()
        print('Assign button clicking successfully')
        self.page.locator('//div[text()="Confirm"]').click()
        print('confirm button clicking successfully')


    
    def feedback_page(self):
        #self.page.locator('//*[@width="22.427px"]').click()
        with self.page.context.expect_page() as new_page_info:
            self.page.locator('//*[@width="22.427px"]').click()

        pdf_page = new_page_info.value
        pdf_page.wait_for_load_state()
        print(pdf_page.url)
        assert ".pdf" in pdf_page.url
        self.page.wait_for_timeout(3000)
        pdf_page.screenshot(path="./screenshot/pdf.png")
        print(pdf_page.title())
        pdf_page.close()
        print('PDF created successfully')

        #Click on Create new assessment button.
        self.page.locator('//button[text()="Create new Assessment"]').click()
        print('Create new Assessment clicking successfully.')
        self.page.wait_for_timeout(3000)
        self.page.go_back()
        self.page.locator('//button[text()="Grading home"]').click()
        print('Grading home clicking successfully.')
        self.page.wait_for_timeout(3000)
        self.page.go_back()
        self.page.locator('//*[name()="path" and contains(@d,"M18 16.08c")]').click()
        print('Grading home clicking successfully.')
        self.page.wait_for_timeout(2000)
        self.page.locator('//button[normalize-space()="Copy link"]')
        self.page.reload()

        
            