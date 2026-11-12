import pytest
from roads import load_roads, summarize_roads
SAMPLE_ROADS = [
    {"type": "way", "id": 1, "tags": {"highway": "primary", "name": "FC Road"}},
    {"type": "way", "id": 2, "tags": {"highway": "primary"}},
    {"type": "way", "id": 3, "tags": {"highway": "footway", "name": "Lane 5"}},
    {"type": "way", "id": 4},
]

def test_empty_list_gives_zero_counts():
    summary = summarize_roads([])
    assert summary["total"] == 0
    assert summary["by_type"] == {}

def test_counts_roads_by_type():
    summary = summarize_roads(SAMPLE_ROADS)
    assert summary["by_type"] == {"primary": 2, "footway": 1}

def test_counts_unnamed_roads():
    summary = summarize_roads(SAMPLE_ROADS)
    assert summary["unnamed"] == 1

def test_skips_road_without_tags():
    summary = summarize_roads(SAMPLE_ROADS)
    assert summary["skipped"] == 1

def test_processed_plus_skipped_equals_total():
    summary = summarize_roads(SAMPLE_ROADS)
    assert summary["processed"] + summary["skipped"] == summary["total"]

def test_missing_file_stops_program():
    with pytest.raises(SystemExit):
        load_roads("week1/does_not_exist.json")

def test_broken_json_stops_program():
    with pytest.raises(SystemExit):
        load_roads("week1/broken.json")

def test_loads_real_file():
    roads = load_roads("week1/pune_roads.json")
    assert len(roads) == 428
