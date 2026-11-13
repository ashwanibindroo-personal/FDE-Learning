# 1. From friday_tools import longest_name
from friday_tools import longest_name

# 2. Sample data
# a. ROADS: roads with names, without names and without tags
ROADS = [
        {"id": 1, "tags": {"highway": "primary", "name": "FC Road"}},
        {"id": 2, "tags": {"highway": "residential", "name": "Senapati Bapat Road"}},
        {"id": 3, "tags": {"highway": "service"}},
        {"id": 4},
    ]
#b. NO_NAME_ROADS: roads with tags but no names
NO_NAME_ROADS = [
    {"id": 1, "tags": {"highway": "service"}},
    {"id": 2, "tags": {"highway": "footway"}},
]

EMPTY_LIST_OF_ROADS = []

# 3. define a function/test which ensures the longest name (Senapati Bapat Road) is produced as an output
def test_longest_name_on_road():
    long_name = longest_name(ROADS)
    assert long_name == "Senapati Bapat Road"

# 4. define a function/test that "longest_name" returns None when given an empty list of roads
def test_longest_name_returns_None_given_empty_list():
    long_name = longest_name(EMPTY_LIST_OF_ROADS)
    assert long_name is None

# 5. define a function/test that "longest_name" returns None when given roads which have no names
def test_longest_name_returns_None_given_no_name_roads():
    long_name = longest_name(NO_NAME_ROADS)
    assert long_name is None