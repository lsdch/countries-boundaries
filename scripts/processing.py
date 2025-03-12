import json

def load_json(path: str) -> dict:
    print(f"Loading {path}")
    with open(path, "r") as f:
        return json.load(f)


def main():
    geojson_data = load_json("data/EEZ_land_union_v4_202410.json")
    # country_codes = load_json("data/countries-codes.json")
    with open("output/countries.json", "w") as f:
        print("Filtering data")
        filtered_features = [
            feature for feature in geojson_data['features']
            if feature['properties']['POL_TYPE']
            in ['Landlocked country', 'Union EEZ and country']
        ]
        print("Writing data to: ./output/countries.json")
        f.write(json.dumps(filtered_features) + "\n")


if __name__ == "__main__":
    main()
