tagReplace
==========
Takes 2 input files:
- a csv file including a list of values (max 2 values/columns per line),
- a template file (whatever format).
For each line in the csv file:
    read the whole template file
    do a search %TAGNAME% and replace with the corresponding value in the csv file
    write the resulting file with new file name
The first line of the csv file is treated as a header and defines the tag names. Max 2 columns are supported.
The name of the resulting file is build like this:
 <value in first column>-<template file name and extension>

Usage: tagRaplce.py -l <listfile-csv> -a <templatefile> [-o <outDir>]

Example:

csv file in.csv:
    GROUPCN;BASEDN
    App_read;OU=EndUsers,OU=Groups,DC=test,DC=me
    App_admin;OU=AdminUsers,OU=Groups,DC=test,DC=me

Template file templ.txt:
    <FIELD_VALUE>
        CN=%GROUPCN%,%BASEDN%
    </FIELD_VALUE>

Run command: pythin tagReplace.py -l in.csv -a templ.txt

Ouput:
  Tag read     : GROUPCN;BASEDN
  Handling line: App_read;OU=EndUsers,OU=Groups,DC=test,DC=me
  Creating file: .//App_read-templ.txt
  Handling line: App_admin;OU=AdminUsers,OU=Groups,DC=test,DC=me
  Creating file: .//App_admin-templ.txt

File App_admin-templ.txt looks like this:
  <FIELD_VALUE>
    CN=App_admin,OU=AdminUsers,OU=Groups,DC=test,DC=me
  </FIELD_VALUE>
