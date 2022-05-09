import json

parser = json.JSONDecoder()
parsed = []  # a list to hold individually parsed JSON structures
with open('try_twitterdata.json') as f:
    data = f.read()
head = 0  # hold the current position as we parse
while True:
    head = (data.find('{', head) + 1 or data.find('[', head) + 1) - 1
    try:
        struct, head = parser.raw_decode(data, head)
        parsed.append(struct)
    except (ValueError, json.JSONDecodeError):  # no more valid JSON structures
        break

print(json.dumps(parsed, indent=2))  # make sure it all went well