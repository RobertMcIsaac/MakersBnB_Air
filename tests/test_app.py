from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
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