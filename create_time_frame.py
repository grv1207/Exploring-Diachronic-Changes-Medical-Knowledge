import argparse
import commonFunctions as cf

def run(start_date, end_date, folder_path):

    range_file_list = [x for x in cf.getAllfiles(folder_path) if int(x)>=start_date and int(x)<= end_date]

    with open(str(start_date)+'_'+str(end_date),'a') as fout:
        for file in range_file_list:
            with open(folder_path+file,'r') as file_out:
                for line in file_out:
                    fout.write(line)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='for creating splits')

    parser.add_argument('--start_date', type=int,
                        help='start date of the time frame')
    parser.add_argument('--end_date', type=int,
                        help='inclusive end date of the time frame')


    parser.add_argument('--folder_path', type=str,
                        help='path of where file are stored', default='/media/gaurav/Elements/Thesis/data/mappedData/correct_yer_match/mapped_data/')
    args = parser.parse_args()

    run(args.start_date,args.end_date,args.folder_path)