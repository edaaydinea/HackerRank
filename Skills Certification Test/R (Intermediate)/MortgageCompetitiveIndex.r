# Complete the 'calculate_competitive_index' function below.

#' @param df_data Data frame data from 'csv' file
#' @return Data frame with processed data
calculate_competitive_index <- function(df_data) {
  
  # Consider only the applications that were approved
  df_approved <- subset(df_data, Action_taken == 1)
  
  # Calculate the total loan amount sanctioned by each bank each year in each country
  loan_amt_bank <- aggregate(Loan_amount ~ Year + Country + Inst_id, df_approved, sum)
  names(loan_amt_bank)[4] <- "Loan_amt_bank"
  
  # Calculate the total loan amount sanctioned by all banks each year in each country
  total_loan_amt_country <- aggregate(Loan_amt_bank ~ Year + Country, loan_amt_bank, sum)
  names(total_loan_amt_country)[3] <- "Total_loan_amt_country"
  
  # Merge the two data frames
  merged_data <- merge(loan_amt_bank, total_loan_amt_country, by = c("Year", "Country"))
  
  # Calculate the squared market-share for each bank
  merged_data$squared_market_share <- (merged_data$Loan_amt_bank / merged_data$Total_loan_amt_country)^2
  
  # Calculate the competitiveness index for each country as the sum of the squared market-share for all banks in that country
  competitive_index <- aggregate(squared_market_share ~ Year + Country, merged_data, sum)
  names(competitive_index)[3] <- "Competitive_index"
  
  # Sort the data frame by "Year" in ascending order and "Country" in alphabetical order
  competitive_index <- competitive_index[order(competitive_index$Year, competitive_index$Country),]
  
  # Round the competitiveness index to three digits
  competitive_index$Competitive_index <- round(competitive_index$Competitive_index, 3)
  
  return(competitive_index)

}

# DO NOT CHANGE THIS CODE

# Open connection
fptr <- file(Sys.getenv("OUTPUT_PATH"))
open(fptr, open = "w")

# Read input 'csv' file
df_input <- read.csv("/dev/stdin", stringsAsFactors = FALSE)

# Process result data set
df_output <- calculate_competitive_index(df_input)

# Save results as 'csv' file 
write.csv(df_output, fptr, row.names = FALSE)

# Close connection
close(fptr)
