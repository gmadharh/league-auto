from tkinter import *
import pyautogui
import time

running = False

class LeagueGui:

	def __init__(self,master):

		self.master = master
		master.title("League Auto")

		self.role_label = Label(master,text="Role: ")
		self.role_label.grid(row=0,column=0)

		self.role_entry = Entry(master)
		self.role_entry.grid(row=0,column=1)

		self.num_label = Label(master,text="Num times to call role: ")
		self.num_label.grid(row=1,column=0)

		self.num_entry = Entry(master)
		self.num_entry.grid(row=1,column=1)

		self.start_button = Button(master,text="Start",command=self.start_script)
		self.start_button.grid(row=2,column=0)

		self.stop_button = Button(master,text="Stop")
		self.stop_button.grid(row=2,column=1)

	def num_input(self):

		num = self.num_entry.get()

		if num == '':
			return 10
		elif num.isdigit():
			return int(num)
		else:
			return 10

	def start_script(self):

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

		for i in range(self.num_input()):
			pyautogui.write('top')
			pyautogui.press('enter')








def main():
	root = Tk()
	my_gui = LeagueGui(root)
	root.mainloop()

if __name__ == '__main__':
	main()
