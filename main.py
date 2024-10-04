import pendulum


def main():
    print(f'Hello world!\n'
          f'Today is {pendulum.now(tz='UTC').format('YYYY-MM-DD HH:mm:ss z')}.n'
          )


if __name__ == '__main__':
    main()
