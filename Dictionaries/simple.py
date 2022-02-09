dayConversion = {
    "Mon" : "\nMonday\n",
    "Tue" : "\nTuesday\n",
    "Wed" : "\nWednesday\n",
    "Thr" : "\nThrusday\n",
    "Fri" : "\nFriday\n",
    "Sat" : "\nSaturday\n",
    "Sun" : "\nSunday\n",
}

n = input("Enter Day : ")
print(dayConversion.get(n, "\nNot a Valid Day!!"))