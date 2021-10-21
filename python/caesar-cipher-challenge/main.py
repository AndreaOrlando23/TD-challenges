from caesar_cipher.message_visualizer import MessageVisualizer


def main():
    # Read the message and shift amount from the user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    visualizer = MessageVisualizer(message, shift)
    result = visualizer.print_ticket()

    print(result)


if __name__ == "__main__":
    main()
