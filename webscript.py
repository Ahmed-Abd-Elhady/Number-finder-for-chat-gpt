from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
from selenium.webdriver.common.action_chains import ActionChains
import cv2
import numpy as np
from selenium.webdriver.common.by import By


urls = [
    "https://azrotv.com/extras/sms-verification/messages.php?id=4628",
    "https://azrotv.com/extras/sms-verification/messages.php?id=4627",
    "https://azrotv.com/extras/sms-verification/messages.php?id=4622",
    "https://azrotv.com/extras/sms-verification/messages.php?id=4621",
]
rengerF = len(urls)
print(rengerF)


print(urls[1])
print(urls[0])
driver = webdriver.Chrome(
    executable_path="C:/Users/abelh/OneDrive/Desktop/chromedriver_win32/New folder/chromedriver.exe"
)


image = cv2.imread("your_image.jpg")
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = np.array([[0, 0, 0], [0, 1, 0], [0, 1, 0]], dtype=np.uint8)

result = cv2.matchTemplate(grayscale_image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result >= threshold)


def find():
    keyboard.press_and_release("F3")
    time.sleep(0.5)
    keyboard.write("Open AI")
    time.sleep(0.5)
    keyboard.press_and_release("Enter")
    keyboard.press_and_release("ESC")
    element = driver.find_element(By.TAG_NAME, "h1")

    element_text = element.text
    # print(element_text)
    # Convert the image to grayscale for easier processing

    # Set a threshold to determine when a match is found
    # Adjust this threshold as needed

    # Find the positions where the match exceeds the threshold

    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + 3, pt[1] + 3), (0, 0, 255), 2)

    if loc[0].size > 0:
        print(f"Found a match! {element_text}")
    else:
        print("This Number Is Used!")
    cv2.imshow("Result", image)


for url in urls:
    driver.get(url)
    find()
    print(f"The link is : {url}")

# driver.get("https://azrotv.com/extras/sms-verification/messages.php?id=4626")
# find()


action = ActionChains(driver)


time.sleep(2)


# cv2.destroyAllWindows()


time.sleep(10000000)
driver.quit()
