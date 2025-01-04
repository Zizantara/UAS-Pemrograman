from data.prosesdata import SupermarketProcess
from view.viewdata import SupermarketView

if __name__ == "__main__":
    process = SupermarketProcess()
    view = SupermarketView(process)
    view.run()