from ride_management import RideManagement


def main():

    import sys
    import helpers
    input_file = sys.argv[1]
    with open(input_file, helpers.INPUT_FILE_MODE) as f:
        contents = f.read().split("\n")
        user_inputs = [content.split(" ") for content in contents]
        RideManagement(user_inputs).ride_management()


if __name__ == "__main__":
    main()
