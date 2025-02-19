import sys, json
file_values, file_tests, file_report = sys.argv[1:]
with open(file_tests, encoding="utf-8") as f:
    tests = json.load(f)
with open(file_values, encoding="utf-8") as f:
    values = json.load(f)

def search_and_fill(directory):
    for i in directory:
        try:
            search_and_fill(i['values'])
        except:
            pass
        if i['value'] == "":
            i['value'] = results[i['id']]

results = {i['id'] : i['value'] for i in values['values']}
search_and_fill(tests["tests"])
with open(file_report, "w", encoding="utf-8") as f:
    json.dump(tests, f, indent=2, ensure_ascii=False)