from tkinter import *
import pyautogui
import time

accept_button = None
queue_label = None
chat_box = None
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

		self.stop_button = Button(master,text="Stop",command=self.stop_script)
		self.stop_button.grid(row=2,column=1)

	def num_input(self):

		num = self.num_entry.get()

		if num == '':
			return 10
		elif num.isdigit():
			return int(num)
		else:
			return 10


	def whole_script(self):

		global queue_label
		global accept_button
		global chat_box
		global running

		# keep searching for the 'in queue label' to know that the user is in queue
		if queue_label is None and running:

			print('not in queue')
			try:
				queue_label = pyautogui.locateOnScreen('../res/queue.png',confidence=0.8)
			except:
				pass
		else:
			# while queue label is present
			# meaning we are not in champ select yet
			if queue_label is not None and accept_button is None and running:

				print('in queue')

				accept_button = pyautogui.locateOnScreen('../res/accept-queue.png',confidence=0.8)
				queue_label = pyautogui.locateOnScreen('../res/queue.png',confidence=0.8)

			else:

				# keep searching for accept button
				if accept_button is None and running:
					print('searching for accept button')
					try:
						accept_button = pyautogui.locateOnScreen('../res/accept-queue.png',confidence=0.8)
					except:
						pass

				else:	
					print('found accept_button')
					# get the location of the accept button
					accept_location = pyautogui.center(accept_button)

					print('clicking it')
					# click it
					pyautogui.click(accept_location)

					if chat_box is None and running:

						print('searching for chat bot')

						try:
							chat_box = pyautogui.locateOnScreen('../res/chat-box.png',confidence=0.8)
						except:
							pass

					else:	
						print('found it')
						chat_location = pyautogui.center(chat_box)

						print('clicking chat')
						pyautogui.click(chat_location)

						print('spamming role' )

						for i in range(self.num_input()):
							pyautogui.write(self.role_entry.get())
							pyautogui.press('enter')
							
						return None


		self.master.after(1000,self.whole_script)


	def start_script(self):

		global running
		running = True

		self.whole_script()
		

	def stop_script(self):

		global running
		running = False
		self.master.destroy()







def main():
	root = Tk()
	my_gui = LeagueGui(root)
	root.mainloop()

if __name__ == '__main__':
	main()
