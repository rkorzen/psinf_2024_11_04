import re


with open("../data/data.txt") as f:
    dane = f.read()

print(dane)

post_code_pattern = re.compile("\d{2}-\d{3}")
email_pattern = re.compile("[\w\-\.]+@(?:\w+\.)+\w+")  # com.pl
date_pattern = re.compile("\d{2} \w{3} \d{4}")


print("kody pocztowe", post_code_pattern.findall(dane))
print("emaile", email_pattern.findall(dane))
print("daty", date_pattern.findall(dane))