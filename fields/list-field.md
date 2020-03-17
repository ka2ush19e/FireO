---
layout: default
title: List Field
parent: Fields
nav_order: 5
---

# List Field

{: .no_toc }

## Table of contents

{: .no_toc .text-delta }

1. TOC
   {:toc}

---

Array field for Firestore

## Example Usage

```python
class User(Model):
    subjects = ListField()



u = User()
u.subjects = ['English', 'Math']
```

## Allowed Attributes

The following attributes supported by List Field.

1. [default](#default)
2. [required](#required)
3. [column_name](#column-name)
4. [validator](#validator)

- ### Default

  Default value for field. This is base attribute that is available in all fields. [Read More](/FireO/fields/field#default)

- ### Required

  Set `True` if value is required for the field. This is base attribute that is available in all fields. [Read More](/FireO/fields/field#required)

- ### Column Name

  Set different column name in Firestore instead of field name. This is base attribute that is available in all fields. [Read More](/FireO/fields/field#column-name)

- ### Validator
  Validate given value of field. This is base attribute that is available in all fields [Read More](/FireO/fields/field#validator)