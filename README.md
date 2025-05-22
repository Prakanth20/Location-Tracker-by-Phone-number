# 📍 Phone Number Location Tracker

This Python-based application allows you to track the approximate location of a phone number using public data and APIs. It provides geolocation information and visualizes the location on an interactive map.

## ⚙️ Features

* Extract country and carrier details from a phone number
* Get geographical coordinates using OpenCage Geocoder
* Display the location on an interactive map using Folium

## 🧰 Requirements

Install the necessary dependencies:

```bash
pip install phonenumbers
pip install folium
pip install geocoder
pip install opencage
```

## 🔐 OpenCage API Key

You will need an API key from [OpenCage Geocoder](https://opencagedata.com/api) to use this tool.

Sign up for a free account, get your API key, and include it in your script like this:

```python
from opencage.geocoder import OpenCageGeocode

key = 'YOUR_OPENCAGE_API_KEY'
geocoder = OpenCageGeocode(key)
```

## 🚀 Usage

1. Run the script:

```bash
python tracker.py
```

2. Input the phone number in international format (e.g., `+14155552671`).

3. The script will:

   * Parse and extract location details
   * Use OpenCage to get latitude and longitude
   * Generate an HTML map with a marker for the location

## 📎 Example Output

* Country: United States
* Carrier: Verizon
* Location: Mountain View, California
* Map: Opens in your browser or saved as `location.html`

## ⚠️ Disclaimer

This tool provides **approximate** location data based on the number's registered area and is **not** capable of real-time GPS tracking. It does **not** invade privacy or access personal phone data.
