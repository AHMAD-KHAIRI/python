from prettytable import PrettyTable

table = PrettyTable()
# table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"]) 
# table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386]) 
# table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769]) 
# table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

# add column to the table:
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# where table is our object and add_column is our method

# left-align table:
table.align = "l"
print(table)