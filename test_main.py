from main import count_failed_logins, find_suspicious


def test_counts_failed_logins_per_ip():
    failed = count_failed_logins("data/auth.log")
    assert failed["203.0.113.5"] == 3
    assert failed["198.51.100.7"] == 1


def test_ignores_successful_logins():
    failed = count_failed_logins("data/auth.log")
    assert "192.168.1.10" not in failed


def test_finds_brute_force_ip():
    failed = count_failed_logins("data/auth.log")
    assert find_suspicious(failed) == ["203.0.113.5"]
