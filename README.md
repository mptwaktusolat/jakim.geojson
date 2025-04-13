# JAKIM Zone code based on daerah in Malaysia

**GeoJson** file containing the JAKIM zone codes based on districts (daerah) in Malaysia.

> [!NOTE]
> GeoJSON is an open standard format for representing simple geographical features, along with their non-spatial attributes. It is widely used in geographic applications and mapping services due to its simplicity and interoperability. It's supported by many GIS software systems, web mapping libraries (like Leaflet and Mapbox), and data visualization tools.

> For detailed specifications, refer to [RFC 7946](https://tools.ietf.org/html/rfc7946) or visit: https://geojson.org/

## Methodology

The original file is [malaysia.district.geojson](./malaysia.district.geojson), containing these properties for each district:

```json
"properties": {
    "name": "Baling",
    "code_state": 2,
    "state": "KDH"
},
```

- `name` is the district name, which I use to compare and match with the JAKIM information.
- `code_state` is similar to the MyKad center number.
- `state` is a short code for the state. This is not necessarily the same as the initial JAKIM code. However, I use this value to cross-check and validate the manually inputted data to ensure no errors slipped in while adding the JAKIM zones data - check [check_zones.py](./check_zones.py)

A copy of the file was created named [malaysia.district-jakim.geojson](./malaysia.district-jakim.geojson). A new item was added to the properties:

```json
"properties": {
    "name": "Kuala Selangor",
    "code_state": 10,
    "state": "SGR",
    "jakim_code": "SGR02"
},
```

Check out the **Zone Visualization tool** - an interactive tool to view maps and JAKIM zones: https://github.com/mptwaktusolat/jakim_zones_map.

## TODOs:

- Add `Bukit Larut` (Perak)

## Modifications

- `Ulu Langat` (SGR) changed to `Hulu Langat`
- `Ulu Selangor` (SGR) changed to `Hulu Selangor`
- Separated Pulau Aur & Pulau Pemanggil from `Mersing` into individual features.
- `Hulu Perak` was broken down into several mukims. A map of Hulu Perak districts was obtained from [wiki](https://ms.wikipedia.org/wiki/Hulu_Perak#/media/Fail:Map_of_Hulu_Perak_District,_Perak.svg), then using https://geojson.io/, the major mukims were traced and added to the geojson file.
- `Rompin` was split into `Rompin` & `Pulau Tioman`.

## Assumptions

Some districts in the geojson file don't have corresponding matches in the JAKIM list. I've made assumptions based on the locations of the districts and data from the Internet.

- `Maradong` (Sarawak) set to the same zone as `Sarikei`. Assumption based on the location of the districts [[wiki]](https://en.wikipedia.org/wiki/Meradong_District).
- `Tanjung Manis` (Sarawak) not in JAKIM list. Information found in [JAIS website](https://jais.sarawak.gov.my/web/subpage/webpage_view/150).
- `Asajaya` (Sarawak) set to the same zone as `Samarahan`. Assumption based on the location of the districts [[wiki]](https://en.wikipedia.org/wiki/Asajaya_District).
- `Pakan` (Sarawak) set to the same zone as `Sarikei`. Assumption based on the location of the districts [[wiki]](https://en.wikipedia.org/wiki/Pakan,_Sarawak).
- `Selangau` (Sarawak) not in the JAKIM list. Assumption based on districts that are on the same longitude axis.
- `Tebedu` (Sarawak) not in the JAKIM list. Assumption based on districts that are on the same longitude axis.
- `Telang Usan` (Sarawak) set to the same zone as `Miri`. Assumption based on the location of the districts [[wiki]](https://ms.wikipedia.org/wiki/Daerah_Telang_Usan).
- `Subis` (Sarawak) set to the same zone as `Miri`. Assumption based on the location of the districts [[wiki]](https://en.wikipedia.org/wiki/Subis_District).
- `Beluru` (Sarawak) set to the same zone as `Miri`. Assumption based on the location of the districts [[wiki]](https://en.wikipedia.org/wiki/Beluru_District).
- `Bukit Mabong` (Sarawak) not in the JAKIM list. Assumption based on districts that are on the same longitude axis.
- `Hulu Perak` (Perak) not in JAKIM list. Information taken from [Penyelarasan Zon-zon Waktu Solat Seluruh Malaysia](https://www.e-solat.gov.my/portalassets/files/Penyelarasan-Zon-Waktu-Solat.pdf).
- `Batang Padang` (Perak) not in JAKIM list. Information taken from [Penyelarasan Zon-zon Waktu Solat Seluruh Malaysia](https://www.e-solat.gov.my/portalassets/files/Penyelarasan-Zon-Waktu-Solat.pdf).
- `Manjung` (Perak) not in the JAKIM list. Using `Sitiawan` as they seem to share similar geographic space.
- `Perak Tengah` (Perak) not in JAKIM list. Information taken from [AzanPro zones](https://raw.githubusercontent.com/mptwaktusolat/mpt-server/main/json/zoneStatesData/azanProZones.json) database.
- `Kinta` (Perak) not in the JAKIM list. Information taken from [Penyelarasan Zon-zon Waktu Solat Seluruh Malaysia](https://www.e-solat.gov.my/portalassets/files/Penyelarasan-Zon-Waktu-Solat.pdf).
- `Hilir Perak` (Perak) not in the JAKIM list. Information taken from [Penyelarasan Zon-zon Waktu Solat Seluruh Malaysia](https://www.e-solat.gov.my/portalassets/files/Penyelarasan-Zon-Waktu-Solat.pdf).
- `Kerian` (Perak) not in the JAKIM list. Information taken from [Penyelarasan Zon-zon Waktu Solat Seluruh Malaysia](https://www.e-solat.gov.my/portalassets/files/Penyelarasan-Zon-Waktu-Solat.pdf).
- `Larut dan Matang` (Perak) not in the JAKIM list. Information taken from [AzanPro zones](https://raw.githubusercontent.com/mptwaktusolat/mpt-server/main/json/zoneStatesData/azanProZones.json) database.
- `Muallim` not in JAKIM list. Assumptions made from neighboring districts (Tanjung Malim/Slim River).
- `Tawau` (Sabah). From the JAKIM list, it is split into two zones, `Bahagian Tawau (Timur)` & `Bahagian Tawau (Barat)`. However, no splitting was made since areas in `Bahagian Tawau (Timur)` are already covered by other districts (e.g., `Kalabakan`). Hence, `Tawau` is considered as `Bahagian Tawau (Barat)`, since it also contains `Bandar Tawau` inside.
- `Tongod` (Sabah) not in the JAKIM list. Information taken from [JADUAL WAKTU SOLAT BAGI NEGERI SABAH TAHUN 2022](https://mufti.sabah.gov.my/images/laman-utama/zon-waktu-solat/Zon_Waktu_solat_2022/ZON_2.pdf).
- `Sandakan` (Sabah). From the JAKIM list, it is split into two zones, `Bahagian Sandakan (Timur)` & `Bahagian Sandakan (Barat)`. However, no splitting was made since areas in `Bahagian Sandakan (Timur)` are assumed to be `Kinabatangan` and `Bahagian Sandakan (Barat)` is considered as `Sandakan`, since it also contains `Bandar Sandakan` inside.
