# isimlere masa numarası atıyoruz
table_numbers = {
    "gara": 7,
    "hasan": 5,
    "omer": 8
}

invitation_list_forToday = ["gara", "hasan", "omer"]
invitation_list_forTomorrow = ["john", "dmitri"]

isim = input("Please write your name: ").lower()

if isim in invitation_list_forToday:
    masaNo = table_numbers.get(isim, 0)  # 0 default değer
    print(masaNo, "number of table, please come in")
elif isim in invitation_list_forTomorrow:
    print("So sorry, your invitation is for tomorrow :(")
else:
    print("We don’t have any invitation for you..")