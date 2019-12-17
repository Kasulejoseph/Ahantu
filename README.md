# Rwanda Locations 
[![Build Status](https://travis-ci.com/Kasulejoseph/Ahantu.svg?branch=master)](https://travis-ci.com/Kasulejoseph/Ahantu)
[![Coverage Status](https://coveralls.io/repos/github/Kasulejoseph/Ahantu/badge.svg?branch=tests)](https://coveralls.io/github/Kasulejoseph/Ahantu?branch=tests)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8e6d206d92344ce881cc29241dea1929)](https://www.codacy.com/manual/Kasulejoseph/Ahantu?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Kasulejoseph/Ahantu&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/rwalocation.svg)](https://badge.fury.io/py/rwalocation)
> A Python library for listing locations in Rwanda 

## Installation
```
pip install rwalocation
```
## Features
1. All locations
2. Provinces
3. Places in specific province
4. Districts
5. Places in a specific district
6. places with contain specified name.
## USAGE
```
1.
>>> from rwalocation import location
>>> location()
>>> [{'id': '84b17f22-c14e-4931-98b2-bdf0cfd90090', 'country_code': 'RWA', 'country_name': 'RWANDA', ... ]

2.
>>> import rwalocation 
>>> rwalocation.province()
>>> [{'province_name': 'EAST', 'province_code': 5}, {'province_name': 'NORTH', 'province_code': 4}, ...]

3. 
>>> rwalocation.province('Kigali')
>>> [{'id': '68028287-fe59-42ae-978e-5d24a37ada38', 'country_code': 'RWA', 'country_name': 'RWANDA', ...]

4.
>> from rwalocation import district
>>> district()
>>> [{'district_name': 'Bugesera', 'district_code': 507, 'province_name': 'EAST'}, ...]

5.
>> from rwalocation import district
>>> district('Kicukiro')
>>> [{'id': '84b17f22-c14e-4931-98b2-bdf0cfd90090', 'country_code': 'RWA', 'country_name': 'RWANDA', ...]

6.
>>> location('Rubashya') :> All locations which contain name "Rubashya"
>>> [{'id': '84b17f22-c14e-4931-98b2-bdf0cfd90090', 'country_code': 'RWA', 'country_name': 'RWANDA',... ]
```

## DATA Spec
1. Province
```
{ 
   'province_code':5,
   'province_name':'EAST',
}
```
2. District
```
{ 
   'district_name':'Bugesera',
   'district_code':507,
   'province_name':'EAST'
}
```
3. Location
```
{ 
   'id':'84b17f22-c14e-4931-98b2-bdf0cfd90090',
   'country_code':'RWA',
   'country_name':'RWANDA',
   'province_code':5,
   'province_name':'EAST',
   'district_code':501,
   'district_name':'Rwamagana',
   'sector_code':'050114',
   'sector_name':'Rubona',
   'cell_code':5011406,
   'cell_name':'Nawe',
   'village_code':501140603,
   'village_name':'Rudashya'
}
```

## Contributing 🙏
Pull requests and potential features are welcome.
1. Make all changes to your forked branch
2. Submit a Pull Request.

## Submit Issues 🐛
Facing any Issues or weird behavior(bug)? Feel free to open a [new issue](https://github.com/Kasulejoseph/Ahantu/issues/new).

## License
[MIT](http://opensource.org/licenses/MIT)
Copyright &copy; 2019, [Kasule Joseph](https://github.com/Kasulejoseph). All rights reserved.
