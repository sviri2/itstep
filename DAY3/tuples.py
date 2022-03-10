# tuple  სია . აბსოლუტურად იგივე რაც list .განსხვავებაა რომ ის არ არის ცვლადი სია - unchangeable მარა ordered
#  ანუ შეგვიძლია ცვლილება ელემენტების და ასევე ელემენტები შეგვიძლია დავნომრით
# ამ სიაში ელემენტები იწერება () ით
# my_tuple = ("levani", "irakli", "nino", "nana", "ezekia")
# my_tuple[3] = "kachapuri"
# print(tuple[3])

# ჩვენ ამ სიაში შეგვიძლია შევქმნატ დუბლიკატი ჩანაწერი
my_tuple2 = ("levani", "irakli", "nino", "nana", "levani")
# print(my_tuple2)
print(my_tuple2[1:3])     #amobeWdva 1-2
# my_tuple2.append("soko")  #damateba არ ემატება რადგან tuple არ იცვლება
my_tuple2[3] = "lobiani"    # არენაცვლება
