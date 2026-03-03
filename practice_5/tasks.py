import re 
with open("raw.txt", "r", encoding="utf-8") as f:
    raw = f.read()


pattern = r"x\s(\d+.*)"
prices = re.findall(pattern, raw)
print("="*5, "Task 1", "="*5)
print("All prices: ", *prices)

pattern = r"\d+\.\s(.+)"
products = re.findall(pattern, raw)
print('='*5, "Task 2", '='*5)
print("All products: ")
print(*products, sep='\n')

pattern = r"Стоимость\n(\d+.*)"
total = re.findall(pattern, raw)
res = 0
print('='*5, "Task 3", '='*5)
for i in total:
    i = i.replace(',', '.')
    i = i.replace(' ', '')
    res += float(i)
print("Total: ", res)

pattern = r"(\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2})"
date = re.findall(pattern, raw)
print("="*5, "Task 4", '='*5)
print(*date)

pattern = r"(Банковская карта|Наличные|Kaspi|Visa|MasterCard)"
payment = re.findall(pattern, raw)
print('='*5, "Task 5", '='*5 )
print(*payment)

#Task 6
import json 

data = dict()
data["prices"] = prices 
data["products"] = products
data["total"] = res 
data["date"] = date 
data["payment"] = payment 
s = json.dumps(data, separators= (":" , ","))

with open("data.json", 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)