import mbta_api

hello  = mbta_api.create_lines_list("https://api-v3.mbta.com")

for i in range(len(hello)):
    print(hello[i])