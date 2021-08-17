import schedule


def execute_job():
    print("I am working!")


# def hello_world():
#     print("hello world")


schedule.every(5).seconds.do(execute_job)
# schedule.every(7).seconds.do(hello_world)

while True:
    schedule.run_pending()
    # time.sleep(1)
