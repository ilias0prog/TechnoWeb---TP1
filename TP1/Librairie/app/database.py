bookstore = {
    # Clé = isbn de forme ""
    "books" : [{
        "id" : "0001",
        "name" : "La conquête de l'espace",
        "author" : "Elon Musk",
        "editor" : "Mc Donalds"
    },
    {
        "id" : "0002",
        "name" : "Python pour les nuls",
        "author" : "Benois Frénay",
        "editor" : "Maison Frénay"
    },
    {
        "id" : "0003",
        "name" : "Tchoupi à l'école",
        "author" : "Erwin",
        "editor" : "Kurtis Production"
    },
    {
        "id" : "0004",
        "name" : "La poule et le lapin",
        "author" : "Jean de La Fontaine",
        "editor" : "Edition Hachette"
    },
    {
        "id" : "0005",
        "name" : "Les bons, le con et le mouton",
        "author" : "Ryan, Ilias",
        "editor" : "Universal"
    },
      {"id": "0006",
        "name" : "100 recettes faciles maison",
        "author" : "Agnès Dupont",
        "editor" : "Test cuisine"
    },
      {   "id": "0007",
        "name" : "Encyclopédie du football",
        "author" : "Kiki Mbappe",
        "editor" : "Le Football Il a Changé"
    }
]
}


a = bookstore.__getitem__()
print(a)