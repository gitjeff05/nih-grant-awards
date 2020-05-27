# NIH Awards Analysis


This project aims to analyze and provide some summary statistics for [NIH grant award data from ExPORTER data files](https://exporter.nih.gov/about.aspx).

<img src="https://user-images.githubusercontent.com/548922/82932523-8ffdcc00-9f56-11ea-9738-faa4896034f2.png" alt="Summary statistics for NIH grant award data" style="text-align:center"/>

## Preprocessing

### Getting the data

In efforts to keep the repository small, this project does not house the ExPORTER data files (~200MB). It does include a bash script `utils/get_csvs` which programatically downloads all of the filess. to download all of the files

The data are cleaned and preprocessed in the `Preprocessing.ipynb` notebook. It should be noted that some rows are dropped during this process:

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