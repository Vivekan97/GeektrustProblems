import sys
import helpers
from course_management import CourseManagement


def main():

    input_file = sys.argv[1]
    with open(input_file, helpers.INPUT_FILE_MODE) as f:
        contents = f.read().split("\n")
    user_inputs = [content.split(" ") for content in contents]
    course_management_instance = CourseManagement(user_inputs)
    course_management_instance.course_management()


if __name__ == "__main__":
    main()
