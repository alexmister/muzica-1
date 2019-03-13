from repo.FileRepository import FileRepository
from service.service import MusicService
from ui.console import UI

class App(object):
    def main(self):

        student_repo = FileRepository("data/data")
        sc = MusicService(student_repo)
        cons = UI(sc)
        cons.run()

if __name__ == '__main__':
    try:
        app = App()
        app.main()
    except Exception as ex:
        print("Exceptie in aplicatie: ", ex)

