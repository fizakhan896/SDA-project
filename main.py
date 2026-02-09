import matplotlib
matplotlib.use('TkAgg')

from dashboard import show_dashboard

if __name__ == "__main__": #run dashboard only when this file is started, not when its imported
    show_dashboard()
