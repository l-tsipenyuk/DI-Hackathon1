# DI-Hackathon1: Energy Generation Tracker

**Project Description:**
Python-based command-line tool that allows users to track and analyze energy generation data from an open database. The tool uses Object-Oriented Programming principles to structure the code effectively and implement the following features:

1. **Data Retrieval:** The tool is able to download and work with data from BP Energy Stats Excel database.
Data Source: https://www.energyinst.org/statistical-review/resources-and-data-downloads

2. **Data Analysis:** There are various functionalities to analyze the electricity generation data by country. Users can input specific queries:

   - Retrieve historical energy generation data in TWh. User inputs a country and receives historical energy production data categorized by source from the oldest available date to the most recent.
   - Query electricity generation mix by share. Users can query a specific country and year to get generation mix percentage. Additionally, there is an option to compare generation mix in a country across multiple years.
   - Compare electricity generation mix across countries. Users can query several countries and year enabling comparison between these countries.
   - Export historical data to Excel. Users can export fetched historical data to Excel for further analysis.
   - Export data to PostgreSQL Database. Users can export the fetched data for a specific country to a PostgreSQL database with the following actions available: create a table, fill in the data and delete the table in the database.
 

3. **User Interaction:** A user-friendly command-line interface enables users to input commands, queries and handles potential errors.


The project contributes to environmental awareness by providing a tool for analyzing shift towards energy transition in different countries from 1985 to 2022. Users can gain insights into energy generation patterns and potentially more effectively analyze countries' energy policies.
