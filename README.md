## cartographer
The cartographer receaves a CSV with positions of students at certain time periods and returns a json-file of interactive map for Fandom. CSV format is as follows:

Time period | Person/Group[^1] | Location[^2]
--------------|-----------------|--------------

To ensure the output map has the same properties as the source map:
1. Open the source map's code in the Fandom editor
2. Copy everything up to (but not including) the `markers` section
3. Paste the copied content into `start.json`

This will preserve all map settings like bounds, categories, and styling.

## schedules
The schedules generator receaves a json-file of interactive map and returns a CSV table with schedules of every single person on the map. 

[^1]: See all available groups in groups.txt
[^2]: See all available locations in locations.txt
