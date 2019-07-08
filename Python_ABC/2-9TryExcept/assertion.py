Wood_Hill = {'ns':'green', 'ew':'red'}
Stone_Scissor = {'ns':'red', 'ew':'green'}

def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		elif stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		elif stoplight[key] == 'red':
			stoplight[key] = 'green'

	assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight )


switchLights(Wood_Hill)


# AssertionError: Neither light is red! {'ns':'green', 'ew':'yellow'}