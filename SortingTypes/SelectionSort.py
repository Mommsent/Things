def selection_sort (nums): #сортировка выбором
	#значение i соответствует тому, сколько значений было отсортировано
	for i in range (len(nums)):
		#Мы предпологаем, что первый элемент несортированного сегмента является наименьшим
		lowest_value_index = i
		for j in range (i+1, len(nums)):
			if nums[j < nums[lowest_value_index]]:
				lowest_value_index = j
		nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

random_list_of_nums = [12,8,3,20,11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)
#временная сложность O(n**2)

def insertion_sort(nums): #сортировка вставками
	# начинаем с первого элемента так как предпологаем что первый отсортирован
	for i in range(1, len(nums)):
		items_to_insert = nums[i]
		#сохраняем ссылку на индекс предыдущего элемента
		j = i-1
		#переместить все элементы отсортрованого сегмента вперёд, если они больше чем элементы для вставки
		while j >= 0 and nums[j] > items_to_insert:
			nums[j+1] = nums[j]
			j-=1
			#вставляем элемент
		nums[j+1] = items_to_insert
#временная стоимость O(n**2)

random_list_of_nums = [9,1,15,28,6]
insertion_sort(random_list_of_nums)
print(random_list_of_nums)

def bubble_sort(nums): #сортировка пузырьком
	swapped = True
	while swapped:
		for i in range(len(nums) - 1):
			if nums[i] > nums[i+1]:
				nums[i], nums[i+1] = nums[i+1], nums[i]
				swapped = True
#временная стоимость O(n**2)
random_list_of_nums = [5,2,1,8,4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

def merge(left_list, right_list):
	sorted_list = []
	left_list_index = right_list_index = 0
	left_list_length,right_list_length = len(left_list),len(right_list)
	for _ in range(left_list_length + right_list_length):
		if left_list_index < left_list_length and right_list_index < right_list_length:
			if left_list(left_list_index) <= right_list(right_list_index):
				sorted_list.append(left_list(left_list_index))
				left_list_index += 1
			else:
				sorted_list.append(right_list(right_list_index))
				right_list_index += 1

		elif left_list_index == left_list_length:
			sorted_list.append(right_list(right_list_index))
			right_list_index += 1

	return sorted_list

def marge_sort(nums):
	if len(nums) <= 1:
		return nums
	mid = len(nums) // 2
	left_list = marge_sort(nums[:mid])
	right_list = marge_sort(nums[mid:])
	return(left_list,right_list)

#временная стоимость O(n log (n))
random_list_of_nums=[120,45,68,250,176]
random_list_of_nums=marge_sort(random_list_of_nums)
print(random_list_of_nums)

def heapify(nums, heap_size, root_index): #Пирамидальная сортировка
	largest = root_index
	left_child = (2 * root_index) + 1
	right_child = (2 * root_index) + 2

	if left_child < heap_size and nums[left_child] > nums[largest]:
		largest = left_child

	if right_child < heap_size and nums[right_child] > nums[largest]:
		largest = right_child

	if largest != root_index:
		nums[root_index], nums[largest] = nums[largest], nums[root_index]
		heapify(nums, heap_size, largest)

def heap_sort(nums):
	n = len(nums)
	for i in range(n - 1, 0, -1):
		nums[i], nums[0] = nums[0], nums[i]
		heapify(nums, 1, 0)
# временная сложность O(n log (n))
random_list_of_nums=[35,12,43,8,51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)

def partition(nums, low, high): # быстрая сортировка
	pivot = nums[(low + high) // 2]
	i = low - 1
	j = high + 1
	while True:
		i += 1
		while nums[i] < pivot:
			i += 1
		j -= 1
		while nums[j] > pivot:
			j -= 1
		if i >= j:
			return j
		nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
	def _quick_sort(items, low, high):
		if low < high:
			split_index = partition(items, low, high)
			_quick_sort(items, low, split_index)
			_quick_sort(items, split_index + 1, high)
	_quick_sort(nums, 0, len(nums) - 1)

#временная сложность O(n log (n))
random_list_of_nums = [22, 5, 1, 18, 99]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

# втроенные сортировки
apples_eaten_a_day = [2, 1, 1, 3, 1, 2, 2]
apples_eaten_a_day.sort()
print(apples_eaten_a_day) # [1, 1, 1, 2, 2, 2, 3]

apples_eaten_a_day.sort(reverse=True)
print(apples_eaten_a_day) # [3, 2, 2, 2, 1, 1, 1]
# Reverse sort to get a new list
sorted_apples_desc = sorted(apples_eaten_a_day, reverse=True)
print(sorted_apples_desc) # [3, 2, 2, 2, 1, 1, 1]