# CSV Combiner

Write a command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. Your script should output a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came (only the file's basename, not the entire path).
Use `filename` as the header for the additional column.

## Input & Output
We will run your code as follows
```
$ ./csv-combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

However, the CSV files inside the fixtures are not the only files we will run
through. We will run your code through files > 2 GB to see if you hit memory limits.

## How to Run
I have written the code in python so please use Python 3 while running the file through command line.
The program is extensible and re-usable, and can be easly used with multiple and large files.
I used chunking in order to make the program work for large files when provided as input.

##  Considerations
* You should use coding best practices. Your code should be re-usable and extensible.
* Your code should be testable by a CI/CD process. Unit tests are important.
