data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

while True:
    land = input("Skriv inn hvilket land du vil se informasjon om (skriv avbryt for å avslutte): ")
    
    if land in data:
        value = data[land]
        print(f"Hovedstaden i {land} er {value[0]}, og befolkningen er {value[1]} millioner mennesker.")

  
       
    if land == "avbryt":
            
            print("Takk for nå, programmet avsluttes. Her er listen over land i databasen: ")
            
            for key, value in data.items():
                
                print(f"{key}: Hovedstad: {value[0]}, Befolkning: {value[1]} millioner")
            break
    
    if land not in data:
        print(f"Beklager, {land} er ikke registrert i databasen.")
        
        legg_til = input("Vil du legge til nytt land? Svar Y for ja eller N for nei: ").strip().upper()
        
        if legg_til == "Y":
            nytt_land = input("Skriv inn land du vil legge til: ").strip()
            hovedstad = input("Skriv inn tilhørende hovedstad: ").strip()
            befolkning = float(input("Skriv inn befolkningen i millioner (f.eks. 0.000): ").strip())
            data[nytt_land] = [hovedstad, befolkning]
        
        elif legg_til == "N":  
            print("Takk for nå, her er databasen over registrerte land:")
        
            for key, value in data.items():
                print(f"{key}: Hovedstad: {value[0]}, Befolkning: {value[1]} millioner")

print("Avslutter programmet. Her er de oppdaterte landene i databasen:")
for key, value in data.items():
    print(f"{key}: Hovedstad: {value[0]}, Befolkning: {value[1]} millioner")