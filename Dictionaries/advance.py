defiMean = {
    "Business" : "\nThe term business refers to an organization or enterprising entity engaged in commercial, industrial, or professional activities.",
    "Economics" : "\nEconomics is the science which studies human behaviour as a relationship between ends and scarce means which have alternative uses.",
    "Leadership" : "\nLeadership is a process of social influence, which maximizes the efforts of others, towards the achievement of a goal.",
    "Education" : "\nEducation is both the act of teaching knowledge to others and the act of receiving knowledge from someone else. ",
}

print("\nBusiness    Economics    Leadership    Education")
print("\nYou can chooose one of thses")
n = input("\nEnter the term which you want to understand :\n")
print(defiMean.get(n, "Invalid Option"))