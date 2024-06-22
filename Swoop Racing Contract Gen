def generate_contract():
    print("Welcome to the Star Wars Swoop Racing Contract Generator")
    print("Please enter the following information to begin your registration:")

    pilot_name = input("Pilot's Name: ")
    home_planet = input("Home Planet: ")
    identification_number = input("Identification Number: ")

    event_date = input("Event Date (DD/MM/YYYY): ")
    event_location = input("Event Location: ")
    prize_description = input("Description of Winner's Prize: ")

    print("\nLet's proceed with the registration.")
    print(f"You are about to register for the thrilling swoop race at {event_location} on {event_date}.")
    confirmation = input("Are you ready to continue with the registration? (y/n): ").lower()

    if confirmation != 'y':
        print("No problem! You can come back when you're ready for the swoop adventure.")
        return

    # Generate the contract
    contract = f"""
    **Swoop Racing Participation Contract**

    **Parties Involved:**

    **Event Provider:**
    Galactic Swoop Racing League
    Coruscant, Space Sector 1138

    **Participant:**
    Pilot's Name: {pilot_name}
    Home Planet: {home_planet}
    Identification Number: {identification_number}

    **Terms and Conditions:**

    1. **Purpose of the Contract:**
    The Participant agrees to compete in the swoop race organized by the Galactic Swoop Racing League,
    scheduled to take place on {event_date} at {event_location}.

    2. **Participant's Obligations:**
       - The Participant shall provide their own swoop in suitable condition for the competition.
       - Maintain sportsmanlike behavior and comply with rules and regulations set forth by the event organizer.
       - Participate in practice and qualifying sessions prior to the event.

    3. **Swoop Modifications:**
       - No modifications that affect fair and equitable race performance are allowed, as regulated in swoop races on Taris, Manaan, and other key planets. Any participant caught using tricked-out or illegally enhanced parts will be immediately disqualified and their ship confiscated by The League.

    4. **Doping:**
       - The use of performance-enhancing substances is strictly prohibited during the competition, in accordance with the Galactic Senate's anti-doping laws. Any participant found using doping will be immediately disqualified and may face additional penalties from the Galactic Swoop Racing League.

    5. **Prize:**
       - The prize for the winner of the race will be {prize_description}, as customary in prestigious swoop competitions.

    6. **Final Provisions:**
       - This contract enters into force upon acceptance by both parties and remains valid until the conclusion of the event.

    May the Force be with you in this thrilling race!

    Participant's Signature: _______________________

    Date: _______________

    Accepted by Galactic Swoop Racing League:

    Signature: _______________________

    Date: _______________
    """

    print("\nContract Successfully Generated!")
    print(contract)

generate_contract()
