#Count the number of entries in the data set (expected outcome = 33469)
awk 'END {print NR}' airline_stats.csv

#Calculate Average Carrier Delay (expected outcome = 7.03537)
awk -F',' 'NR > 1 {sum += $1; count++} END {if (count > 0) print sum / count}' airline_stats.csv #the answer is off for last 2 digits (can't figure out why tho)
#-F',': This sets the field separator to a comma (since it's a CSV file).
#NR > 1: Skips the first line (header).
#sum += $1: Adds the values from the first column (pct_carrier_delay).
#count++: Increments the count for each data row.
#END {if (count > 0) print sum / count}: After processing all lines, it calculates and prints the average if there are any data rows.

#Count Airlines with Carrier Delay Above 10% (expected outcome = 6549)
awk -F',' 'NR > 1 && $1 > 10 {count++} END {print count}' airline_stats.csv

#Calculate the Percentage of Airlines with No Weather Delay (expected outcome = 31.8474)
awk -F',' 'NR > 1 {total++} NR > 1 && $3 == 0 {count++} END {if (total > 0) print (count / total) * 100 "%"}' airline_stats.csv

#challenge 1: Aggregate data to find average delays by airline. Write a script that uses `awk` to calculate the average carrier delay per airline. 
awk -F',' '
NR > 1 {
    airline = $4;                 
    sum[airline] += $1;      
    count[airline]++;          
}
END {
    print "Average Carrier Delay per Airline:"
    for (airline in sum) {
        avg = sum[airline] / count[airline];  
        printf "%s: %.4f\n", airline, avg;  
    }
}' airline_stats.csv





