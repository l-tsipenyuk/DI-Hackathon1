# DI-Hackathon1

**Project Title:** Energy Generation Tracker

**Project Description:**
Python-based command-line tool that allows users to track and analyze energy generation data from an open database. The tool should use Object-Oriented Programming principles to structure the code effectively and implement the following features:

1. **Data Retrieval:** The tool is able to download and work with data from BP Energy Stats Excel database.
Data Source: https://www.energyinst.org/statistical-review/resources-and-data-downloads

2. **Data Analysis:** There are various functionalities to analyze the electricity generation data by country. Users can input specific queries:

   - User inputs a country and receives historical energy production data categorized by source from the oldest available date to the most recent.
   - Users can query a country, year and get the electricity generation mix in percentage.
   - Users can query several countries, year and get the electricity generation mix in percentage to compare these countries.
   - Users can export fetched historical data to Excel.
   - Users can export the fetched data for a specific country in a PostgreSQL database (options available: create a table, fill in the data and delete the table in the database).
 

3. **User Interaction:** There is a user-friendly command-line interface that allows users to input commands and queries.


The project contributes to environmental awareness by providing a tool for analyzing shift towards energy transition in different countries from 1985 to 2022. Users can gain insights into energy generation patterns and potentially more effectively analyze countries' energy policies.
