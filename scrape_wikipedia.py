import requests
from bs4 import BeautifulSoup


def extract_info():
    wikiurl = "https://el.wikipedia.org/wiki/%CE%9A%CE%B1%CF%84%CE%AC%CE%BB%CE%BF%CE%B3%CE%BF%CF%82_%CF%84%CE%B1%CF%87%CF%85%CE%B4%CF%81%CE%BF%CE%BC%CE%B9%CE%BA%CF%8E%CE%BD_%CE%BA%CF%89%CE%B4%CE%B9%CE%BA%CF%8E%CE%BD_%CF%84%CE%B7%CF%82_%CE%95%CE%BB%CE%BB%CE%AC%CE%B4%CE%B1%CF%82"

    response = requests.get(wikiurl)

    soup = BeautifulSoup(response.text, 'html.parser')
    tk_table = soup.find_all('table', {'class': "wikitable"})
    tk_table = tk_table[1]
    rows = tk_table.find_all("tr")
    header_cols = rows[0].find_all('th')
    header_names = [x.text for x in header_cols]

    table_data = []
    for row in rows[1:]:
        col_data = []
        for col in row:
            col_data.append(col.text)
        table_data.append(col_data)

    striped_table = []
    for row in table_data:
        row_data = []
        for i in row:
            row_data.append(i.strip())
        striped_table.append(row_data)

    cleaned_data_table = []
    for x in striped_table:
        remove_empty_strings = [y for y in x if y]
        cleaned_data_table.append(remove_empty_strings)

    final_table = []
    for i, data in enumerate(cleaned_data_table):
        if len(data) < 4:
            for missing_data in cleaned_data_table[i-1][len(data):]:
                data.append(missing_data)
        data[0] = data[0].replace(" ", "")
        data[0] = data[0].replace("Χ", "0")
        final_table.append(data)

    strip_header_names = []
    for i in header_names:
        strip_header_names.append(i.strip())

    context = []
    for data in final_table:
        dict_table = {}
        for key, value in zip(strip_header_names, data):
            dict_table[key] = value
        context.append(dict_table)

    return context


# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct


# l = ['giannis', 'bratias']
# print(Convert(final_table[0]))
