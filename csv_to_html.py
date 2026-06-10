import csv
import html


def csv_to_html_table(csv_file, output_file="table.html"):
    with open(csv_file, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV file is empty.")

    headers = rows[0]
    data_rows = rows[1:]

    # Find the Cost column
    try:
        total_cost_index = headers.index("Cost")
    except ValueError:
        raise ValueError('CSV must have a column named "Cost".')

    # Calculate Cost
    total_cost = 0

    for row in data_rows:
        if len(row) > total_cost_index and row[total_cost_index].strip() != "":
            total_cost += float(row[total_cost_index])

    html_code = ""

    html_code += "<table>\n"
    html_code += "    <thead>\n"
    html_code += "        <tr>\n"

    for header in headers:
        html_code += f'            <th style="color: white;">{html.escape(header)}</th>\n'

    html_code += "        </tr>\n"
    html_code += "    </thead>\n"
    html_code += "    <tbody>\n"

    for row in data_rows:
        html_code += "        <tr>\n"

        for cell in row:
            html_code += f"            <td>{html.escape(cell)}</td>\n"

        html_code += "        </tr>\n"

    # Add final total row
    html_code += "        <tr>\n"

    for i in range(len(headers)):
        if i == 0:
            html_code += '            <td><strong>Total</strong></td>\n'
        elif i == total_cost_index:
            html_code += f"            <td><strong>{total_cost:.2f}</strong></td>\n"
        else:
            html_code += "            <td></td>\n"

    html_code += "        </tr>\n"

    html_code += "    </tbody>\n"
    html_code += "</table>"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_code)

    return html_code


# Example use
html_table = csv_to_html_table("BOM.csv", "parts_table.html")

print(html_table)