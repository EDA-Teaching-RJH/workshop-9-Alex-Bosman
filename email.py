import re


emails = ["qvahxzeueq@nhs.net", "rwvqhptft@nhs.net", "njvun@nhs.net", "omkueltb@gov.uk", "qpzyqnlaq@nhs.net", "dkf*ggnu@gov.uk", "mtnurpnn@gov.uk", "wiq)jadaa@nhs.net", "fph@jp@ac.uk", "euktfrzm@gov.uk"]


'''
Prompts the user to input an email address
2. Accepts emails ending with '.ac.uk', '.gov.uk', or '.nhs.net'
3. Prints the specific domain type if valid (e.g., "Valid Academic Email", "Valid Government Email", "Valid
NHS Email")
4. Allows only letters and numbers in the username and domain.
5. Prints detailed feedback on why an email is invalid if it doesn't meet all criteria
'''


for x in emails:
    output = re.findall("@nhs.net$", x)
    print(output)



#"(@nhs.net$)"
#"(@gov.uk$)"