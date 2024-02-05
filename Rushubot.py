
    # Création du dictionnaire des artefacts basé sur les informations fournies

artefacts = {
    1: {"Nom": "Bond", "Passif": "+1PM", "Effet": "DO terre sur une cellule libre PO 4 - 6", "Iteration": "+1 po par tour", "Placement": "osef"},
    2: {"Nom": "Saccage", "Passif": "+1PW début de tour", "Effet": "DO feu cercle de 1-2 sur l'entité la plus proche", "Iteration": "+1 joueur par tour", "Placement": "Plus de 2 cases des joueurs proches du boss"},
    3: {"Nom": "Malédiction", "Passif": "150 Msoin", "Effet": "DO terre + 1 incurable sur le joueur le plus affaibli", "Iteration": "+1 niveau d'incurable par tour", "Placement": "osef"},
    4: {"Nom": "Cyclone", "Passif": "10% VdV", "Effet": "DO air, pousse le joueur de 2 cases", "Iteration": "+1 case par tour", "Placement": "Stab si danger"},
    5: {"Nom": "Oblitération", "Passif": "100 Mdos", "Effet": "DO feu anneau de PO 13-30 autour de rushu", "Iteration": "Baisse la taille minimale de l'anneau de 1", "Placement": "13 - (Nb Tour de la phase) proche du boss"},
    6: {"Nom": "Massacre", "Passif": "100 Mmonocible", "Effet": "Do feu en cercle 3 autour de rushu", "Iteration": "Augmente la taille du cercle de 1", "Placement": "3 + (nb tour de la phase) éloigné du boss"},
    7: {"Nom": "Dévastation", "Passif": "100 Mzone", "Effet": "Do feu anneau 5-8 autour de l'entité la plus proche de Rushu", "Iteration": "+1 joueur par tour", "Placement": "Moins de 5 ou plus de 8 des joueurs impactés"},
    8: {"Nom": "Météore", "Passif": "15 DF en ligne", "Effet": "Do Feu, pose un glyphe cercle de 3 sur 3 joueurs", "Iteration": "+1 taille et +1 joueur par tour", "Placement": "Ne pas se placer sur les glyphes"},
    9: {"Nom": "Grêle", "Passif": "100 Mmélée", "Effet": "Do eau sur l'entité la plus proche de rushu", "Iteration": "+1 entité par tour", "Placement": "Tank/invoc proche de Rushu"},
    10: {"Nom": "Tonnerre", "Passif": "100 Mdistance", "Effet": "Do air sur l'entité le plus éloigné de Rushu", "Iteration": "+1 entité par tour", "Placement": "Tank/invoc éloigné de Rushu"},
    11: {"Nom": "Obscurité", "Passif": "15DF côté", "Effet": "Prison autour des joueurs si traversé DO stasis et -1PO 2 tours", "Iteration": "nb de dégats et rall PO augmenté", "Placement": "osef mais courage"},
    12: {"Nom": "Ressac", "Passif": "1PA", "Effet": "DO eau et rall rési sur l'entité la plus affaibli", "Iteration": "+40 rall rési", "Placement": ""},
    13: {"Nom": "Ouragan", "Passif": "+10% Armure donnée", "Effet": "Do air, attire de 2 cases", "Iteration": "+1 case attiré", "Placement": "osef sauf si ordre artefact cringe alors stab si danger"},
    14: {"Nom": "Fracas", "Passif": "10% Df convertit en armure", "Effet": "Do terre, -1pm + stab", "Iteration": "rall PM +1", "Placement": "osef"},
    15: {"Nom": "Explosion", "Passif": "10% armure reçu", "Effet": "Do terre anneau 4 - 6", "Iteration": "+1 PO max", "Placement": "Moins de 3 ou plus (6+Nb de tour)"},
    16: {"Nom": "Grondement", "Passif": "150% Berserk", "Effet": "invoque 2 rochers autour de Rushu détruire un rocher retire 2PM", "Iteration": "+2 rocher par tour", "Placement": "osef"},
}

    
def select_artefacts():
    selected_artefacts = []
    print("Veuillez sélectionner 4 artefacts par leur numéro.")
    while len(selected_artefacts) < 4:
        try:
            choice = input(f"Sélectionnez l'artefact {len(selected_artefacts) + 1}: ")
            artefact_id = int(choice)
            if artefact_id in artefacts and artefact_id not in selected_artefacts:
                selected_artefacts.append(artefact_id)
            else:
                print("Numéro d'artefact invalide ou déjà sélectionné. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return selected_artefacts

def show_artefact_info(selected_artefacts):
    for artefact_id in selected_artefacts:
        artefact = artefacts[artefact_id]
        info = f"Artefact {artefact_id}: {artefact['Nom']} - {artefact['Effet']}, {artefact['Iteration']}, Placement: {artefact['Placement']}"
        print(info)

def main():
    selected_artefacts = select_artefacts()
    show_artefact_info(selected_artefacts)

if __name__ == "__main__":
    main()