from lib.space_repository import SpaceRepository
from lib.space import Space

"""
    Get all spaces
"""

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repo = SpaceRepository(db_connection)
    spaces = repo.all()
    assert spaces == [
        Space(1, 'Cozy Apartment', 'A small, comfortable apartment in the city center', 120, 1),
        Space(2, 'Modern Office', 'A sleek office space with a view', 250, 4),
        Space(3, 'Warehouse', 'Spacious warehouse near the docks', 300, 3),
        Space(4, 'Studio Loft', 'An open loft with lots of natural light', 150, 5),
        Space(5, 'Private Office', 'A compact office space for individual work', 18, 2),
        Space(6, 'Garden Den', 'A shed in my garden', 180, 2),
        Space(7, 'Cupboard', 'A crappy cupboard underneath the stairs', 150, 2)
    ]

"""
    Create a space
"""

def test_create_space(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repo = SpaceRepository(db_connection)
    test_space = Space(None, 'Little Black Box', 'Very dark and mysterious', 555, 5)
    repo.create(test_space)
    assert repo.all() == [
        Space(1, 'Cozy Apartment', 'A small, comfortable apartment in the city center', 120, 1),
        Space(2, 'Modern Office', 'A sleek office space with a view', 250, 4),
        Space(3, 'Warehouse', 'Spacious warehouse near the docks', 300, 3),
        Space(4, 'Studio Loft', 'An open loft with lots of natural light', 150, 5),
        Space(5, 'Private Office', 'A compact office space for individual work', 18, 2),
        Space(6, 'Garden Den', 'A shed in my garden', 180, 2),
        Space(7, 'Cupboard', 'A crappy cupboard underneath the stairs', 150, 2),
        Space(8, 'Little Black Box', 'Very dark and mysterious', 555, 5)
    ]

"""
    Find all by user_id
"""

def test_find_all_by_owner(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repo = SpaceRepository(db_connection)
    spaces = repo.find_with_user_id(2)
    assert spaces == [
        Space(5, 'Private Office', 'A compact office space for individual work', 18, 2),
        Space(6,'Garden Den', 'A shed in my garden', 180, 2),
        Space(7, 'Cupboard', 'A crappy cupboard underneath the stairs', 150, 2),
    ]

"""
    Find space by space_id
"""
def test_find_by_id(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repo = SpaceRepository(db_connection)
    space = repo.find(2)
    assert space == Space(2, 'Modern Office', 'A sleek office space with a view', 250, 4)
    