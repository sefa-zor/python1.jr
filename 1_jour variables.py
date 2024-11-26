
#job 1, 2 et 3
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)
#job 4
alphabet = "a b c d e f g h i j k l m n o p q r s t u v x y z"
print(alphabet)
#job 5
print(alphabet [::-1])
#job 6
ma_string = "Je suis une String"
print(ma_string)
#job 7
num1 = 40
num2 = 2
print(num1 + num2)
#job 8
num1 = 3
num2= 14
print(num1, num2)
#job 9
nom = "chocolat"
prix_unitaire = 2
quantite_en_stock = 10
info_du_produit = (f"il y a {quantite_en_stock} {nom} en_stock vendu à {prix_unitaire} euros. " )
print(info_du_produit)
prix_unitaire = (prix_unitaire*1.1)
print(prix_unitaire)
prix = str(prix_unitaire)
demande_de_client = 3
ajout_de_stock = 1
stock_actuel = (quantite_en_stock + ajout_de_stock - demande_de_client)
print(stock_actuel)
stock = str(stock_actuel)
info_du_produit = (f"il y a {quantite_en_stock} {nom} en_stock vendu à {prix_unitaire} euros. " )
print(info_du_produit)
#job 10
montant_initial = 1000
taux_rend_annuel = 0.05
gain_annuel = montant_initial*taux_rend_annuel
print(gain_annuel)
montant_total = montant_initial + gain_annuel
print(montant_total)
montant_augmente = montant_total + 5000
print(montant_augmente)
taux_rend_annuel_actu = taux_rend_annuel + taux_rend_annuel*0.02
print(taux_rend_annuel_actu)
gain_annuel_actu = montant_augmente*taux_rend_annuel_actu
print(gain_annuel_actu)
montant_total = montant_augmente + gain_annuel_actu
print(montant_total)
montant_retire = montant_total*0.10
montant_total= montant_total - montant_retire
print(montant_total)
taux_rend_annuel_actu = taux_rend_annuel_actu - taux_rend_annuel_actu*0.01
print(taux_rend_annuel_actu)
gain_annuel_actu = montant_total*taux_rend_annuel_actu
print(gain_annuel_actu)
montant_final = montant_total + gain_annuel_actu
print(montant_final)
#Pour aller plus loin
text = "Il me faut un e."
if "e" in text:
    print("oui")
else:
    print("non")