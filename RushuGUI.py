import tkinter as tk
from tkinter import ttk
import sys
import os

# Fonction pour redémarrer l'application
def restart_app():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Création de la fenêtre principale
root = tk.Tk()
root.title("RushuBot")

# Variables globales
current_phase = 0
selected_artefacts_by_phase = {1: [], 2: [], 3: [], 4: []}

# Fonction pour vérifier le nombre d'artefacts sélectionnés
def update_checkboxes():
    selected_count = sum(var.get() for artefact_id, var, checkbox in artefact_checkboxes)

    for artefact_id, var, checkbox in artefact_checkboxes:
        if selected_count >= 4 and var.get() == 0:
            checkbox.config(state=tk.DISABLED)
        else:
            checkbox.config(state=tk.NORMAL)

# Fonction pour afficher les sélections
def show_selection():
    # Efface les anciennes informations s'il en existe
    for widget in info_frame.pack_slaves():
        widget.destroy()

    # Crée un sous-cadre pour chaque artefact sélectionné
    for artefact_id, var, checkbox in artefact_checkboxes:
        if var.get() == 1:
            artefact = artefacts[artefact_id]
            sub_frame = tk.Frame(info_frame, borderwidth=1, relief="solid")
            sub_frame.pack(padx=5, pady=5, fill='x')

            # Nom de l'artefact
            tk.Label(sub_frame, text=artefact['Nom'], font=("Arial", 12, "bold")).pack(anchor='w')

            # Informations détaillées
            tk.Label(sub_frame, text=f"Effet: {artefact['Effet']}").pack(anchor='w')
            tk.Label(sub_frame, text=f"Iteration: {artefact['Iteration']}").pack(anchor='w')
            tk.Label(sub_frame, text=f"Placement: {artefact['Placement']}").pack(anchor='w')

# Fonction pour gérer la phase
def handle_phase():
    global current_phase

    show_selection()

    if current_phase < 4:
        selected_artefacts_by_phase[current_phase] = [artefact_id for artefact_id, var, checkbox in artefact_checkboxes if var.get() > 0]
        current_phase += 1
        phase_button.config(text="Phase suivante")
        phase_label.config(text=f"Phase {current_phase}")

        # Réinitialiser l'état des cases à cocher pour la nouvelle phase
        for artefact_id, var, checkbox in artefact_checkboxes:
            var.set(0)  # Désélectionner toutes les cases
            checkbox.config(state=tk.NORMAL)  # Réactiver toutes les cases
            if artefact_id in sum(selected_artefacts_by_phase.values(), []):
                checkbox.pack_forget()  # Cacher les cases sélectionnées dans les phases précédentes
            else:
                checkbox.pack(anchor='w')  # Réafficher les cases non sélectionnées


# Création des cases à cocher pour les artefacts
def create_artefact_checkboxes():
    global artefact_checkboxes
    artefact_checkboxes = []

    for artefact_id, artefact_info in artefacts.items():
        var = tk.IntVar()
        var.trace("w", lambda *args: update_checkboxes())
        checkbox = tk.Checkbutton(root, text=f"{artefact_id} - {artefact_info['Nom']}", variable=var, anchor='w')
        checkbox.pack(anchor='w')
        artefact_checkboxes.append((artefact_id, var, checkbox))


artefacts = {
    1: {"Nom": "Bond", "Passif": "+1PM", "Effet": "DO terre sur une cellule libre PO 4 - 6", "Iteration": "+1 po par tour", "Placement": " "},
    2: {"Nom": "Saccage", "Passif": "+1PW début de tour", "Effet": "DO feu cercle de 1-2 sur l'entité la plus proche", "Iteration": "+1 joueur par tour", "Placement": "Plus de 2 cases des joueurs proches du boss"},
    3: {"Nom": "Malédiction", "Passif": "150 Msoin", "Effet": "DO terre + 1 incurable sur le joueur le plus affaibli", "Iteration": "+1 niveau d'incurable par tour", "Placement": " "},
    4: {"Nom": "Cyclone", "Passif": "10% VdV", "Effet": "DO air, pousse le joueur de 2 cases", "Iteration": "+1 case par tour", "Placement": "Stab si danger"},
    5: {"Nom": "Oblitération", "Passif": "100 Mdos", "Effet": "DO feu anneau de PO 13-30 autour de rushu", "Iteration": "Baisse la taille minimale de l'anneau de 1", "Placement": "13 - (Nb Tour de la phase) proche du boss"},
    6: {"Nom": "Massacre", "Passif": "100 Mmonocible", "Effet": "Do feu en cercle 3 autour de rushu", "Iteration": "Augmente la taille du cercle de 1", "Placement": "3 + (nb tour de la phase) éloigné du boss"},
    7: {"Nom": "Dévastation", "Passif": "100 Mzone", "Effet": "Do feu anneau 5-8 autour de l'entité la plus proche de Rushu", "Iteration": "+1 joueur par tour", "Placement": "Moins de 5 ou plus de 8 des joueurs impactés"},
    8: {"Nom": "Météore", "Passif": "15 DF en ligne", "Effet": "Do Feu, pose un glyphe cercle de 3 sur 3 joueurs", "Iteration": "+1 taille et +1 joueur par tour", "Placement": "Ne pas se placer sur les glyphes"},
    9: {"Nom": "Grêle", "Passif": "100 Mmélée", "Effet": "Do eau sur l'entité la plus proche de rushu", "Iteration": "+1 entité par tour", "Placement": "Tank/invoc proche de Rushu"},
    10: {"Nom": "Tonnerre", "Passif": "100 Mdistance", "Effet": "Do air sur l'entité le plus éloigné de Rushu", "Iteration": "+1 entité par tour", "Placement": "Tank/invoc éloigné de Rushu"},
    11: {"Nom": "Obscurité", "Passif": "15DF côté", "Effet": "Prison autour des joueurs si traversé DO stasis et -1PO 2 tours", "Iteration": "nb de dégats et rall PO augmenté", "Placement": "Si P4, restez proche du boss"},
    12: {"Nom": "Ressac", "Passif": "1PA", "Effet": "DO eau et rall rési sur l'entité la plus affaibli", "Iteration": "+40 rall rési", "Placement": ""},
    13: {"Nom": "Ouragan", "Passif": "+10% Armure donnée", "Effet": "Do air, attire de 2 cases", "Iteration": "+1 case attiré", "Placement": "  sauf si ordre artefact cringe alors stab si danger"},
    14: {"Nom": "Fracas", "Passif": "10% Df convertit en armure", "Effet": "Do terre, -1pm + stab", "Iteration": "rall PM +1", "Placement": " "},
    15: {"Nom": "Explosion", "Passif": "10% armure reçu", "Effet": "Do terre anneau 4 - 6", "Iteration": "+1 PO max", "Placement": "Moins de 3 ou plus (6+Nb de tour)"},
    16: {"Nom": "Grondement", "Passif": "150% Berserk", "Effet": "invoque 2 rochers autour de Rushu détruire un rocher retire 2PM", "Iteration": "+2 rocher par tour", "Placement": " "},
}

create_artefact_checkboxes()
# Création d'un cadre pour afficher les informations sélectionnées
info_frame = tk.Frame(root)
info_frame.pack(fill='both', expand=True)

# Bandeau pour afficher l'état actuel
phase_label = tk.Label(root, text=f"Phase {current_phase}", font=("Arial", 16), bg="orange")
phase_label.pack(fill='x')


# Bouton pour gérer le changement de phase
phase_button = tk.Button(root, text="Phase Suivante", command=handle_phase)
phase_button.pack()

# Bouton de réinitialisation qui redémarre l'application
reset_button = tk.Button(root, text="Reset", command=restart_app)
reset_button.pack()

# Lancement de l'interface utilisateur
root.mainloop()