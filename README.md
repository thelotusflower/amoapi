amoCRM python API wrapper 
-------------------------

python [amoCRM](https://www.amocrm.ru/) API wrapper with a human interface for easy use

forked from [amocrm_api](https://github.com/Krukov/amocrm_api)  


Installation
============

```
pip install amoapi
```


Usage
=====


There are 7 abstraction of 5 AmoCRM objects:

- Контакт - BaseContact
- Компания  - BaseCompany
- Сделка - BaseLead
- Задача - (LeadTask, ContactTask)
- Событие - (LeadNote, ContactNote)

Settings
--------

First of all you need to define settings:

```python
from amocrm import BaseContact, amo_settings, fields
amo_settings.set('krukov@centrobit.ru', '4b332718c4c5944003af7e6389860ced', 'testcentrobit')
```


Custom field
------------

One of the features of AmoCRM in the presence of custom fields in a contact, company and lead objects

To define your custom field you need describe it:

```python
from amocrm import BaseContact, amo_settings, fields

amo_settings.set('<put user email here>', '<put user_hash here>', '<put domain here>')

class Contact(BaseContact):
    position = fields.CustomField(u'Должность')
    site = fields.CustomField(u'Сайт')
    phone = fields.EnumCustomField(u'Телефон', enum='WORK')
```

Ok, now it is ready to use and you can get, create or edit contacts:

```python
new_contact = Contact(name='Example2', company='ExampleCorp2', position='QA', phone='0001')
new_contact.site = 'http://example.com'
new_contact.save()

contact = Contact.objects.get(new_contact.id)
contact_search = Contact.objects.search('Example2')
assert contact.id == contact_search.id
print(contact.phone)
contact.phone = '8-800-00000000'
contact.save()
contact.create_task('New task, yeee', task_type=u'Звонок',
                 complete_till=datetime.datetime.now()+datetime.timedelta(days=3))
print(contact.notes)
print(contact.tasks)
```
