#Output a menu of automotive services and the corresponding cost of each service
services = {'Oil change' : 35, 
            'Tire rotation' : 19, 
            'Car wash' : 7, 
            'Car wax' : 12}

print('Davy\'s auto shop services')
print('Oil change -- $%d' % (services['Oil change']))
print('Tire rotation -- $%d' % (services['Tire rotation']))
print('Car wash -- $%d' % (services['Car wash']))
print('Car wax -- $%d' % (services['Car wax']))
print('')

#Prompt the user for two services from the menu
first_service = input('Select first service:\n')
if first_service == '-':
  services['No service'] = 0 #Adds 'No service' to 'services' dictionary for later use
  first_service = ('No service')

second_service = input('Select second service:\n')
if second_service == '-':
  services['No service'] = 0 #Adds 'No service' to 'services' dictionary for later use
  second_service = ('No service')
print('')

#Output an invoice for the services selected. Output the cost for each service and the total cost.
print('Davy\'s auto shop invoice\n')
if first_service == 'No service':
  print('Service 1: %s' % (first_service))
else: 
  print('Service 1: %s, $%d' % (first_service, services[first_service]))

if second_service == 'No service':
  print('Service 2: %s' % (second_service))
else:
  print('Service 2: %s, $%d' % (second_service, services[second_service]))
print('')

invoice = (services[first_service]) + (services[second_service])
print('Total: $%d' % (invoice))
