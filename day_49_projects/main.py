from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import os

NAME = "Navruza"
ACCOUNT_EMAIL = "testing@test.com"
ACCOUNT_PASSWORD = "vovovovo@lalala"
GYM_URL = "https://appbrewery.github.io/gym/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 5)

login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# create_account =wait.until(ec.element_to_be_clickable((By.ID, "toggle-login-register")))
# create_account.click()
#
# name_input = wait.until(ec.presence_of_element_located((By.ID, "name-input")))
# name_input.clear()
# name_input.send_keys(ACCOUNT_EMAIL)

email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_button = driver.find_element(By.ID, "submit-button")
submit_button.click()

# Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

target_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            #
            # button = time.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            # button.click()

            print(f" 🥳 Booked for Tuesday {time_text}, {class_name}")
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"•Already booked: {class_info}")
                already_booked_count += 1
                target_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"•Already on waitlist: {class_info}")
                waitlist_count += 1
                target_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                button.click()
                WebDriverWait(driver, 5).until(ec.text_to_be_present_in_element((By.XPATH, "Booked")))
                print(f"•Successfully booked: {class_info}")
                booked_count += 1
                target_classes.append(f"[New Booking] {class_info}")
            elif button.text == "Join Waitlist":
                button.click()
                WebDriverWait(driver, 5).until(ec.text_to_be_present_in_element((By.XPATH, "Booked")))
                print(f"•Joined waitlist for: {class_info}")
                waitlist_count += 1
                target_classes.append(f"[New Waitlist] {class_info}")

# print("\n--- BOOKING SUMMARY ---")
# print(f"New bookings: {booked_count}")
# print(f"New waitlist entries: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Tuesday & Thursday 6pm classes: {booked_count + waitlist_count + already_booked_count}")
#
# # Print detailed class list
# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in target_classes:
#     print(f"  • {class_detail}")

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")

my_booking_link = driver.find_element(By.ID, value="my-bookings-link")
my_booking_link.click()

wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))


all_bookings= driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
confirmed_bookings_count= 0

for books in all_bookings:
    try:
        when_paragraph = books.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Checks if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = books.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            confirmed_bookings_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {confirmed_bookings_count} bookings")

if total_booked == confirmed_bookings_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - confirmed_bookings_count} bookings")


# driver.quit()






