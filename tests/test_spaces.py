from lib.space import Space

"""
    Initially 
    A Space has a   
        name
        description
        price
        user_ID
"""
def test_space_initialises_correctly():

    space = Space("The Scottish Conversatory", "The extremely hot and extremely cold", 20.5, 1)

    assert space.name == "The Scottish Conversatory"
    assert space.description == "The extremely hot and extremely cold"
    assert space.price == 20.50
    assert space.user_ID == 1


"""
    Two Identical Spaces are Equal : __eq__
"""
def test_space_is_equal():

    space1 = Space("The Scottish Conversatory", "The extremely hot and extremely cold", 20.5, 1)
    space2 = Space("The Scottish Conversatory", "The extremely hot and extremely cold", 20.5, 1)
    
    assert space1 == space2

"""
    Space formats nicely : __repr__
"""
def test_formats_nicely():

    space = Space("The Scottish Conversatory", "The extremely hot and extremely cold", 20.5, 1)

    assert str(space) == "Space(The Scottish Conversatory, The extremely hot and extremely cold, 20.5, 1)"
