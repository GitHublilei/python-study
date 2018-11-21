def greet_user(pet_name, animal_type="dog"):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

greet_user(pet_name="harry")
greet_user(pet_name="harry", animal_type="hamster")
greet_user(pet_name="xiaohei")

