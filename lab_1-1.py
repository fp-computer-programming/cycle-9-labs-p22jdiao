# Author: JD 01/06/2021


rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin" "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]


for i in range(len(rows)):
    for j in range(len(rows[i])):
        check = list(rows[i][j])
        check.reverse()
        if check[0] == "s":
            rows[i][j] += "'"
        else:
            rows[i][j] += "'s"


print(rows)
