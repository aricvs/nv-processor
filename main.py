import re
import pandas as pd

# Regex patterns to match date + link and link only
date_link_pattern = r"\d{1,2}\/\d{1,2}\/\d{2,4}.*http[s]*\S+"
link_pattern = r"http[s]*\S+"

# Opens the log file and save the variable
with open("log.txt", "r") as file:
    log = file.read()

# List with all the substrings that start with a date and end with a link
job_msgs = re.findall(date_link_pattern, log)

# Lists comprehensions for the dates and links which are easier to get
dates = [match[:10] for match in job_msgs]
unformatted_links = re.findall(link_pattern, log)
links = [link for link in unformatted_links if "docs" not in link]

# Empty list for authors
authors = []

# Get only the message sender name (author) from each job_msg string
for match in job_msgs:
    author_start = match.find(" - ")
    author_end = match.find(": ")
    author_name = match[author_start + 3 : author_end]
    authors.append(author_name)

# Test to see if the data look good
# with open("dates.txt", "w") as file:
#     for date in dates:
#         file.write("%s\n" % date)
# with open("authors.txt", "w") as file:
#     for author in authors:
#         file.write("%s\n" % author)
# with open("links.txt", "w") as file:
#     for link in links:
#         file.write("%s\n" % link)
# print(len(dates), len(authors), len(links))

data = {"Date": dates, "Author": authors, "Link": links}
df = pd.DataFrame(data)

df.to_csv("jobs.csv", index=False)

print(df)
