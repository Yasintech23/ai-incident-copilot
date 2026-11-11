from collections import Counter

THRESHOLD = 3

failed = Counter()

with open("data/auth.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[parts.index("from") + 1]
            failed[ip] += 1

for ip, count in failed.items():
    if count >= THRESHOLD:
        print(f"[VARNING] {ip}: {count} misslyckade försök – möjlig brute force")
    else:
        print(f"[OK] {ip}: {count} misslyckade försök")
