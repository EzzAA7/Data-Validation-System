# Data-Validation-System
In some cases, you want to check that a given data is valid, before doing some operations on it(for example storing it to database). So instead of validating every data manually, it’s better to create a general validation rules that validate any data, then f the validation rules pass, your code will keep executing normally ; however, if validation fails a validation error messages will be shown to describe which fields have failed to pass. 

Given A python dictionary that have multi-level data. It builds validation rules for the data in that dictionary.
