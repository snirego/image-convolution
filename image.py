# ----------------< Imports >----------------
import cv2
import numpy as np
import scipy.signal
import queue
import threading
import time
from multiprocessing import Process

# ----------------< Variables >----------------
start_time = time.perf_counter()

kernel_size = 10
kernel = ((1 / kernel_size**2) * np.ones(kernel_size**2))
kernel = kernel.reshape((kernel_size, kernel_size))

image_dir_path = 'image_dir/'
images_queue = queue.Queue()

deafult_image_id = 'deafult_id'

# ----------------< Functions >----------------
def image_to_gray(image_path, image_id):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(image_dir_path + image_id + 'gray' + image_path, gray)
    output = scipy.signal.convolve2d(gray, kernel)
    # cv2.imwrite(image_dir_path + str(image_id) + '.jpeg', output)
    cv2.imwrite(f'{image_dir_path}{str(image_id)}.jpeg', output)
    return gray

def push_image_to_queue(image):
    images_queue.put(image)

def pop_image_from_queue():
    return images_queue.get()

def image_to_gray_and_push_to_queue(image_path, image_id):
    image = image_to_gray(image_path, image_id)
    push_image_to_queue(image)

def print_queue():
    print(''.center(75, '-'))
    for i in range(images_queue.qsize()):
        print(pop_image_from_queue())
        print(''.center(75, '-'))

# ----------------< Main Program >----------------
for i in range(10):
    image_to_gray_and_push_to_queue('road.jpeg', i)

finish_time = time.perf_counter()
total_time_1 = finish_time - start_time
print(''.center(75, '-'))
print(f'{total_time_1} Seconds')
print(''.center(75, '-'))

for i in range(10):
    thread = threading.Thread(target=image_to_gray_and_push_to_queue, args=('road.jpeg', i))
    thread.start()

finish_time_2 = time.perf_counter()
total_time_2 = finish_time_2 - finish_time
print(f'{total_time_2} Seconds')
print(''.center(75, '-'))


print(f'Was faster X {int(total_time_1/total_time_2)} times!')
print(''.center(75, '-'))
# print_queue()