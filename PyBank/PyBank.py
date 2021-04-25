#!/usr/bin/env python
# coding: utf-8

# In[14]:


## import libraries to view csv
import os
import csv


# In[17]:


## Set variables for months, total months, current rev, previous rev, total rev, rev change and total rev change.
months=[]
months_count=0
total_rev=0
current_rev=0
previous_rev=0
rev_change=0
rev_changes=[]


# In[45]:


## set path to csv file on directory
csvpath = os.path.join("budget_data.csv")
path_output=os.path.join("budget_data_results.txt")


# In[46]:


## open csv file using path, and use csv.reader to read the csv file.
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
## read header first    
    next(csvreader)
    
## iterate through each row after the header
### count the months by adding +1 to count
    for row in csvreader:
        months_count = months_count + 1
        months.append(row[0])
        current_rev = int(row[1])
        total_rev = total_rev + current_rev
        
        if months_count > 1:
            rev_change = current_rev - previous_rev
            rev_changes.append(rev_change)
        previous_rev = current_rev


# In[47]:


sum_pl = sum(rev_changes)
avg_pl_chg= sum_pl / (months_count -1)
max_change= max(rev_changes)
min_change= min(rev_changes)
max_month_index=rev_changes.index(max_change)
min_month_index=rev_changes.index(min_change)
max_month= months[max_month_index]
min_month=months[min_month_index]


# In[48]:


print("Financial Analysis")
print("__________________________")
print("                          ")
print(f"Total Months: {months_count}")
print(f"Total: ${total_rev}")
print(f"Average Change: ${avg_pl_chg}")
print(f"Greatest Increase in Profits: {max_month} ${max_change}")
print(f"Greatest Decrease in Profits: {min_month} ${min_change}")


# In[49]:


# print to terminal and save / export to new file
output=(
    f"Financial Analysis \n"
    f"__________________________\n"
    f"                          \n"
    f"Total Months: {months_count}\n"
    f"Total: ${total_rev}\n"
    f"Average Change: ${avg_pl_chg}\n"
    f"Greatest Increase in Profits: {max_month} ${max_change}\n"
    f"Greatest Decrease in Profits: {min_month} ${min_change}\n")
    
    


# In[50]:


print(output)


# In[56]:


text_file=open("budget_results.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("____________________\n")
text_file.write("                     \n")
text_file.write("Total months: " + str(months_count) + "\n")
text_file.write("Total: "  +  str(total_rev)  +  "\n")
text_file.write("Average Change: "  +  str(avg_pl_chg) + "\n")
text_file.write("Greatest Increase in Profits: "  + str(max_change)  +  "\n")
text_file.write("Greatest Decrease in Profits: "  + str(min_change)  + "\n")
text_file.close()


# In[ ]:




