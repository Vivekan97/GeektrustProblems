import sys
import helpers
from course_management import course_management


def main():

    input_file = sys.argv[1]
    with open(input_file, helpers.INPUT_FILE_MODE) as f:
        contents = f.read().split("\n")
    user_inputs = [content.split(" ") for content in contents]
    course_management(user_inputs)


if __name__ == "__main__":
    main()
