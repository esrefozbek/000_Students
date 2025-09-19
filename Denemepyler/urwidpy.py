from InquirerPy import inquirer

seçilenler = inquirer.checkbox(
    message="Silmek istediklerinizi seçin:",
    choices=["Ahmet", "Ayşe", "Mehmet"]
).execute()

print(seçilenler)


