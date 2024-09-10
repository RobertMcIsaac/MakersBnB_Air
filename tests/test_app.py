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