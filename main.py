from app.exercise_time import ExerciseTime
from app.menu import Menu
from app.login import LoginManager
from app.physical import PhysicalCheck
from app.points import PointManager
from app.stock import StockRegistration


def main() -> None:
    login_manager = LoginManager("admin", "1234")

    if not login_manager.login():
        return

    stock = StockRegistration()
    stock_name = stock.register_stock()

    physical = PhysicalCheck()
    physical.check_physical(stock_name)

    exercise_time = ExerciseTime()
    exercise_time.register_time()

    point_manager = PointManager()
    menu = Menu(point_manager)
    menu.select_menu()

main()
