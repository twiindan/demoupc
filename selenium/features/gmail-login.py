__author__ = 'arobres'


from lettuce import *
import time
from selenium import webdriver


@before.each_scenario
def setUp(scenario):

    world.driver = webdriver.Firefox()
    world.driver.get("http://gmail.com")


@step('Given a user registered with username "(.*)" and password "(.*)"')
def user_registered(step, user, pwd):
    print "User registered with: "
    print "username: " + user
    print "password: " + pwd


@step('When I enter (.*) and (.*)')
def login(step, username, password):
    textbox_username = world.driver.find_element_by_name("Email")
    textbox_pwd = world.driver.find_element_by_name("Passwd")
    textbox_username.clear()
    textbox_pwd.clear()
    textbox_username.send_keys(username)
    textbox_pwd.send_keys(password)
    button = world.driver.find_element_by_name('signIn')
    button.click()


@step('Then I obtain an <error>')
def obtain_error(step):
    errortext =  world.driver.find_element_by_id('errormsg_0_Passwd')
    assert "correo" in world.driver.title
    time.sleep(5)


@step('Then I enter to my account')
def then_i_enter_to_my_account(step):
    time.sleep(15)
    first_mail = world.driver.find_element_by_name('El equipo de Gmail')
    assert "Recibidos" in world.driver.title
    time.sleep(5)



@after.each_scenario
def tearDown(scenario):
    world.driver.close()
