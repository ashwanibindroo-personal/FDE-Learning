# print(f"road_summary.py says: __name__ = {__name__}")

import logging
import os

from roads import load_roads, summarize_roads


# Print the summary report
def print_report(summary):
    print(f"Total highway features in file: {summary['total']}")
    print(f"Processed: {summary['processed']}")
    print(f"Skipped (no tags): {summary['skipped']}")
    print(f"Roads by type: {summary['by_type']}")
    print(f"Roads with no name: {summary['unnamed']}")


if __name__ == "__main__":
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    roads = load_roads("week1/pune_roads.json")
    summary = summarize_roads(roads)
    print_report(summary)
