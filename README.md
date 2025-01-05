## Maps generator
`cartographer.py` generates an interactive map for the wiki from an `.csv` table.

The table should have the following three columns, repeating in the following order, with no column headers:

Time period | Person/Group[^1] | Location[^2]
--------------|-----------------|--------------

To get .csv table, make a normal table in Excel or Google Sheets and use "save as" function.

## Schedules from a map
`schedules.py` gets an interactive map code in `.json` format as an input and returns `.csv` table with schedules of every single person on the map. Afterwards, the schedules can be either added manually or using AutoWikiBrowser.

[^1]: See all available groups in groups.txt
[^2]: See all available locations in locations.txt
