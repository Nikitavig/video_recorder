import cv2
import numpy as np
import os
import pyautogui
import time
import subprocess
from datetime import datetime


SAVE_PATH = 'video'
TIMER = 1


FORMAT = 'mp4'
# FORMAT = 'avi'


def reboot():
	try:
		subprocess.call(['shutdown', '/-r'])
	except Exception as e:
		print(e)

def main():

	start_time = datetime.today().timestamp()
	
	output = SAVE_PATH + '/' + f"""video_{datetime.today().day}-{datetime.today().month}-{datetime.today().year}_{datetime.today().hour}-{datetime.today().minute}.{FORMAT}"""
	print(f"Название файла >>> {output}")

	img = pyautogui.screenshot()
	img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	#get info from img
	height, width, channels = img.shape
	# Define the codec and create VideoWriter object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(output, fourcc, 10.0, (width, height))

	while True:
		# Проверяем не пора ли перезагрузить компьютер
		# Если пора, то сохраняем файл 
		if (datetime.today().timestamp() - start_time) > TIMER:
			# Сохраняем видео
			out.release()
			cv2.destroyAllWindows()
			break
		else:
			try:
				img = pyautogui.screenshot()
				image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
				out.write(image)
				StopIteration(0.1)
			except KeyboardInterrupt:
				break

	print("Перезагрузка")
	# Перезагружаем компьютера
	reboot()


if __name__ == '__main__':
	main()