import time
import os
from datetime import datetime

SYSTEM_NAME = "SAMProb Core"
DOCTOR_NAME = "Dr Samaké Amara Tabaouo"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print(f"Initialisation de {SYSTEM_NAME}...")
    time.sleep(1)
    print(f"Authentification : {DOCTOR_NAME} [OK]")
    time.sleep(0.5)
    
    while True:
        clear_screen()
        print("="*60)
        print(f"   HUB DIAGNOSTIQUE {SYSTEM_NAME} v1.0")
        print(f"   Utilisateur : {DOCTOR_NAME}")
        print("="*60)
        print("\nCONTEXTE ACTUEL :")
        print("1. [CHU]  Donka (Plateau technique complet)")
        print("2. [CSA]  Maferinya (Ressources limitées)")
        print("3. Quitter")
        
        choice = input("\n>> Choix du contexte (1/2/3) : ")
        
        if choice == '3':
            print("Fermeture du système...")
            break
            
        context = "CHU Donka" if choice == '1' else "CSA Maferinya"
        
        print(f"\n--- MODE {context.upper()} ACTIVÉ ---")
        print("Veuillez décrire le cas (Symptômes, Constantes, Histoire)...")
        print("Appuyez sur Entrée après avoir saisi les données.")
        data = input(">> ")
        
        print("\n[ANALYSE EN COURS...]")
        time.sleep(1.5)
        print("\n" + "-"*50)
        print("COPIEZ CE RAPPORT ET COLLEZ-LE DANS LE CHAT AVEC L'IA :")
        print("-"*50)
        
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"CAS CLINIQUE | {timestamp} | {context}")
        print(f"DONNÉES : {data}")
        print("-"*50)
        
        input("\nAppuyez sur Entrée pour traiter un nouveau patient...")

if __name__ == "__main__":
    main()
