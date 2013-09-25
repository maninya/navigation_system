navigation_system
=================

1) Run "readings.py" to collect signal strength readings at different locations. Take some pictures and label them, and store the names in img.py.
2) All the readings are placed in "final_readings.txt".
3) Now to find the location, run "./prog.sh" from shell.
4) This program runs "find_loc.py" which measures signal strengths and compares it with the readings just collected.
5) If there is a match, it means an approx location has been found, we get a voice output. Otherwise, step 8.
6) Then "img.py" is run automatically and a picture is taken, and compared with the image database.
7) We get a voice output according to match or not.
8) If no match, signal strength reading and a picture is taken and added to the database.
9) Thus the system "learns", i.e. gets better with use.
