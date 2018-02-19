story = "At the end of world war 2, the {0} stormed into the nazi's once controlled  bunker that served as the finale resting place for Adolf Hitler. There the  found no one alive. They only found one body though. The body was identified as Adolf Hitler. His body was found to be covered in blood. Belongings such as anime  and a body pillow where found in his personal collection underneith his desk. The soldiers brought the body out of the bunker and placed it in a near by ditch for the world to see. They then buried it in a collection of tears." 
name = raw_input ("enter a name")
verb = raw_input ("enter a verb")
verb2 = raw_input ("enter a verb")
adjusted =story.format(name, verb)
adjusted2 = name + "was" + verb  + "by a bus."

print(adjusted)


