# JAKIM Zone code based on daerah in Malaysia

## Methodology

From JAKIM website: https://www.e-solat.gov.my/, they show the JAKIM Code with their respective districts. I've collected
those information and presents it nicely in MPT-Server site: https://mpt-server.vercel.app/locations.

Now, I need the districts geofences, so that I can determine one's districts given the coordinates. Luckily, I found the districts
geojson file from [nullifye](https://github.com/nullifye): https://github.com/nullifye/malaysia.geojson

The original file is [malaysia.district.geojson](./malaysia.district.geojson), containing this properties for each districts.

```json
"properties": {
    "name": "Baling",
    "code_state": 2,
    "state": "KDH"
},
```

- `name` is the district name, I use this to compare and match with the JAKIM information.
- `code_state` is IC center number
- `state` is a short code for the state. This is not necessarily the same with the initial JAKIM code. But, I use this value to cross check and validate the data I've inputted manually to ensure there are no errors slipped in while in the process of adding the jakim zones data - check [check_zones.py](./check_zones.py)

A copy of the file is created named [malaysia.district-jakim.geojson](./malaysia.district-jakim.geojson). A new item was added to the properties.

```json
"properties": {
    "name": "Kuala Selangor",
    "code_state": 10,
    "state": "SGR",
    "jakim_code": "SGR02"
},
```

Check out Zone Visualization tool - an interactive tool to view map and jakim zones: https://github.com/mptwaktusolat/jakim_zones_map.

## TODOs:

- `Asajaya` Sarawak not in JAKIM list. Need to make an assumption.
- `Pakan` Sarawak not in JAKIM list. Need to make an assumption.
- `Selangau` Sarawak not in JAKIM list. Need to make an assumption.
- `Tebedu` Sarawak not in JAKIM list. Need to make an assumption.
- `Telang Usan` Sarawak not in JAKIM list. Need to make an assumption.
- `Subis` Sarawak not in JAKIM list. Need to make an assumption.
- `Beluru` Sarawak not in JAKIM list. Need to make an assumption.
- `Bukit Mabong` Sarawak not in JAKIM list. Need to make an assumption.
- `Hulu Perak` Perak not in JAKIM list. However, a similar zone `Hulu` is available. Need to confirm the assumption.
- `Batang Padang` Perak not in JAKIM list. Need to make an assumption.
- `Manjung` Perak not in JAKIM list. Need to make an assumption.
- `Perak Tengah` Perak not in JAKIM list. Need to make an assumption.
- `Hilir Perak` Perak not in JAKIM list. Need to make an assumption.
- `Kerian` Perak not in JAKIM list. Need to make an assumption.
- `Muallim` Perak not in JAKIM list. Need to make an assumption.
- `Kinta` Perak not in JAKIM list. Need to make an assumption.
- `Tawau` Sabah. From Jakim list, ada banyak Tawau. Need to check.
- `Sandakan` Sabah. From Jakim list, ada banyak Sandakan. Need to check.
- `Larut Dan Matang` Perak not in JAKIM list. However, a similar zone `Bukit Larut` is available. Need to confirm the assumption.
- `Tongod` Sabah not in JAKIM list. Need to make an assumption.

## Modification

- `Ulu Langat` (SGR) become `Hulu Langat`
- `Ulu Selangor` (SGR) become `Hulu Selangor`
- Seperated Pulau Aur & Pulau Pemanggil from `Mersing` to individual feature.

## Assumptions

Some districts in geojson file doesn't have corresponding match in JAKIM list. I've made some assumptions based on the location of the districts and some data from Internet.

- `Maradong` (Sarawak) set same zone as `Sarikei`. Assumption made based on location of the districts [[wiki]](https://en.wikipedia.org/wiki/Meradong_District).
- `Tanjung Manis` (Sarawak) not in JAKIM list. But found in [JAIS website](https://jais.sarawak.gov.my/web/subpage/webpage_view/150).
