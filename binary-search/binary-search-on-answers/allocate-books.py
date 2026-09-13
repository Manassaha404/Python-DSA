# You are given an array books of n integers, where books[i] is the number of pages in the i-th book.
# You are also given an integer m representing the number of students.

# All books need to be allocated to the students such that:

# Each student gets at least one book.
# Each book is allocated to exactly one student.
# The allocation must be in contiguous order — i.e., a student cannot be assigned a non-contiguous set of books. 
# (Book i can only be allocated to a student if books 0, 1, ..., i-1 have already been allocated.)

# The goal is to minimize the maximum number of pages assigned to any single student.

# Return the minimum possible value of the maximum pages a student has to read. If allocation is not possible (e.g., m > n), return -1.

# Example 1: 
# Input: books = [12, 34, 67, 90], m = 2
# Output: 113
# Explanation: Split as [12, 34, 67] and [90] → max = 113.
# This is the most balanced split possible; any other split gives a higher max.

# Example 2: 
# Input: books = [10, 20, 30, 40], m = 2
# Output: 60
# Explanation: Split as [10, 20, 30] and [40] → max(60, 40) = 60.

# Constraints:

# 1 <= n <= 10^5
# 1 <= books[i] <= 10^5
# 1 <= m <= 10^5




# Time Complexity: O(n) — single pass through the books array
# Space Complexity: O(1) — constant extra space
def shouldStudents(books:int, min_page:int) -> int:
    count = 0 
    sum_of_pages = 0 
    for book in books:
        if sum_of_pages + book > min_page:
            count += 1
            sum_of_pages = book
        else:
            sum_of_pages += book 
    return count + 1  



# Time Complexity: O(n log(sum)) — binary search over [max(books), sum(books)] range (log(sum) steps),
#                  each step calls shouldStudents which is O(n). Sorting is O(n log n),
#                  which is dominated by O(n log(sum)) for large sums.
# Space Complexity: O(n) — for the sorted copy of books (Python's sorted() creates a new list)
def allocateBooks(books:list[int], student:int) -> int:
    n = len(books)
    if student > n:
        return -1 
    books = sorted(books) 
    low = books[n - 1]
    high = sum(books) 
    while low <= high:
        mid = low + (high - low) // 2 
        should_students = shouldStudents(books, mid) 
        if should_students > student:
            low = mid + 1 
        else:
            high = mid - 1 
    return low 

print(allocateBooks([15, 10], 2)) 
        
