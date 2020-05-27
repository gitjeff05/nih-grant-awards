# NIH Awards Analysis


This project aims to analyze and provide some summary statistics for [NIH grant award data from ExPORTER data files](https://exporter.nih.gov/about.aspx).

<img src="https://user-images.githubusercontent.com/548922/82957080-33afa200-9f80-11ea-94a8-09586fdb9c43.png" alt="Summary statistics for NIH grant award data" style="text-align:center"/>

## Preprocessing the data with Preprocessing.ipynb

### The notebook and relevant directories

The data are cleaned and preprocessed in the `Preprocessing.ipynb` notebook. This is meant to be run against the raw data from `./data/exporter` and the output is saved to `./out/csv` with the format: `out/csv/post_processed_{ISO_DATE}.csv.gzip`.

### Fetching the data

This project does not house the ExPORTER data files (~200MB). As a convenience, we include a bash script `./utils/get_csvs` which programmatically downloads all of the files listed in `./utils/reporter_files.txt`. Once you have the exporter files downloaded in the `./data/exporter` directory, the preprocessing notebook will be able to find them. The files list in `reporter_files.txt` is up to date at the time of this publishing. However, as new files are added weekly, you should add the new files to `reporter_files.txt` and re-run `./utils/get_csvs`. A more efficient way might be to just download the new file directly to `./data/exporter` with `curl` like so:

```bash
> curl https://exporter.nih.gov/CSVs/final/RePORTER_PRJ_C_FY2020_031.zip -o "./data/exporter/RePORTER_PRJ_C_FY2020_031.zip"
```

### Converting column dtypes

Any column meant to represent a date is converted to `datetime64[ns]` using `pandas.to_datetime`. Some columns that are strings are explicitly converted to `StringDtype` as it is [the recommended way to store strings in pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html).

### Dropping rows:

Some rows are dropped during preprocessing as they would be unhelpful for analysis. This is primarily because they:

- have no associated costs
- are duplicates of another award

When filtering out the above cases, about 3.433% of rows were dropped.

Although ~98.3% of ExPORTER data reference awards that are administered by an NIH agency, the data also includes awards from other government agencies (CDC, FDA, VA). Since this analysis is only relevant to NIH, rows that are not NIH awards are dropped. Also, we drop all rows where `ORG_COUNTRY` ("country in which the business office of the grantee organization or contractor is located") is *not* the United States.

### Geospatial data

Since all US award data have related zip codes for the organization, we added additional columns for lat/long coordinates. The "[US Zip Code Latitude and Longitude](https://public.opendatasoft.com/explore/dataset/us-zip-code-latitude-and-longitude/information/)" by [CivicSpace Labs]() is licensed under [Creative Commons Attribution-ShareAlike](https://creativecommons.org/licenses/by-sa/2.0/). Copyright 2004 CivicSpace Labs.

## Project Structure

```bash
.
├── Analysis.ipynb # Analysis
├── LICENSE
├── Preprocess.ipynb
├── README.md
├── data
│   ├── geo
│   │   ├── cb_2019_us_state_500k.cpg
│   │   ├── cb_2019_us_state_500k.dbf
│   │   ├── cb_2019_us_state_500k.prj
│   │   ├── cb_2019_us_state_500k.shp
│   │   ├── cb_2019_us_state_500k.shp.ea.iso.xml
│   │   ├── cb_2019_us_state_500k.shp.iso.xml
│   │   └── cb_2019_us_state_500k.shx
│   └── zips
│       └── us-zip-code-latitude-and-longitude.csv
├── out
│   ├── csv
│   │   └── post_processed_2020-05-14T15:17:56+00:00.csv.gzip
│   ├── json
│   └── models
├── styles
│   └── styles-nih.css
└── utils
    ├── get_csvs
    └── reporter_files.txt

9 directories, 19 files
```



- 