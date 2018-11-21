responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is you name?")
    response = input("which mountain would you like to cllimb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n--- poll results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

