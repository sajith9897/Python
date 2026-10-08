web_development = ["rahul", "noorudeen", "glen"]
data_science = ["aromal", "pranav", "amal"]
ui_ux_design = ["kichu", "vettu", "nandhu"]

all_participants = [web_development, data_science, ui_ux_design]
print (all_participants)

web_development.append ("sajith")
print(web_development)

data_science.insert(1,"sooraj")
print(data_science)

del ui_ux_design[-1]
print (ui_ux_design)

new_data_science = data_science.copy()
data_science.clear()
print(new_data_science)
print("data science=", data_science)

print ("First 2:",web_development[:2])

new_data_science_length = [len(x) for x in new_data_science]
print ("Lenght:", new_data_science_length)

# asha_presnt = ("Asha" in web_development or "Asha" in new_data_science or "Asha" in ui_ux_design)
# print (asha_presnt)

print ("Asha" in web_development or "Asha" in new_data_science or "Asha" in ui_ux_design)

# first_participants = ( web_development[0], new_data_science[0], ui_ux_design[0])
# print("First participants:", first_participants)

print ("First participants:", (web_development[0], new_data_science[0], ui_ux_design[0]))
