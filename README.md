# Sense, Detect and Avoid

### Contributing:
	- please see issues tab and assign yourself a task
	- issues assigned as TASK: are new functionalities to be added
	- issues assigned as PROBLEM: are actual "issues" to be fixed in current functionality

### Information regarding Interoperability and sdamain.py:
	- General overview: information about the obstacles, both moving and stationary, is sent  from the competition provided interoperability server. In other words, we must request the current status of all obstacles from server at a given rate[provided by the rules]. The competition has provided us the source for the interoperbility server so that we can emulate the competition setup.

	- Important to you:  I have added the source sdamain.py, this is the first program to be ran from all of your programs. However, it is not ran directly by you[discussed late]. I have also converted your programs in a python package [see __init__.py]. What all this means is that sdamain.py and all of other programs you write will be utilized by another program[it is in interop repo...although it doesn't matter to you] which contacts the interop server on your behalf and calls your functions [i.e. the two you write in sdamain.py]. So when all this is finished all your programs in the "sda" directory will be copied to the same directory as the program in the interop repo. So your first task is to integrate you current code into sdamain.py which is the only program exported by this package [ in other words, everything else you write is considered private] this means try to reference as few other functions ans possible in sdamain.py. I have commented sdamain.py as much as I could and even added an example where confusion might arise. NOTE: the only source that is relavent to you in the interop repo, that you just have to read (not clone or edit), is called libinterop/types.py. This was provided by AUVSI and contains the object format of the MovingObstacles and StationaryObstacles[ just used it as a reference].

	- Extra description about sdamain.py:
		- contains two functions:
			- async_routine(moving,stationary,error)
				- passed a list of moving,stationary obstacles
				- to understand their format you will unfortunately need to look into the interop repo under libinterop/types.py provided by AUVSI. That's the only thing outside this program you will need to understand
			- sync_routine()
				- this is where the main function for your program gets called (import it to sdamain.py and call it here)
			- These two functions are asynchronous, meaning access to global variables/data must be synchronized. I have provided an example in sdamain.py as to what that means[this is probably the most complex and confusing thing you will encounter].
