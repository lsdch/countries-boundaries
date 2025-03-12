# About

A simplified dataset of world countries boundaries, including their maritime exclusive economic zones (EEZ).

Original dataset was retrieved from [Marine Regions](https://www.marineregions.org/sources.php#unioneezcountry),
transformed from Shapefile to GeoJSON,
and then filtered to remove ambiguous areas, i.e. "Joint regime" and "Overlapping claim".

## Usage

```sh
python scripts/processing.py
```

Outputs to `output/countries.json` as GeoJSON


## Reference
Flanders Marine Institute (2024). Union of the ESRI Country shapefile and the Exclusive Economic Zones (version 4).
Available online at https://www.marineregions.org/.
https://doi.org/10.14284/698.
Consulted on 2025-03-12.