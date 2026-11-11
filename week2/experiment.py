from road_summary import print_report

fake_summary = {
    "total": 3,
    "processed": 2,
    "skipped": 1,
    "unnamed": 1,
    "by_type": {"primary": 2},
}

print_report(fake_summary)