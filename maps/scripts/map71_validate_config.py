#!/usr/bin/env python3
"""Validate Map 71's bounded, keyless runtime source contract."""

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def main():
    config = json.loads((ROOT / "data/map71-wildlife-api-config.json").read_text())
    assert config["schema_version"] == 1
    assert config["radii_km"] == [5, 10, 25]
    assert config["default_radius_km"] in config["radii_km"]
    assert 1 <= config["record_limit_per_source"] <= 30
    assert 5000 <= config["request_timeout_ms"] <= 20000
    expected = {
        "inaturalist": "api.inaturalist.org",
        "gbif": "api.gbif.org",
    }
    for name, host in expected.items():
        source = config["sources"][name]
        parsed = urlparse(source["endpoint"])
        assert parsed.scheme == "https" and parsed.hostname == host
        assert not parsed.username and not parsed.password and not parsed.query
    assert set(config["sources"]["inaturalist"]["licenses"]) == {"cc0", "cc-by"}
    assert set(config["sources"]["gbif"]["licenses"]) == {"CC0_1_0", "CC_BY_4_0"}
    print("Validated Map 71 bounded keyless configuration")


if __name__ == "__main__":
    main()
