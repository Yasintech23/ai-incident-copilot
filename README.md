# AI Incident Copilot

En säkerhetsassistent i Python som analyserar loggfiler och hittar misstänkta händelser.

## Vad den gör just nu
- Läser Linux-loggen `auth.log`
- Räknar misslyckade inloggningar per IP-adress
- Varnar för möjliga brute force-attacker (3 eller fler misslyckade försök)
- Har automatiska tester med pytest

## Kör programmet
```bash
python3 main.py
```

## Kör testerna
```bash
python3 -m pytest -v
```

## Exempel på resultat
```
[VARNING] 203.0.113.5: 3 misslyckade försök – möjlig brute force
[OK] 198.51.100.7: 1 misslyckade försök
```

## Plan
1. Loggparser utan AI ✅
2. Tester med pytest ✅
3. Automatiska tester med GitHub Actions
4. Hitta fler attackmönster (t.ex. lyckad inloggning efter brute force)
5. AI som förklarar incidenter och föreslår åtgärder
6. Driftsättning på Azure med CI/CD
