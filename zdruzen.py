import os


if not os.path.exists("stran"):
    os.makedirs("stran")

input_directory = "strani"
output_directory = "stran"

html_dats = [dat for dat in os.listdir(input_directory) if dat.endswith(".html")]


merged_html = ""
for html_dat in html_dats:
    with open(os.path.join(input_directory, html_dat), "r", encoding="utf-8") as f:
        merged_html += f.read()


output_path = os.path.join(output_directory, "merged.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(merged_html)

print(f"Merged HTML saved to: {output_path}")
