#input phase
appliance_name = input("Enter the name of the aplliance:")
appliance_cost = float(input("Enter the cost of the appliance: "))

if appliance_cost > 1000:
    warranty_cost = appliance_cost *0.10
else:
    warranty_cost = appliance_cost *0.05

#process phase
total_cost = appliance_cost + warranty_cost

#output phase
print("Appliance Name: {}".format(appliance_name))
print("Appliance Cost: ${:.2f}".format(appliance_cost))
print("Warranty Cost: ${:.2f}".format(warranty_cost))
print("Total Cost (Appliance + Warranty): ${:.2f}".format(total_cost))

    
