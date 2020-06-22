from base.selenium_driver import SeleniumDriver
import untility.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
   # _login_link = "Login"
    _email_field = "username"
    _password_field = "password"
    _login_button = "html/body/div[1]/div/form/button"

    #def clickLoginLink(self):
        #self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        #self.clickLoginLink()

        # self.clearField()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("html/body/div[1]/div[3]/div[1]/div/div/div[2]/ul/li[4]/a/strong",locatorType="xpath")

        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'These credentials do not match our records.')]",locatorType="xpath")
        return result
    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")


    # def clearFields(self):
    #     emailField = self.getElement(locator=self._email_field)
    #     emailField.clear()
    #     passwordField = self.getElement(locator=self._password_field)
    #     passwordField.clear()

