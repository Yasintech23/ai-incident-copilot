from collections import Counter

THRESHOLD = 3


def count_failed_logins(path):
    failed = Counter()
    with open(path) as f:
        for line in f:
            if "Failed password" in line:
                parts = line.split()
                ip = parts[parts.index("from") + 1]
                failed[ip] += 1
    return failed


def find_suspicious(failed, threshold=THRESHOLD):
    suspicious = []
    for ip, count in failed.items():
        if count >= threshold:
            suspicious.append(ip)
    return suspicious


def main():
    failed = count_failed_logins("data/auth.log")
    suspicious = find_suspicious(failed)

    for ip, count in failed.items():
        if ip in suspicious:
            print(f"[VARNING] {ip}: {count} misslyckade försök – möjlig brute force")
        else:
            print(f"[OK] {ip}: {count} misslyckade försök")


if __name__ == "__main__":
    main()
