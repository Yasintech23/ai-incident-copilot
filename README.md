# AI Incident Copilot

![Tests](https://github.com/Yasintech23/ai-incident-copilot/actions/workflows/tests.yml/badge.svg)

AI Incident Copilot is a Python security tool that analyzes Linux log files and detects suspicious activity.
It currently reads SSH login attempts from `auth.log` and counts failed login attempts per IP address.
If an IP address has 3 or more failed attempts, it is flagged as a possible brute force attack.
The project includes automated tests with pytest that check the counting logic and make sure successful logins are ignored.
The next step is to add AI that explains incidents and suggests actions, and to deploy the tool on Azure with CI/CD.

## Features
- Reads the Linux log file `auth.log`
- Counts failed login attempts per IP address
- Warns about possible brute force attacks (3 or more failed attempts)
- Automated tests with pytest

## Run the program
```bash
python3 main.py
```

## Run the tests
```bash
python3 -m pytest -v
```

## Example output
```
[VARNING] 203.0.113.5: 3 misslyckade försök – möjlig brute force
[OK] 198.51.100.7: 1 misslyckade försök
```

## Roadmap
1. Log parser without AI ✅
2. Tests with pytest ✅
3. Automated tests with GitHub Actions ✅
4. Detect more attack patterns (e.g. successful login after brute force)
5. AI that explains incidents and suggests actions
6. Deployment on Azure with CI/CD
