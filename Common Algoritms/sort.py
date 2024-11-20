# Sort two arrays based on one array's index accending
x_lst = [5, 3, 7, 9, 0, 1, 4, 2, 6, 8]
y_lst = [10, 1, 26, 18, 53, 15, 3, 2, 8, 6]

sorted_x, sorted_y = zip(*sorted(zip(x_lst, y_lst)))

print(f"Ascending sorted_x: {sorted_x}, sorted_y: {sorted_y}")

# Sort in descending order
sorted_x, sorted_y = zip(*sorted(zip(x_lst, y_lst), reverse=True))

print(f"Descending sorted_x: {sorted_x}, sorted_y: {sorted_y}")