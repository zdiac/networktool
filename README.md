ELIAS KARLSTRÖM

Python är enklare att koda i än C för att man slipper tänka på:
1: Minne, exempelvis i C så gjorde jag char ip[50];
Jag behövde aldrig tänka på minne i python.

2. Stränghantering. I python räckte det med att skriva delar = ip.split(".")
   i C så var jag tvungen att dela upp alla delar av ip adressen själv
   for (int i = 0; ip[i] != '\0'; i++) {
    if (isdigit(ip[i])) { ... }
    else if (ip[i] == '.') { ... }
}

3. Loggning. I python kunde jag göra logg.append(f"[{datetime.now()}] Validerade IP: {ip}")
I C så var jag tvungen att välja ett max antal loggar, bestämma längd per loggrad och hålla koll på index.

4. Mitt python program behövde inte kompileras för att köras i Ubuntu, jag kunde köra det med att skriva python3 namnpåprogram.py

5. Om jag exempelvis skrev ett "(" så fyllde den automatiskt in ")" samma sak med citattecken. Det var enklare att se vart man eventuellt gjort fel.

6. Det var otroligt enkelt att lägga till saker i git med VScode. Jag behövde aldrig skriva något förutom mina commit-meddelanden.

PS.
Jag gjorde mina program med hjälp utav AI, för annars hade det varit för svårt för den kunskapen jag besitter just nu, men jag gjorde i princip en rad
i taget och bad AI att förklara varje rad jag gjorde, sedan comittade jag och fortsatte så.
