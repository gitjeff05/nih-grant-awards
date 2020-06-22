# NIH Awards Analysis

This project aims to analyze and provide some summary statistics for [NIH grant award data from ExPORTER data files](https://exporter.nih.gov/about.aspx).

### For fiscal years 2019 and 2020, the NIH has funded:

<img src="https://user-images.githubusercontent.com/548922/85337721-f5d66880-b4ae-11ea-80ed-c204947de808.png" alt="Summary statistics for NIH grant award data" style="text-align:center"/>

<img src="https://user-images.githubusercontent.com/548922/85338207-d429b100-b4af-11ea-8f0e-08c227867227.png" alt="Rolling median for select NIH administering agencies" style="text-align:center"/>

# Preprocessing the data with Preprocessing.ipynb

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
├── Analysis.ipynb                                               # this notebook
├── Preprocess.ipynb                                             # preprocessing notebook
├── CHANGELOG.md                                                 # When data or models are generated, a corresponding entry goes here
├── README.md                                                    # Project details
├── data
│   ├── exporter                                                 # exporter files (not included in repo) 
│   ├── geo                                                      # shapefiles for maps
│   │   └── cb_2019_us_state_500k.{cpg,dbf,prj,shp,shx,xml}
│   └── zips                                                     # Zip to lat/long
│       └── us-zip-code-latitude-and-longitude.csv 
├── out
│   ├── csv                                                      # output of preprocessing
│   │   └── post_processed_2020-05-29T12:36:20+00:00.csv.gzip    # sample (Note: this is not the entire dataset, see utils/get_csvs for script to get all files for yourself)
│   ├── json                                                     # any json output goes here
│   └── models                                                   # any saved models go here
├── styles                                                       
│   └── styles-nih.css                                           # external styles
└── utils
    ├── get_csvs                                                 # function to get data
    ├── reporter_files.txt                                       # list of reporter files to retrieve
    └── style_dataframes.py                                      # Helper methods to style dataframes  

9 directories, 19 files
```
