def main():
    # Dictionary to store student names and heights
    student_heights = {}

    # Input heights for three students
    for i in range(3):
        name = input(f"Enter student {i+1}'s name: ")
        height = float(input(f"Enter {name}'s height in cm: "))
        student_heights[name] = height

    # Find the tallest student
    tallest_student = max(student_heights, key=student_heights.get)

    # Output the result
    print(f"{tallest_student} is the tallest with a height of {student_heights[tallest_student]} cm.")

if __name__ == "__main__":
    main()
