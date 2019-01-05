# Udacity Full Stack Web Developer Project Three - Logs Analysis

## Objective
Create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Instructions

**Step 1:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org).

**Step 2:** Clone the VM configuration from this [github repo](https://github.com/udacity/fullstack-nanodegree-vm).

**Step 3:** Download the database dump file from [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

**Step 4:** Extract and copy the `newsdata.sql` file to the `/vagrant` directory that was created in Step 2.

**Step 5:** Clone `analyze_log.py` and `analyze_logdb.py` from this [github repo](https://github.com/tcu93/FSWD3) into the `/vagrant` directory.

**Step 6:** Open a terminal and navigate to the same `/vagrant` directory mentioned in previous steps and type the following:

```
# Install & Configure VM
vagrant up

# Log into VM
vagrant ssh

# [Inside VM]
cd /vagrant

# Confirm existence of all required files
ls

# Populate database with database dump file
psql -d news -f newsdata.sql

# Run Log Analyzer Tool
python analyze_log.py

# Log out of machine
# <Ctrl + D>

# Destroy machine once done
vagrant destroy

```
## Screenshot of Output
![Capture.PNG](https://github.com/tcu93/FSWD3/blob/master/Capture.PNG)
