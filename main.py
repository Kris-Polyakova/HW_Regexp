import csv

from src.get_formatted_contacts import get_formatted_contacts

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
    datawriter.writerows([[str(c)] for c in get_formatted_contacts(contacts_list)])
