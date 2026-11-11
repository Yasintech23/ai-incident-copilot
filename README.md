# AI Incident Copilot

En säkerhetsassistent i Python som analyserar loggfiler och hittar misstänkta händelser.

## Vad den gör just nu
- Läser Linux-loggen `auth.log`
- Räknar misslyckade inloggningar per IP-adress
- Varnar för möjliga brute force-attacker (3 eller fler misslyckade försök)

## Kör programmet
```bash
python3 main.py
```

## Exempel på resultat
## Plan
1. Loggparser utan AI ✅
2. Tester med pytest
3. AI som förklarar incidenter och föreslår åtgärder
4. Driftsättning på Azure med CI/CD
