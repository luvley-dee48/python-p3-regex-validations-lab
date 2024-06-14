import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name_pattern = r"^(?:[A-Z][a-z]*[-'\s]?)+$"
name_regex = re.compile(name_pattern)


phone_pattern = r"^\+?\d{0,3}[-.\s]?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_pattern)


email_pattern = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_pattern)

