# Program to calculate and print the number of hours spend on different Jira issues per day and a total for the week
# Take in data
# The user will be asked for the current number of Jira issues
number_jira_issues = int(input("How many Jira issues did you work on this week? "))
jira_issues = [None for i in range(number_jira_issues) ] # define array jira_issues
# The user will be asked for the names of the current Jira issues
for i in range(len(jira_issues)):
    jira_issues = input(str("Please write all the titles one by one of the current Jira issues: "))
# The user will be asked for number of hours spend on each current Jira issue per week day
# hours_jira_issues = [None for i in range(number_jira_issues) ] # define array hours_jira_issues
hours_jira_issues = [None, None, None ] # define array hours_jira_issues

for i in range(len(jira_issues)):
    print("Issue number", i+1, " With the title: ", jira_issues[i])
# The user will be asked
    hours_jira_issues = int( input("How many hours did you work on the above Jira issue: "))

# Perform calculations
# The program will calculate the number of hours spend on each Jira issue per day
# The program will calculate the total number of hours spend on each Jira issue for the current week 

# Output data
# The program will print the number of hours spend on each Jira issue per day
# The program will print the total number of hours spend on each Jira issue for the current week 

# Debug lines below to help debug
print("I globale : ", dir() ) # Debug line to print all active names in namespace