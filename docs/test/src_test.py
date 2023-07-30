import multipleloader as xld
import time

""" main """
def main():

    """ csv test """
    if True:
        csv_path = ".\\test_datas.csv"
        csv_data = xld.load(csv_path)
        #print(csv_data)
        time.sleep(1)

    """ tsv test """
    if True:
        tsv_path = ".\\test_datas.tsv"
        tsv_data = xld.load(tsv_path)
        #print(tsv_data)
        time.sleep(1)

    """ json test """
    if True:
        json_path = ".\\test_datas.json"
        json_data = xld.load(json_path)
        #print(json_data)
        time.sleep(1)

    """ pickle test """
    if True:
        pickle_path = ".\\test_datas.pickle"
        pickle_data = xld.load(pickle_path)
        #print(pickle_data)
        time.sleep(1)

    """ pkl test """
    if True:
        pkl_path = ".\\test_datas.pkl"
        pkl_data = xld.load(pkl_path)
        #print(pkl_data)
        time.sleep(1)

    """ npy test """
    if True:
        npy_path = ".\\test_datas.npy"
        npy_data = xld.load(npy_path)
        #print(npy_data)
        time.sleep(1)

    """ npz test """
    if True:
        npz_path = ".\\test_datas.npz"
        npz_data = xld.load(npz_path)
        #print(npz_data)
        time.sleep(1)

if __name__ == "__main__":

    """ main program """
    main()

