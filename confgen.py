# write .conf files for etscbu
# version 1

def make(location, bacname, profilename, progver):
    f = open(location + "\\.conf", "w")
    f.write("bacname: " + bacname + "\n")
    f.write("profile: " + profilename + "\n")
    f.write("progver: " + progver + "\n")
    f.write("CONFEND")
    f.close