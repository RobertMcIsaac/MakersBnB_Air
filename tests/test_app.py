from playwright.sync_api import Page, expect

# Tests for your routes go here

# LOGIN TESTS

"""GET/ login page"""

def test_render_login_page_successfully(page, test_web_address):
    page.goto(f'http://{test_web_address}/login')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Login")
    input_email_tag = page.get_by_text("Username")
    expect(input_email_tag).to_be_visible()
    input_password_tag = page.get_by_text("Password")
    expect(input_password_tag).to_be_visible()
    submit_button_tag = page.locator("button")
    expect(submit_button_tag).to_have_text("Submit")

"""
POST login information successfully
"""

# def test_login_success(db_connection, page, test_web_address):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/air_makersbnb_test.sql')
#     page.goto(f'http://{test_web_address}/login')
#     input_username_tag = page.locator("input[name='username']")
#     input_username_tag.fill('Sam')
#     input_password_tag = page.locator("input[name='password']")
#     input_password_tag.fill('password123!')
#     page.click("button[type='submit']")
#     expect(page).to_have_url("/login")
#     p_tag = page.locator("p")
#     expect(p_tag).to_have_text("This is the homepage.")

# def test_register_page(page, test_web_address):
#     page.set_default_timeout(1000)

#     page.goto(f"http://{test_web_address}/register")

#     h1_tag = page.locator("h1")
#     expect(h1_tag).to_have_text("Register")

#     input_username_tag = page.locator("input[name='username']")
#     input_username_tag.fill('Bobby')

#     input_email_tag = page.locator("input[name='email']")
#     input_email_tag.fill("bobby@example.com")

#     input_password_tag = page.locator("input[name='password']")
#     input_password_tag.fill("pasw0rd!2#")
 
#     page.click("button[type='submit']")

#     expect(page).to_have_url("/register_success")
#     p_tag = page.locator("p")
#     expect(p_tag).to_have_text("Successfully created an account")

# BOOKING TESTS

"""
GET/ all bookings 
"""

"""
POST/ create booking
test that when we create a booking the form logs a booking_date
"""
# def test_post_booking(db_connection, page, test_web_address):
#     db_connection.seed('seeds/air_makersbnb_test.sql')
#     page.goto(f'http://{test_web_address}/booking/1/2')
#     page.fill('input[name=date_booked]', '2025-10-20')
#     page.click("text=Confirm booking")
#     h2 = page.locator("h2")
#     expect(h2).to_have_text("Your booking is pending. Please wait for confirmation")

# def test_booking_date_unavailable(db_connection, page, test_web_address):
#     db_connection.seed('seeds/air_makersbnb_test.sql')
#     page.goto(f'http://{test_web_address}/booking/1/3')
#     page.fill('input[name=date_booked]', '2024-09-25')
#     page.click("text=Confirm booking")
#     h6 = page.locator("h6")
#     expect(h6).to_have_text("This date is unavailable. Please choose another date.")


"""
PUT/ update booking status
"""

"""
    SPACES MAIN PAGE
    Request : GET
    Path : /spaces
"""
# def test_spaces_page(page, test_web_address):

#     page.goto(f"http://{test_web_address}/spaces")

#     # title_tag = page.locator("title")
#     h3_tags = page.locator('h3')
#     h5_tags = page.locator('h5')
#     p_tags = page.locator('p')

#     # expect(title_tag).to_have_text('MakersBnB - Air')
#     expect(h3_tags).to_have_text([
#         'Cozy Apartment',
#         'Modern Office',
#         'Warehouse', 
#         'Studio Loft', 
#         'Private Office',
#         'Garden Den', 
#         'Cupboard'
#     ][::-1])

#     expect(h5_tags).to_have_text([
#         '120.00',
#         '250.00',
#         '300.00',
#         '150.00',
#         '18.00',
#         '180.00',
#         '150.00'
#     ][::-1])

#     expect(p_tags).to_have_text([
#         'A small, comfortable apartment in the city center', 
#         'A sleek office space with a view', 
#         'Spacious warehouse near the docks', 
#         'An open loft with lots of natural light', 
#         'A compact office space for individual work', 
#         'A shed in my garden', 
#         'A crappy cupboard underneath the stairs'
#     ][::-1])

"""
    Create Space succes
"""

# def test_create_space_successful(page, test_web_address):
#     page.set_default_timeout(1000)

#     page.goto(f"http://{test_web_address}/create_space")

#     h1_tag = page.locator("h1")
#     expect(h1_tag).to_have_text("Create a space")

#     input_name_tag = page.locator("input[name='name']")
#     input_name_tag.fill('Bobbies House')

#     input_description_tag = page.locator("input[name='description']")
#     input_description_tag.fill("Bobbies lovely cold house")

#     input_price_tag = page.locator("input[name='price']")
#     input_price_tag.fill("12.00")
    
#     input_user_id_tag = page.locator("input[name='user_id']")
#     input_user_id_tag.fill("1")
 
#     page.click("text='Create space'")

#     p_tag = page.locator("p")
#     expect(p_tag).to_have_text("Successfully created a space")

"""
    Register page
"""

def test_register_page(page, test_web_address):
    page.set_default_timeout(1000)

    page.goto(f"http://{test_web_address}/register")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Register")

    input_username_tag = page.locator("input[name='username']")
    input_username_tag.fill('Bobby')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("bobby@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("pasw0rd!2#")
 
    page.click("text='Submit'")

    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Successfully created an account")


"""
    REGISTER VALIDATION -- password fails validation, URL remains the same
"""
def test_password_throws_validation_errors(page, test_web_address):
    page.set_default_timeout(1000)

    page.goto(f"http://{test_web_address}/register")

    input_username_tag = page.locator("input[name='username']")
    input_username_tag.fill('Bobby')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("bobby@example.com")

    input_password_tag = page.locator("input[name='password']")

    # ---- TESTING INVALID PASSWORD
    input_password_tag.fill("pass")
 
    page.click("text='Submit'")

    expect(page).to_have_url(f"http://{test_web_address}/register")


"""
    REGISTER VALIDATION -- username fails validation, URL remains the same
"""
def test_username_throws_validation_errors(page, test_web_address):
    page.set_default_timeout(1000)

    page.goto(f"http://{test_web_address}/register")

    input_username_tag = page.locator("input[name='username']")

    # ----- TESTING DUPLICATE USERNAME
    input_username_tag.fill('Sam')

    input_email_tag = page.locator("input[name='email']")
    input_email_tag.fill("bobby@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("passworfhiene!@")
 
    page.click("text='Submit'")

    expect(page).to_have_url(f"http://{test_web_address}/register")


"""
    REGISTER VALIDATION -- email fails validation, URL remains the same
"""
def test_email_throws_validation_errors(page, test_web_address):
    page.set_default_timeout(1000)

    page.goto(f"http://{test_web_address}/register")

    input_username_tag = page.locator("input[name='username']")

    input_username_tag.fill('Sam')

    input_email_tag = page.locator("input[name='email']")

    # ----- TESTING DUPLICATE EMAIL
    input_email_tag.fill("sam@example.com")

    input_password_tag = page.locator("input[name='password']")
    input_password_tag.fill("passworfhiene!@")
 
    page.click("text='Submit'")

    expect(page).to_have_url(f"http://{test_web_address}/register")

