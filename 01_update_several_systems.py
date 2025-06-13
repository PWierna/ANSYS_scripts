# 1) Identify the system names to update (e.g. "SYS 3", "SYS 31", "SYS 32")
# 2) In WB, go to File > Scripting > Open Command Window > (Type the following lines):


# List of system names to update
system_names = ["SYS 3", "SYS 31", "SYS 32"]

# Loop through each system and update it
for system_name in system_names:
    try:
        sys2update = Project.GetSystem(system_name)
        sys2update.Update()
        print("System {} updated successfully.".format(system_name))
    except Exception as e:
        print("Error updating {}: {}".format(system_name, e))
