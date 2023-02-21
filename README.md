# binmodder
Python program for replacing strings in the .bin files for Galaxy On Fire 2. Also uses a version of random-googletrans, gof2translate

<b>Made for the GOF2 Google Translate Mod</b>

<h2>Dependencies:</h2>
gof2translate.py uses googletrans3.1.0a0 to prevent AttributeError: 'NoneType' object has no attribute 'group'
You will therefore need googletrans==3.1.0a0

<b>pip install googletrans==3.1.0a0</b>

<h2>How to use the GUI:</h2>
Run binModderGui.py or download on of the <a href=https://github.com/KroeteTroete/binmodder/releases/>releases</a> and execute binModderGui.exe

Select the .bin file you want to modify by clicking "Choose .bin file".

<h3>Using .txt files</h3>
Make a .txt file which contains the strings in the .bin file you want to replace (You can see the strings of a .bin file in a hex editor) and seperate the strings with a new line. (!Make sure the very last line is not empty!)
Import that .txt file into binmodder by clicking on "Choose strings to be replaced".

If you want to choose the replacements yourself, make another .txt file which contains the replacements for the strings in the same order, seperated by new lines and import it by clicking on "Choose replacements". Then click on "Replace".

<h3>Using the random-googletrans freature</h3>
When using gof2translate, any txt files imported as replacements txt will be ignored.
If you want to use the gof2translate feature, check the gof2translate box and click on "Replace".

<h3>Importing strings automatically</h3>
binmodder can also use <a href="https://github.com/KroeteTroete/gofdetect/">gof2detect</a>, which extracts all the strings from the bin files automatically.
To use this feature, select a bin file and click on "detect". Then choose the type of bin file you're modifying.

<h3>GOF2 Google Translate Mod:</h3>
<a href="https://www.moddb.com/mods/gof2-google-translated" title="View GOF2 Google Translated (Not finished at all) on Mod DB" target="_blank"><img src="https://button.moddb.com/popularity/medium/mods/56340.png" alt="GOF2 Google Translated (Not finished at all)" /></a>

