import time

def timestamp(method):
	def wrapper(*args, **kwargs):
		ts = time.time()
		result = method(*args, **kwargs)
		te = time.time()
		time_result = int((te-ts) * 1000)
		message = (
			f'[I] '
			f'{method.__qualname__}'
			f' took '
			f'{time_result}'
			f'ms to complete, or ~'
			f'{time_result//60000}'
			f'm, or ~'
			f'{time_result//1000}'
			f's'
		)
		#print('[I] {} took {}ms to complete'.format(method.__name__, int((te-ts) * 1000)))
		print(message)
		return result
	return wrapper