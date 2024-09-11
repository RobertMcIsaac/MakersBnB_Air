from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
    INDEX PAGE
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")



# BOOKING TESTS

"""
GET/ all bookings 
"""

"""
POST/ create booking
test that when we create a booking the form logs a booking_date
"""
def test_post_booking(db_connection, page, test_web_address):
    db_connection.seed('seeds/air_makersbnb_test.sql')
    page.goto(f'https://{test_web_address}/booking')
    page.fill('input[name=booking_date]', '2025-09-20')
    page.click("text='Make Booking")
    p = page.locator("p")
    expect(p).to_have_text("Your booking is pending. Please wait for confirmation")

    # page.click("text='add new album'")
    # page.fill("input[name=title]", "test album")
    # page.fill("input[name=release_year]", "1999")
    # page.fill("input[name=artist_id]", "3")
    # page.click("text='click to add album'")

"""
PUT/ update booking status
"""
=======
"""
    SPACES MAIN PAGE
    Request : GET
    Path : /spaces
"""
def test_spaces_page(page, test_web_address):

    page.goto(f"http://{test_web_address}/spaces")

    # title_tag = page.locator("title")
    h3_tags = page.locator('h3')
    h5_tags = page.locator('h5')
    p_tags = page.locator('p')

    # expect(title_tag).to_have_text('MakersBnB - Air')
    expect(h3_tags).to_have_text([
        'Cozy Apartment',
        'Modern Office',
        'Warehouse', 
        'Studio Loft', 
        'Private Office',
        'Garden Den', 
        'Cupboard'
    ])

    expect(h5_tags).to_have_text([
        '120.00',
        '250.00',
        '300.00',
        '150.00',
        '18.00',
        '180.00',
        '150.00'
    ])

    expect(p_tags).to_have_text([
        'A small, comfortable apartment in the city center', 
        'A sleek office space with a view', 
        'Spacious warehouse near the docks', 
        'An open loft with lots of natural light', 
        'A compact office space for individual work', 
        'A shed in my garden', 
        'A crappy cupboard underneath the stairs'
    ])

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
 
    page.click("button[type='submit']")

    expect(page).to_have_url("/register_success")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Successfully created an account")