## Final Project of Data Engineer Bootcamp (Digital Skola)

> Created by: M Faathir. Creation date: 28 Jan 2023.

Brief Description:
- The goal is to establish a data pipeline using Airflow.
- Data source is obtained by sending GET API request to https://pikobar.jabarprov.go.id/ (public data of Covid-19 cases in West Java, Indonesia)
- Data warehouse is configured using MySQL and PostgreSQL
  - Dimension table: `dim_case`, `dim_district`, `dim_province`
  - Fact table: `district_daily`, `province_daily`
