import csv


dane = [
    [1, "Ala,kot", 3],
    [2, "Ala", 3],
    [3, "Xxx,yyy", 3]
]

"""
1;Ala,kot;3
2;Ala;3
3;Xxx,yyy;3
"""

"""
1,"Ala,kot",3
2,Ala,3
3,"Xxx,yyy",3

"""

with open("data.csv", "w") as f:
    writer = csv.writer(f, delimiter=",", quotechar="|")
    writer.writerows(dane)