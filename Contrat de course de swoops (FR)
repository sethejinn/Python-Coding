def generer_contrat():
    print("Bienvenue sur le générateur de contrat de course de swoops!")
    print("Veuillez entrer les informations suivantes pour commencer votre inscription :")

    nom_pilote = input("Nom du Pilote : ")
    planete_origine = input("Planète d'Origine : ")
    numero_identification = input("Numéro d'Identification : ")

    date_evenement = input("Date de l'Événement (JJ/MM/AAAA) : ")
    lieu_evenement = input("Lieu de l'Événement : ")
    description_prix = input("Description du Prix pour le Vainqueur : ")

    print("\nParfait ! Procédons à l'inscription.")
    print(f"Vous êtes sur le point de vous inscrire à la passionnante course de swoops à {lieu_evenement} le {date_evenement}.")
    confirmation = input("Êtes-vous prêt à continuer l'inscription ? (o/n) : ").lower()

    if confirmation != 'o':
        print("Pas de problème ! Vous pouvez revenir lorsque vous serez prêt pour l'aventure swoop.")
        return

    contrat = f"""
    **Contrat de Participation à la Course de Swoops**

    **Parties Impliquées :**

    **Organisateur de l'Événement :**
    Galactic Swoop Racing League
    Coruscant, Secteur Spatial 1138

    **Participant :**
    Nom du Pilote : {nom_pilote}
    Planète d'Origine : {planete_origine}
    Numéro d'Identification : {numero_identification}

    **Termes et Conditions :**

    1. **Objet du Contrat :**
    Le Participant s'engage à participer à la course de swoops organisée par la Galactic Swoop Racing League,
    prévue le {date_evenement} à {lieu_evenement}.

    2. **Obligations du Participant :**
       - Le Participant doit fournir son propre swoop en bon état pour la compétition.
       - Maintenir un comportement sportif et respecter les règles et réglementations établies par l'organisateur de l'événement.
       - Participer aux sessions d'entraînement et de qualification avant l'événement.

    3. **Modifications du Swoop :**
       - Aucune modification affectant la performance équitable de la course n'est autorisée, conformément aux régulations des courses de swoops sur Taris, Manaan et autres planètes clés. Tout participant surpris en train d'utiliser des pièces truquées ou améliorées illégalement sera immédiatement disqualifié et son vaisseau confisqué par La Ligue.

    4. **Dopage :**
       - L'utilisation de substances dopantes est strictement interdite pendant la compétition, conformément aux lois anti-dopage du Sénat Galactique. Tout participant surpris en train de se doper sera immédiatement disqualifié et pourrait faire face à des sanctions supplémentaires de la part de la Galactic Swoop Racing League.

    5. **Prix :**
       - Le prix pour le vainqueur de la course sera {description_prix}, comme le veut la tradition dans les compétitions prestigieuses de swoops.

    6. **Dispositions Finales :**
       - Ce contrat entre en vigueur dès son acceptation par les deux parties et reste valide jusqu'à la conclusion de l'événement.

    Que la Force soit avec vous dans cette course palpitante !

    Signature du Participant : _______________________

    Date : _______________

    Accepté par la Galactic Swoop Racing League :

    Signature : _______________________

    Date : _______________
    """

    print("\nContrat Généré avec Succès !")
    print(contrat)


generer_contrat()
