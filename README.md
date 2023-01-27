## Final Project of Data Engineer Bootcamp (Digital Skola)

> Created by: M Faathir. Creation date: 28 Jan 2023.

Brief Description:
- The goal is to establish an end-to-end data pipeline.
- Data source is obtained by sending GET API request to https://pikobar.jabarprov.go.id/ (public data of Covid-19 cases in West Java, Indonesia)
- Environments for building data warehouse (Airflow, MySQL, Postgres) is set up by using Docker container.
- Automatic data refresh is configured and scheduled using Airflow dag.
  - Dag name = `summary_daily_finalproject`
- Data warehouse is configured using MySQL (dbeaver) and PostgreSQL (PGAdmin).
  - Dimension table: `dim_case`, `dim_district`, `dim_province`
  - Fact table: `district_daily`, `province_daily`

--

Naming conventions
- fp = final project
- dim = dimension
