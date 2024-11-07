import json

text = """
{
    "x": 1,
    "y": [
        1,
        2,
        3
    ]
}

"""

# json.loads

data = json.loads(text)
data["z"] = {"a": 1, "c": "żążółć gęślą jaźń"}
print(data, type(data))

# json.dumps
print(json.dumps(data))

# json.load

with open("dane.json") as f:
    print(json.load(f))

# json.dump


with open("dane2.json", "w") as f:
    json.dump(data, f)