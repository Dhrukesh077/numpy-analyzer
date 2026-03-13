import numpy as np


class DataAnalytics:

    def __init__(self):
        self.array = None

    # -------------------------------
    # CREATE ARRAY
    # -------------------------------

    def create_array(self):

        print("\nSelect Array Type")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter choice: "))

        if choice == 1:

            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements)

        elif choice == 2:

            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements).reshape(rows, cols)

        elif choice == 3:

            depth = int(input("Enter depth: "))
            rows = int(input("Enter rows: "))
            cols = int(input("Enter columns: "))

            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.array = np.array(elements).reshape(depth, rows, cols)

        print("\nArray Created Successfully")
        print(self.array)

    # -------------------------------
    # INDEXING & SLICING
    # -------------------------------

    def indexing_slicing(self):

        if self.array is None:
            print("Create array first")
            return

        print("\n1. Indexing")
        print("2. Slicing")

        choice = int(input("Enter choice: "))

        if choice == 1:

            row = int(input("Row index: "))
            col = int(input("Column index: "))

            print("Value:", self.array[row][col])

        elif choice == 2:

            r1 = int(input("Row start: "))
            r2 = int(input("Row end: "))
            c1 = int(input("Column start: "))
            c2 = int(input("Column end: "))

            result = self.array[r1:r2, c1:c2]

            print("Sliced Array:")
            print(result)

    # -------------------------------
    # MATHEMATICAL OPERATIONS
    # -------------------------------

    def math_operations(self):

        if self.array is None:
            print("Create array first")
            return

        print("\nChoose Operation")
        print("1 Addition")
        print("2 Subtraction")
        print("3 Multiplication")
        print("4 Division")
        print("5 Dot Product")

        choice = int(input("Enter choice: "))

        elements = list(map(int, input("Enter elements for second array: ").split()))
        second = np.array(elements).reshape(self.array.shape)

        if choice == 1:

            result = self.array + second

        elif choice == 2:

            result = self.array - second

        elif choice == 3:

            result = self.array * second

        elif choice == 4:

            result = self.array / second

        elif choice == 5:

            result = np.dot(self.array, second)

        print("\nResult:")
        print(result)

    # -------------------------------
    # COMBINE / SPLIT ARRAYS
    # -------------------------------

    def combine_split(self):

        if self.array is None:
            print("Create array first")
            return

        print("\n1 Combine Arrays")
        print("2 Split Array")

        choice = int(input("Enter choice: "))

        if choice == 1:

            elements = list(map(int, input("Enter elements for second array: ").split()))
            second = np.array(elements).reshape(self.array.shape)

            result = np.vstack((self.array, second))

            print("\nCombined Array:")
            print(result)

        elif choice == 2:

            parts = int(input("Enter number of parts: "))

            result = np.array_split(self.array, parts)

            print("\nSplit Arrays:")

            for r in result:
                print(r)

    # -------------------------------
    # SEARCH SORT FILTER
    # -------------------------------

    def search_sort_filter(self):

        if self.array is None:
            print("Create array first")
            return

        print("\n1 Search Value")
        print("2 Sort Array")
        print("3 Filter Values")

        choice = int(input("Enter choice: "))

        if choice == 1:

            value = int(input("Enter value to search: "))
            pos = np.where(self.array == value)

            print("Position:", pos)

        elif choice == 2:

            sorted_arr = np.sort(self.array)

            print("Sorted Array:")
            print(sorted_arr)

        elif choice == 3:

            value = int(input("Show values greater than: "))
            filtered = self.array[self.array > value]

            print("Filtered Values:")
            print(filtered)

    # -------------------------------
    # AGGREGATES
    # -------------------------------

    def aggregates(self):

        if self.array is None:
            print("Create array first")
            return

        print("\nChoose Aggregate Operation")
        print("1 Sum")
        print("2 Mean")
        print("3 Median")
        print("4 Standard Deviation")
        print("5 Variance")

        choice = int(input("Enter choice: "))

        if choice == 1:

            print("Sum:", np.sum(self.array))

        elif choice == 2:

            print("Mean:", np.mean(self.array))

        elif choice == 3:

            print("Median:", np.median(self.array))

        elif choice == 4:

            print("Standard Deviation:", np.std(self.array))

        elif choice == 5:

            print("Variance:", np.var(self.array))

    # -------------------------------
    # STATISTICAL FUNCTIONS
    # -------------------------------

    def statistics(self):

        if self.array is None:
            print("Create array first")
            return

        print("\nStatistical Operations")
        print("1 Minimum")
        print("2 Maximum")
        print("3 Percentile")
        print("4 Correlation")

        choice = int(input("Enter choice: "))

        if choice == 1:

            print("Minimum:", np.min(self.array))

        elif choice == 2:

            print("Maximum:", np.max(self.array))

        elif choice == 3:

            p = int(input("Enter percentile: "))
            print("Percentile:", np.percentile(self.array, p))

        elif choice == 4:

            elements = list(map(int, input("Enter elements for second array: ").split()))
            second = np.array(elements).reshape(self.array.shape)

            corr = np.corrcoef(self.array.flatten(), second.flatten())

            print("Correlation Matrix:")
            print(corr)


# --------------------------------
# MAIN MENU (CONSOLE UI)
# --------------------------------

def main():

    analyzer = DataAnalytics()

    while True:

        print("==============================")
        print(" Welcome to NumPy Analyzer")
        print("==============================")

        print("1 Create Numpy Array")
        print("2 Indexing / Slicing")
        print("3 Mathematical Operations")
        print("4 Combine / Split Arrays")
        print("5 Search / Sort / Filter")
        print("6 Aggregates")
        print("7 Statistical Functions")
        print("8 Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            analyzer.create_array()

        elif choice == 2:
            analyzer.indexing_slicing()

        elif choice == 3:
            analyzer.math_operations()

        elif choice == 4:
            analyzer.combine_split()

        elif choice == 5:
            analyzer.search_sort_filter()

        elif choice == 6:
            analyzer.aggregates()

        elif choice == 7:
            analyzer.statistics()

        elif choice == 8:
            print("Thank you for using NumPy Analyzer!")
            break


if __name__ == "__main__":
    main()