# 1) Identify the corrupt system in workbench (e.g. "SYS 3")
# 2) In WB, go to File > Scripting > Open Command Window > (Type the following lines):

badSystem = Project.GetSystem("SYS 3")
badSystem.Components = []
badSystem.Delete()

# 3) Save, close and reopen the project.
# More options at: https://discuss.ansys.com/discussion/2625/how-to-delete-corrupt-static-structural-systems-from-wb-project-page
