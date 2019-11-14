# Rwalocation
> A Python library for listing locations in Rwanda 

```
USAGE

1.
>>> import rwalocation 
>>> rwalocation.province()
Returns a list of all provinces
>>> [{'id': '84b17f22-c14e-4931-98b2-bdf0cfd90090', 'country_code': 'RWA', 'country_name': 'RWANDA', 'province_code': 5, 'province_name': 'EAST', 'district_code': 501, 'district_name': 'Rwamagana', 'sector_code': '050114', 'sector_name': 'Rubona', 'cell_code': 5011406, 'cell_name': 'Nawe', 'village_code': 501140603, 'village_name': 'Rudashya'}, ...]

2. 
>> from rwalocation import district
>>> district()
results
>>> [{'district_name': 'Bugesera', 'district_code': 507, 'province_name': 'EAST'}, ...]

```
