import re
from models.contact import Contact

def get_formatted_contacts(contacts_list):
    unique_contacts = []
    for con in contacts_list[1:]:
        data = f'{con[0]} {con[1]} {con[2]}'
        data = data.replace('  ', ' ')
        argument = data.split(' ')
    
        phone = re.sub(r'[^\d]', '', con[5])
        
        if len(phone) == 15:
            groups = re.findall(r'\d{3}', phone[1:7])
            groups2 = re.findall(r'\d{2}', phone[7:11])
            formatted_phone = (f'+7({groups[0]})'
            f'{groups[1]}-{groups2[0]}-{groups2[1]} доб.{phone[11:]}')
        if len(phone) == 11:
            groups = re.findall(r'\d{3}', phone[1:7])
            groups2 = re.findall(r'\d{2}', phone[7:])
            formatted_phone = (f'+7({groups[0]})'
            f'{groups[1]}-{groups2[0]}-{groups2[1]}')
        if len(phone) < 11:
            formatted_phone = ''
            
        contact = Contact(argument[0], argument[1], argument[2], formatted_phone)
        
        if contact not in unique_contacts:
           unique_contacts.append(contact)
        else: 
            idx = unique_contacts.index(contact)
            dup = unique_contacts[idx]
            dup.add_phone(contact.get_phone())
            
    return unique_contacts