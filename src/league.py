# accept queue button
accept_button = None

# 'in queue' label
queue_label = None

# keep searching for the 'in queue label' to know that the user is in queue
while queue_label is None:

	print('not in queue')

	try:
		queue_label = pyautogui.locateOnScreen('../res/queue.png',confidence=0.8)
	except:
		pass

# while queue label is present
# meaning we are not in champ select yet
while queue_label is not None:

	print('in queue')

	queue_label = pyautogui.locateOnScreen('../res/queue.png',confidence=0.8)
	
	# keep searching for accept button
	while accept_button is None:
		print('searching for accept button')
		try:
			accept_button = pyautogui.locateOnScreen('../res/accept-queue.png',confidence=0.8)
		except:
			pass

	print('found accept_button')
	# get the location of the accept button
	accept_location = pyautogui.center(accept_button)

	print('clicking it')
	# click it
	pyautogui.click(accept_location)


chat_box = None

while chat_box is None:
	print('searching for chat bot')
	try:
		chat_box = pyautogui.locateOnScreen('../res/chat-box.png',confidence=0.8)
	except:
		pass

print('found it')
chat_location = pyautogui.center(chat_box)

print('clicking chat')
pyautogui.click(chat_location)

print('spamming role' )
for i in range(20):
	pyautogui.write('top')
	pyautogui.press('enter')



		





