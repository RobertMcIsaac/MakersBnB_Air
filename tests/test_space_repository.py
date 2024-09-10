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
        Space('Cozy Apartment', 'A small, comfortable apartment in the city center', 120, 1),
        Space('Modern Office', 'A sleek office space with a view', 250, 4),
        Space('Warehouse', 'Spacious warehouse near the docks', 300, 3),
        Space('Studio Loft', 'An open loft with lots of natural light', 150, 5),
        Space('Private Office', 'A compact office space for individual work', 18, 2),
        Space('Garden Den', 'A shed in my garden', 180, 2),
        Space('Cupboard', 'A crappy cupboard underneath the stairs', 150, 2)
    ]

"""
    Create a space
"""

def test_create_space(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repo = SpaceRepository(db_connection)
    test_space = Space('Little Black Box', 'Very dark and mysterious', 555, 5)
    repo.create(test_space)
    assert repo.all() == [
        Space('Cozy Apartment', 'A small, comfortable apartment in the city center', 120, 1),
        Space('Modern Office', 'A sleek office space with a view', 250, 4),
        Space('Warehouse', 'Spacious warehouse near the docks', 300, 3),
        Space('Studio Loft', 'An open loft with lots of natural light', 150, 5),
        Space('Private Office', 'A compact office space for individual work', 18, 2),
        Space('Garden Den', 'A shed in my garden', 180, 2),
        Space('Cupboard', 'A crappy cupboard underneath the stairs', 150, 2),
        Space('Little Black Box', 'Very dark and mysterious', 555, 5)
    ]

"""
    Find all by user_id
"""

def test_find_all_by_owner(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repo = SpaceRepository(db_connection)
    spaces = repo.find_with_user_id(2)
    assert spaces == [
        Space('Private Office', 'A compact office space for individual work', 18, 2),
        Space('Garden Den', 'A shed in my garden', 180, 2),
        Space('Cupboard', 'A crappy cupboard underneath the stairs', 150, 2),
    ]
