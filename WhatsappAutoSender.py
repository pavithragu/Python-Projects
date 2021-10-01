from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def send_file():
    receiver = input("Enter the contact name of the user: ")
    filepath = input("Enter file path: ")

    # Open the Chrome Browser
    browser = webdriver.Chrome(executable_path=r"C:\Users\MRP\Downloads\chromedriver_win32\chromedriver.exe")

    # Whatsapp link to load
    browser.get('https://web.whatsapp.com/')

    print("Scan the QR code with your Whatsapp Mobile to Open WhatsApp Web")
    sleep(10)

    # Click on the Receiver
    user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(receiver))
    user.click()
    sleep(1)

    # Click on the Attachment
    attachment_box = browser.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()
    sleep(1)

    # Attach the file
    image_box = browser.find_element_by_xpath('//input[@accept = "*"]')
    image_box.send_keys(filepath)
    sleep(3)

    # Click on the Send Button
    send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()

    print("File Sent Successfully!")


def send_message():
    receiver = input("Enter the contact name of the user: ")
    msg = input('Enter your Message: ')
    count = int(input('How many times you want to send: '))

    # Open the Chrome Browser
    browser = webdriver.Chrome(executable_path=r"C:\Users\MRP\Downloads\chromedriver_win32\chromedriver.exe")

    # Whatsapp link to load
    browser.get('https://web.whatsapp.com/')

    print("Scan the QR code with your Whatsapp Mobile to Open WhatsApp Web")
    sleep(10)

    # Click on the Receiver
    user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(receiver))
    user.click()
    sleep(1)

    # Send messages with loop
    message_box = browser.find_element_by_xpath('//div[@role="textbox"][@contenteditable="true"][@data-tab="9"]')
    for i in range(count):
        message_box.send_keys(msg + Keys.ENTER)

    print("Message Sent Successfully!")


while True:
    print("\n<------------------- Whatsapp Auto Sender ------------------->\n")
    print("Available Options:\n1. Send File\n2. Send Message\n3. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        send_file()
    elif choice == "2":
        send_message()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid selection! Please try again...")
