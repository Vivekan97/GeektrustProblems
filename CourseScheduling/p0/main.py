import sys
import helpers
from scheduler import CourseScheduler


def main():

    input_file = sys.argv[1]

    with open(input_file, helpers.INPUT_FILE_MODE) as f:
        contents = f.read().split("\n")

    user_inputs = [content.split(" ") for content in contents]
    scheduler = CourseScheduler()

    for user_input in user_inputs:
        if user_input[0] == helpers.COURSE_OFFERING_MODE:
            if len(user_input) != helpers.OFFERING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                print(scheduler.add_course(user_input[1], user_input[2], user_input[3],
                                           int(user_input[4]), int(user_input[5])))
        if user_input[0] == helpers.COURSE_REGISTERING_MODE:
            if len(user_input) != helpers.REGISTERING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                print(scheduler.register_course(user_input[1], user_input[2]))

        if user_input[0] == helpers.COURSE_ALLOTING_MODE:
            if len(user_input) != helpers.ALLOTING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                for message in scheduler.course_allotment(user_input[1]):
                    print(message)

        if user_input[0] == helpers.COURSE_CANCELLING_MODE:
            if len(user_input) != helpers.CANCELLING_INPUT_COUNT:
                print(helpers.INPUT_ERROR_MESSAGE)
            else:
                print(scheduler.cancel_registration(user_input[1]))

    # print(user_inputs)


if __name__ == "__main__":
    main()
