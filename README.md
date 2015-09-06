# panorama-sorter

Some cameras (at least the Canon PowerShot ones) save photos taken with the panorama assistant as STA_1234.JPG, STB_1235.JPG, STC_1236.JPG and so on. If your file browser or terminal sorts your files by name or not at all, finding those panorama photos which belong to one set can be very tedious.

This little script sorts them into subfolders named after the first file of the set.

Just place the script into the same directory as the panorama photos and run it from your terminal as `python panorama-sorter.py`.

It should work on both Linux and Windows, but is definitely not sufficiently tested yet, so do make backups of your photos and other data before you run it!
