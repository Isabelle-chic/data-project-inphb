
def Parse_model(x,use_columns):
    if "Survived" not in x.columns:
        raise ValueError("la valeur cible  doit être dans le jeu de donnee")
    target=x["Survived"]
    x=x[use_columns]
    return x, target