# Populating the Database

To populate the justforplay database, issue the following command-line prompts
once in your VM and in the python_scripts folder of the JustForPlay repository:
    * dropdb justforplay
    * createdb justforplay
    * psql justforplay -af ../justforplay.sql
    * python zip.py (note: this command takes a few minutes to run)
    * python community.py
    * python subcommunity.py
    * python groups_to_messages.py

These commands set up your database, then load the Zip, Community, SubCommunity tables,
and then the groups_to_members script loads the remaining tables with randomly-generated
data.
