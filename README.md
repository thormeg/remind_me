# Remind me!
A handy utility for creating reminders for important events happening in your life. This utility is designed to be run twice a month to give users an overview of important dates coming up in their calendar.

This provides a handy on-device experience for those not wishing to store their important dates in the cloud or other hosted service.

Created using Python and Tkinter.

# Installation
TBD - Command line application only at the moment.

# How to run
From the command line execute:
>$ python run.py

# How it works
Remind me! works by showing important dates on a split schedule broken into approximately two week halves:

* On the first of the month
* At the middle of the month (16th)

Where in each case the user will see the important date 2-4 weeks prior to it occurring.

E.g. Important date `20 Mar 2020` will be shown for the time period `1-15th March` (inclusive). This event will fall off notifications from the `16th March`, where date range `1-15th April` 

This is designed to give the user several weeks advanced notice of the event before it occurs.

# Entering data
Data can be stored on the main page of the application and all dates should be in the format `'%d %b %Y'` which appears as `20 Mar 2021`.

Each data row is converted from the text box into JSON, complete data rows in-app would appear as:
> 1 May 2020 May Day

> 25 Dec 2020 Christmas

# Plans
* Increase input safety for user
* Rewrite in PyQT or similar framework for better UI.
